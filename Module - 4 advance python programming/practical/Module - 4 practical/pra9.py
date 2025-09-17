# Single Inheritance
class Parent:
    def display_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def display_child(self):
        print("This is the Child class.")

obj = Child()
obj.display_parent()
obj.display_child()


# Multiple Inheritance
class Mother:
    def show_mother(self):
        print("This is the Mother class.")

class Father:
    def show_father(self):
        print("This is the Father class.")

class Child(Mother, Father):
    def show_child(self):
        print("This is the Child class.")

obj = Child()
obj.show_mother()
obj.show_father()
obj.show_child()


# Multilevel Inheritance
class Grandparent:
    def display_grandparent(self):
        print("This is the Grandparent class.")

class Parent(Grandparent):
    def display_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def display_child(self):
        print("This is the Child class.")

obj = Child()
obj.display_grandparent()
obj.display_parent()
obj.display_child()


# Hierarchical Inheritance
class Parent:
    def display_parent(self):
        print("This is the Parent class.")

class Child1(Parent):
    def display_child1(self):
        print("This is Child1 class.")

class Child2(Parent):
    def display_child2(self):
        print("This is Child2 class.")

obj1 = Child1()
obj2 = Child2()

obj1.display_parent()
obj1.display_child1()

obj2.display_parent()
obj2.display_child2()


# Hybrid Inheritance
class A:
    def method_a(self):
        print("This is Class A.")

class B(A):
    def method_b(self):
        print("This is Class B.")

class C(A):
    def method_c(self):
        print("This is Class C.")

class D(B, C): 
    def method_d(self):
        print("This is Class D.")

obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()
