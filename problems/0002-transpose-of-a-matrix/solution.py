def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    l=[]
    # l1=[]
    for i in range(len(a[0])):
        l1=[]
        for j in range(len(a)):
            l1.append(a[j][i])
        l.append(l1)
    return l

