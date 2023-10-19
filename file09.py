def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=[]
    f=open(data).read()
    for i in f:
        if i.isdigit():
            a.append(i)
    return min(a)
print(main("data/data09.txt"))
# Read data from file