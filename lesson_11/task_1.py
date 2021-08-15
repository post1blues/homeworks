class Person:
    def __init__(self, first_name, last_name, age, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday

    def say_fullname(self):
        print(f"{self.first_name} {self.last_name}")

    def say_age(self):
        print(f"{self.age} years old")

    def say_birthday(self):
        print(f"My birthday is {self.birthday}")

    def say_hello(self):
        print(f"Hello! My name is {self.first_name}")


class Student(Person):
    def __init__(self, first_name, last_name, age, birthday, year_of_study, direction, marks=None):
        super().__init__(first_name, last_name, age, birthday)
        self.year_of_study = year_of_study
        self.direction = direction
        self.marks = marks if marks else []

    def get_mark(self, mark):
        self.marks.append(mark)

    def print_all_marks(self):
        print(", ".join(self.marks))

    def increase_year_of_study(self, num_of_years):
        self.year_of_study += num_of_years

    def say_year_of_study(self):
        print(f"I'm studying for {self.year_of_study} years")

    def change_direction(self, new_direction):
        self.direction = new_direction

    def say_direction(self):
        print(f"My direction is {self.direction}")


class Teacher(Person):
    def __init__(self, first_name, last_name, age, birthday, subject_of_teach, experience, salary):
        super().__init__(first_name, last_name, age, birthday)
        self.subject_of_teach = subject_of_teach
        self.experience = experience
        self.salary = salary

    def say_subject_of_teach(self):
        print(f"I teach {self.subject_of_teach}")

    def say_salary(self):
        print(f"My salary is {self.salary}")

    def increase_experience(self, num_of_years):
        self.experience += num_of_years

    def say_experience(self):
        print(f"My experience is {self.experience} years")
