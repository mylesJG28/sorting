def swap(alist, index):
    a = alist[index]
    b = alist[index+1]
    alist[index] = b
    alist[index+1] = a
    return (alist)
