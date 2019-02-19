def acmTeam(topic):
    attendees = len(topic)
    topicLength = len(str(topic[0]))
    result = []
    for i in range(1,attendees):
        for j in range(i):
            totalcount = 0
            for k in range(topicLength):
                if topic[i][k] == "1" or topic[j][k] == "1":
                        totalcount +=1
                result.append(totalcount)
    print(result)
    finalResult = [max(result), result.count(max(result))]
    return finalResult

topic = ["10101","11100","11010","00101"]
acmTeam(topic)
