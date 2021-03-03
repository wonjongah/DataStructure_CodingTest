def multiple(data):
	if data <= 1:
		return data
	return data * multiple(data - 1)
	
print(multiple(10))