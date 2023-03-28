class Person:
    def __init__(self, student, pre, mid, fin):
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin
        self.__student = student

    def display(self):
        print("The Grade of ", self.__student, "in Prelims is ", self.__pre, "in Midterms is ", self.__mid,
              "in Finals is", self.__fin, "The Average is", self.grade())

    def grade(self):
        return (self.__pre + self.__mid + self.__fin) / 3


class Std1(Person):
    pass


class Std2(Person):
    pass


class Std3(Person):
    pass


std1 = Std1("Student1", 75, 85, 90)
std1.display()
std2 = Std2("Student2", 65, 75, 80)
std2.display()
std3 = Std3("Student3", 69, 79, 99)
std3.display()
