def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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
    return max(a)
print(main("data/data08.txt"))
# Read data from file