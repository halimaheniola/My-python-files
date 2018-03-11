 #from module_directory import oop # or
from Module_directory.oop import ShapesCalc as Sc # module__dir is seen as a package
# if an empty file is in the  same folder whith the file to be imported. 
class MathCalc(Sc):
    def perimeter_circle(self):
        radius = input("Enter radius")
        return 2 * self.pi * float(radius)
  
class NewMathCalc(MathCalc):
    pass
my_perimeter = NewMathCalc()
print(my_perimeter.perimeter_circle())



from module_directory.oop import Customer
