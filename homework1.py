"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second # відповідь піддивився :(

# моя спроба

# if first and second:
#     return

#   pass


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second) # по аналогії з попереднім
#    pass


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """

    return type(first) is type(second) # google
    #pass


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    except ValueError:
        print('Enter integer, please')

    return first_value * second_value
    #pass


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    # сумніваюсь, що це правильна конструкція
    except ValueError:
        print("Not valid input data")

    return int(first_value)*int(second_value)
    #pass


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    return text in word

    #pass


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    for x in range(13):
        if x != 5 and x != 7:
            return [x]
    #pass


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
for i in data:
    if i <= 0:
        data.remove(i)
#     pass


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    for k in string.ascii_lowercase:
        for v in string.digits:
            print({k, v}) # воно якось каряво призначає k,v
    # pass


# def simple_sort(data: List[int]) -> List[list]:
#     """
#     Sort list of ints without using built-in methods.
#     Examples:
#         simple_sort([2, 9, 6, 7, 3, 2, 1])
#         >>> [1, 2, 2, 3, 6, 7, 9]
#     Returns:

#simple_sort[2, 9, 6, 7, 3, 2, 1]
#for i in simple_sort:
#    if simple_sort[i] > simple_sort[i+1]:
#        simple_sort # не знаю, як задати, щоб два елементи помінялись місцями

#
#     """
#     pass