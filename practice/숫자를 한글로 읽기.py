def readNumber(n):
  units = ["", "십", "백", "천", "만", "십만", "백만", "천만"]
#   [''] + list('십백천만')
  nums = '일이삼사오육칠팔구'
  result = []
  i = 0
  while n > 0:
    n, r = divmod(n, 10)
    if r > 0:
      result.append(("" if nums[r-1] == "일" else nums[r-1]) + units[i])
    i += 1
  return ''.join(result[::-1])

print(readNumber(15493))