# Method Overloading Example 
class MathOperations:
    def add(self, a=0, b=0, c=0):
        return a + b + c

obj = MathOperations()

print("Sum of 2 numbers:", obj.add(5, 10))
print("Sum of 3 numbers:", obj.add(5, 10, 15))
print("Sum with 1 number:", obj.add(7))


# Method Overriding Example
class Parent:
    def show_message(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show_message(self):
        print("This is the Child class method (overridden).")

parent_obj = Parent()
child_obj = Child()

parent_obj.show_message()  
child_obj.show_message() 
