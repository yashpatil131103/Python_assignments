class Student:
    count = 0   # class variable

    @classmethod
    def show_count(cls):
        print("Total students:", cls.count)

# Calling class method without creating an object
Student.show_count()
