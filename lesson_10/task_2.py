
class Doggy:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        print(f"Human age of this dog: {self.age_factor * self.age}")



dog1 = Doggy(2)
dog1.human_age()

dog2 = Doggy(3)
dog2.human_age()