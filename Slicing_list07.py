def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list = ['a','b','c','d','e','f']
    return list[::-1]
print(main(list,'n'))