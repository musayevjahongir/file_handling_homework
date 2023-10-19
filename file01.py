def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data).read().split(",")
    a=[]
    for i in f:
        a.append(int (i))
    return a
print(main("data/data01.txt"))
# Read data from file