def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=0
    f=open (data).read()
    for i in f:
        if i.isdigit():
            s+=int (i)
    return s
print(main("data/data07.txt"))
# Read data from file