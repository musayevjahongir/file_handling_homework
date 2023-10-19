def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data).read()
    a=[]
    for i in f:
        if i.isdigit():
            a.append(i)
    return a
print(main("data/data03.txt"))
# Read data from file
