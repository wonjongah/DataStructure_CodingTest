# li = [1, 2, 3, 4, 5, 1, 2, 3]
# new_li = []
# for a in li:
#     if a not in new_li:
#         new_li.append(a)
# print(new_li)

def print_nums(nums, count):
    if nums[count] == 0:
        return
    elif count < len(nums)-1:
        print(nums[count])
        count += 1
        # Recursion
        print_nums(nums, count)
    else:
        return
        

nums = input().split()
count = 0
print_nums(nums, count)