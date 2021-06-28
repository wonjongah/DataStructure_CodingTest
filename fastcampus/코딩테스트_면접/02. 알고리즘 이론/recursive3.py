def function(data):
    if data == 1:
        return data
    print(data)
    if data % 2 == 1:
        data = (3 * data) + 1
        return function(data)
    else:
        data = int(data / 2)
        return function(data)

print(function(3))