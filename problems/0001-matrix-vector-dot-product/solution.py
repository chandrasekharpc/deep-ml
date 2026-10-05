def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	l=[]
	if len(a) != len(b):
		return -1
	for i in range(len(a)):
		tot=0
		for j in range(len(a[0])):
			tot+=a[i][j]*b[j]
		l.append(tot)
	return l
