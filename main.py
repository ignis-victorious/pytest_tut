#  _______________
#  Import LIBRARIES
#  Import FILES
#  _______________


class Person:
    def __init__(self, fname: str, lname: str, age: int) -> None:
        self.fname: str = fname
        self.lname: str = lname
        self.age: int = age

    @property
    def full_name(self) -> str:
        return f"{self.fname} {self.lname}"

    def update_age(self, new_age: int) -> None:
        if new_age > 0:
            self.age = new_age
            # self.age = new_age + 1  # To test the test error
            return
        raise ValueError


john: Person = Person(fname="John", lname="Smith", age=55)
print(vars(john))
print(vars(john).keys())
print(vars(john).values())


# if __name__ == "__main__":
#     main()


#  _______________
#  Import LIBRARIES
#  Import FILES
#  _______________
