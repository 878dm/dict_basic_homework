def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    a={}
    x=0
    s=0
    for i in txt :
        if i.isalpha() :
            x+=1
        elif i.isdigit():
            s+=1
    a["LETTERS"]=x
    a["DIGIT"]=s
    return a
print(count_all("Hello World"))