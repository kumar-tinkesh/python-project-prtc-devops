import math

class Car: 
    """
    docstring
    """

    def __init__(self, engine, tires):
        """
        initating method
        Dunder Method
        """
        self.engine = engine
        self.tires = tires

    
    def description(self):
        print(f"A car with an {self.engine} engine and {self.tires} tires")

    
    def wheel_circum(self):
        if len(self.tires) > 0:
            return self.tires[0].circumfrence
        else:
            return 0



class Tire:

    def __init__(self, tire_type, width, ratio, diemeter, brand="Toyota", construction="R"):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diemeter = diemeter
        self.brand = brand
        self.construction = construction

    
    def circumfrence(self):
       
        total_diameter = self._side_wall_inches() * 2 + self.diemeter
        return round(total_diameter * math.pi, 1)


    def __repr__(self) -> str:
        """
        Represantation the tire information in the standard 
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}" + f"{self.construction}{self.diemeter}") 

    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4


class SnowTier(Tire):
    def __init__(self, tire_type, width, ratio, diemeter, chain_thickness, brand="Toyota", construction="R"):
        Tire.__init__(self, tire_type, width, ratio, diemeter, brand="Toyota", construction="R")

        self.chain_thickness = chain_thickness

    def circumfrence(self):
        total = (self._side_wall_inches() + self.chain_thickness) *2 + self.diemeter
        return round(total * math.pi, 1)

