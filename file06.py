def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data, mode="r")
    a=f.readlines()
    l=[]
    for i in a:
        l.append(len(i)-1)
    l[-1]+=1
    return l
print(main("data/data06.txt"))
# Read data from file