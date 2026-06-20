from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  def pack(self) -> str:
        return "Envoltorio de papel"
  def material(self) -> str:
        return "Papel"

class Bottle(FoodPackage):  
    def pack(self) -> str:
        return "Botella"
    def material(self) -> str:
        return "Plástico"
      
class Glass(FoodPackage):  
    def pack(self) -> str:
        return "Vaso"
    def material(self) -> str:
        return "Cartón"

class Box(FoodPackage):  
    def pack(self) -> str:
        return "Caja"
    def material(self) -> str:
        return "Cartón"