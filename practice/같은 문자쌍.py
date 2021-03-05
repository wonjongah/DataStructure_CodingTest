def is_same(string1, string2):
    s1 = list(string1)
    s2 = list(string2)

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(is_same("yes", "sey"))
print(is_same("uy", "ui"))