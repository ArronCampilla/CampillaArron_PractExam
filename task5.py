class Triangle:
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2= side2
        self.side3= side3
side1 = int(input("side1="))
side2 = int(input("side2="))    
side2 = int(input("side2="))

   
class computerPerimeter(Triangle):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
        return (side1*side2*side3)
        
print(str(computerPerimeter(Triangle)))