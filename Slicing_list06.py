def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    list = ['a','b','c','d','e','f']
    return list[:-1:3]
print(main(list))