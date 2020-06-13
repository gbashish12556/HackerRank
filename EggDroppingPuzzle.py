def nofOfTrials(egg,floor):
    trials = [[0 for k in range(floor+1)] for n in range(egg+1)]
    for n in range(1,egg+1):
        for k in range(floor+1):
            if k == 1:
                trials[n][k] = k
            elif n == 1:
                trials[n][k] = k
            else:
                trials[n][k] = 1+max(trials[n-2][k-1],trials[n-1][floor-k+1])
    return min(trials[egg-1])

testCases = int(input())

for n in range(testCases):
    array = list(map(int,input().split(" ")))
    egg,floor = array[0],array[1]
    value = nofOfTrials(egg,floor)
    print(value)