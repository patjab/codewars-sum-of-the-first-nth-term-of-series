def series_sum(n):
    answer = 0
    for x in range(1, n+1):
      if x == 1:
        answer += 1
      else:
        answer += ((4+(3*(x-2))) ** -1)
    return "%.2f" % answer
