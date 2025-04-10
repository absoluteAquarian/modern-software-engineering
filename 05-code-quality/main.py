"""
A simple Python program
"""


def expensive_op(number):
    """
    This function performs arithmetic on a number
    :param number: The number
    :return: A value derived from the input
    """
    return number * 999 * 1000 // 2


def slow_func(lst):
    """
    This function generates a new lines based on the contents of an input list
    :param lst: The input list
    :return: A new list derived from the input
    """
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result


def main():
    """
    A basic main function
    :return: None
    """
    numbers = list(range(1000))
    slow_func(numbers)
    print("Done")


if __name__ == "__main__":
    main()
