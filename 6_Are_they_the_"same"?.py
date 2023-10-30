# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    elif len(array1) != len(array2):
        return False
    else:
        for i in range(len(array1)):
            if sorted(array1)[i]**2 == sorted(array2)[i]:
                continue
            else:
                return False
        return True
