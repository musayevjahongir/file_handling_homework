def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data).read()
    a=[]
    for i in f:
        if not i.isdigit():
            a.append(i)
    return a
print(main ("data/data04.txt"))
# Read data from file