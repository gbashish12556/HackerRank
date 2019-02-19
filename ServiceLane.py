def serviceLane(n, cases,width):
    result = []
    for i in range(n):
        result.append(min(width[cases[i][0]:cases[i][1]+1]))
    return result

width   = "2 3 1 2 3 2 3 3"
width = list(map(int, width.split(" ")))
cases = [[0,7]]
n = len(cases)
print(serviceLane(n, cases,width))