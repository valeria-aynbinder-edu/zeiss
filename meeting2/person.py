class Person:

    def __init__(self, id, first_name, last_name, age, phone_number=None):
        # print(f"Called __init__ with id {id}")
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age

    def is_child(self):
        print(f"Called is_child for id {self.id}")
        return self.age <= 16


    def __str__(self):
        return f"{self.id} : {self.first_name} {self.last_name}"



class Student(Person):
    pass



valeria = Person("123456789", "Valeria", "aynbinder", 35)
student = Student(987654321, "Dan", "Dan", 25)



