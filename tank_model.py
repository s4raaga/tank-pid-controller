"""


"""

# Water tank class.
class Tank:
    def __init__(self, area, max_flow, drain_k):
        self.area = area # Tank area.
        self.max_flow = max_flow # Maximum flow rate.
        self.drain_k = drain_k # Drain rate.
        self.level = 0.0

    def step(self, valve_percent, dt):
        """
        Change in water level based on how open the valve is.
        
        Arguments:
        valve_percent = how open the valve is as a %. 
        dt = time step amount.

        Returns:
        new_level = new tank level 
        """

        # Inflow (from valve)
        inflow = (valve_percent / 100) * self.max_flow

        # Outflow (from gravity)
        outflow = self.drain_k * self.level

        # Flow (vol / sec) -> Water level change for New Level
        new_level = (self.level + (inflow - outflow)) / (self.area * dt)






        new_level = 0;

        return new_level
    

    