"""Simulation harness — runs the tank + PID experiments and saves plots."""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tank_model import Tank
from pid_controller import PIDController

# ── Parameters ────────────────────────────────────────────────────────────────
AREA     = 1.0    # m²   — tank cross-sectional area
MAX_FLOW = 2.0    # m³/s — max inflow at 100% valve
DRAIN_K  = 0.5    # 1/s  — gravity-drain coefficient (outflow = k * level)
SETPOINT = 2.0    # m    — target water level
DT       = 0.1    # s    — simulation timestep
DURATION = 60.0   # s    — total run length

# Tuned PID gains
KP = 25.0
KI =  2.0
KD =  3.0

PLOTS_DIR = "plots"


def run_simulation(Kp, Ki, Kd, setpoint=SETPOINT, duration=DURATION, dt=DT):
    """Run one experiment; return (times, levels, valve_commands)."""
    tank = Tank(area=AREA, max_flow=MAX_FLOW, drain_k=DRAIN_K)
    pid  = PIDController(Kp=Kp, Ki=Ki, Kd=Kd)

    times, levels, valves = [], [], []
    t = 0.0

    while t <= duration:
        times.append(t)
        levels.append(tank.level)
        valve = pid.update(setpoint, tank.level, dt)
        valves.append(valve)
        tank.step(valve, dt)
        t = round(t + dt, 6)  # avoid floating-point drift

    return times, levels, valves


def plot_step_response(times, levels, valves, setpoint):
    """Two-panel plot: water level and valve command over time."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    ax1.plot(times, levels, color="#2563eb", linewidth=1.8, label="Level")
    ax1.axhline(setpoint, color="#dc2626", linewidth=1.2,
                linestyle="--", label="Setpoint")
    ax1.set_ylabel("Water Level (m)")
    ax1.set_ylim(bottom=0)
    ax1.set_title(f"PID Step Response  —  Kp={KP}, Ki={KI}, Kd={KD}")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(times, valves, color="#16a34a", linewidth=1.5, label="Valve %")
    ax2.set_ylabel("Valve Position (%)")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylim(0, 105)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(PLOTS_DIR, "step_response.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved {path}")


def plot_gain_comparison(setpoint):
    """P vs PI vs PID on the same axes to show effect of each term."""
    configs = [
        ("P only",  KP,  0.0, 0.0, "#f59e0b"),
        ("PI",      KP,  KI,  0.0, "#8b5cf6"),
        ("PID",     KP,  KI,  KD,  "#2563eb"),
    ]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axhline(setpoint, color="#dc2626", linewidth=1.2,
               linestyle="--", label="Setpoint")

    for label, kp, ki, kd, color in configs:
        times, levels, _ = run_simulation(kp, ki, kd, setpoint)
        ax.plot(times, levels, label=label, color=color, linewidth=1.8)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Water Level (m)")
    ax.set_ylim(bottom=0)
    ax.set_title("P vs PI vs PID — Gain Comparison")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(PLOTS_DIR, "gain_comparison.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved {path}")


if __name__ == "__main__":
    os.makedirs(PLOTS_DIR, exist_ok=True)

    times, levels, valves = run_simulation(KP, KI, KD)
    plot_step_response(times, levels, valves, SETPOINT)
    plot_gain_comparison(SETPOINT)
