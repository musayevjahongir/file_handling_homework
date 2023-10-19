def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data, mode="r")
    a=f.readlines()
    l=[]
    for i in a:
        l.append(len(i)-1)
    l[-1]+=1
    return max(l)
print(main("data/data10.txt"))
# Read data from file