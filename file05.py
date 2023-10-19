def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
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
    return [len(f)-len(a), len(a)]
print(main("data/data05.txt"))
# Read data from file