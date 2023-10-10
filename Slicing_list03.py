def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    list = ['a','b','c','d']
    list1 = list[::-1]
    return list+list1
print(main(list))