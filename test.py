#  _______________
#  Import LIBRARIES
import pytest

#  Import FILES
from main import Person

#  _______________


# def test_person_creation() -> None:
#     test_instance: Person = Person(fname="John", lname="Smith", age=55)
#     assert test_instance.fname == "John"  # "Johns" to force a failed test
#     assert test_instance.lname == "Smith"
#     assert test_instance.age == 55


def test_person_creation() -> None:
    test_instance: Person = Person(fname="John", lname="Smith", age=55)
    expected_key: list[str] = [
        "fname",
        "lname",
        "age",
    ]
    expected_val: list[str | int] = [
        "John",
        "Smith",
        55,
    ]

    assert list(vars(test_instance).keys()) == expected_key
    assert list(vars(test_instance).values()) == expected_val


# def test_person_creation() -> None:
#     test_instance: Person = Person(fname="John", lname="Smith", age=55)
#     expected: list[str] = ["fname", "lname", "age"]  # To fail: ["fname", "name", "age"]

#     assert list(vars(test_instance).keys()) == expected
#     assert test_instance.fname == "John"
#     assert test_instance.lname == "Smith"
#     assert test_instance.age == 55


def test_full_name() -> None:
    test_instance_a: Person = Person(fname="John", lname="Smith", age=55)
    assert test_instance_a.full_name == "John Smith", (
        "Something is wrong with the full name property!"
    )
    test_instance_b: Person = Person(fname="James", lname="Smith", age=55)
    assert test_instance_b.full_name == "James Smith", (
        "Something is wrong with the full_name property!"
    )
    test_instance_c: Person = Person(fname="abc", lname="def", age=55)
    assert test_instance_c.full_name == "abc def", (
        "Something is wrong with the full_ name property!"
    )


def test_setting_age() -> None:
    test_instance_a: Person = Person(fname="John", lname="Smith", age=55)
    test_instance_a.update_age(new_age=100)
    assert test_instance_a.age == 100, "No respect for a venerable age!"
    # test_instance_b: Person = Person(fname="John", lname="Smith", age=55)
    # test_instance_b.update_age(new_age=-1)
    # assert test_instance_b.age == -1


def test_setting_age_with_invalid_input() -> None:
    test_instance: Person = Person(fname="John", lname="Smith", age=55)
    with pytest.raises(expected_exception=ValueError):
        # test_instance.update_age(new_age=-10)  # This will raise an error but we want to check the error is raised!
        test_instance.update_age(new_age=-10)
