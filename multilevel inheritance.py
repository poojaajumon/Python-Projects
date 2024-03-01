# multilevel inheritance
class A:
    def show1(self):
        print("this is class A")
class B(A):
    def show2(self):
        print("this is class B")
class C(B):
    def show3(self):
        print("this is class C")

obj=C()
obj.show1()
obj.show2()
obj.show3()
