def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data).read()
    return len (f)
print(main("data/data02.txt"))
# Read data from file