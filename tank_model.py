"""


"""

# Water tank class.
class Tank:
    def __init__(self, area, max_flow, drain_k):
        self.area = area # Tank's cross-sectional area.
        self.max_flow = max_flow # Maximum inflow rate when valve is 100% open.
        self.drain_k = drain_k # Drain / leak rate.
        self.level = 0.0 # Current water height.

    def step(self, valve_percent, dt):
        """
        Change in water level based on how open the valve is.
        
        Arguments:
        valve_percent = how open the valve from 0 to 100. 
        dt = timestep amount.

        Returns:
        new_level = new tank level.
        """

        # Inflow (from valve)
        inflow = (valve_percent / 100) * self.max_flow

        # Outflow (from gravity)
        outflow = self.drain_k * self.level

        # Flow (vol / sec) -> Water level change for New Level
        new_level = self.level + (inflow - outflow) / self.area * dt






        new_level = max(0.0, new_level)

        return new_level
    

    