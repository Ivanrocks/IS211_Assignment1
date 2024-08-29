def list_divide(numbers, divide = 2):
    """
        The function returns the number of elements in the numbers list that are divisibleby divide
    """
    result = 0
    for number in numbers:
        if number%divide == 0:
            result+=1
    return result

class ListDivideException(Exception):
    """
    ListDivideException is a custom exception class that will be raised when a test case fails
    """
    pass

def test_list_divide():
    """
        Testcases for listDivide.
        If a test case fails there will be a Custom Exception raised
    """
    if list_divide([1,2,3,4,5]) != 2:
        raise ListDivideException("Error: Test 1")

    if list_divide([2,4,6,8,10]) != 5:
        raise ListDivideException("Error: Test 2")

    if list_divide([30,54,63,98,100],10) != 2:
        raise ListDivideException("Error: Test 3")

    if list_divide([]) != 0:
        raise ListDivideException("Error: Test 4")

    if list_divide([1,2,3,4,5], 1) != 5:
        raise ListDivideException("Error: Test 5")

if __name__ == "__main__":
    test_list_divide()