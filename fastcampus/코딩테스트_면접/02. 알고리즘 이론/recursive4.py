def func(data):
	if data == 1:
		return 1
	elif data == 2:
		return 2
	elif data == 3:
		return 4
	else:
		return func(data-1) + func(data -2) + func(data - 3)
    
print(func(5))