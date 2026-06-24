"""


"""


class Tank:
    def __init__(self, area, qmax, drain_k):
        self.area = area
        self.qmax = qmax
        self.drain_k = drain_k
        self.level = 0.0

    def step(self, valve_percent, dt):
        """Advance one timestep; return new level"""
        return 
    

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint, measurement, dt):
        """Return valve command (0–100)"""
        return 