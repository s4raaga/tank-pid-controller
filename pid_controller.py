"""Discrete PID controller with anti-windup."""


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd # Proportional, integral, derivative gains.
        self.integral = 0.0 # Running sum of error.
        self.prev_error = 0.0

    def update(self, setpoint, measurement, dt):
        """
        How much the valve should be adjusted.

        Params:
        setpoint = target water level.
        measurement = current tank water level.
        dt = timestep amount (same as tank)


        Returns:
        change = valve command (0–100)
        
        """

        # Calculate error & add to running sum.
        error = setpoint - measurement
        self.integral += error * dt

        # Calculate rate of change in error.
        derivative = (error - self.prev_error) / dt

        # PID Adjustment
        adjustment = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)

        # Anti-windup: undo integral accumulation if output is saturated.
        if adjustment < 0 or adjustment > 100:
            self.integral -= error * dt

        # Update & return adjustment value btwn 0 & 100.
        self.prev_error = error

        return max(0, min(100, adjustment))

        