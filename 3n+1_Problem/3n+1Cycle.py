def cycleCount(num):
    count = 1
    while(num > 0 and not num == 1):
        if (num % 2 == 0):
            num /= 2
        else:
            num = (3*num) + 1
        count += 1
    return count

def maxCycle(start, end):
    cycleCounts = []
    for num in range(start,end+1):
        cycleCounts.append(cycleCount(num))
    return max(cycleCounts)

raw = raw_input()
data = raw.split(" ")
print data[0] +  " " + data[1] + " " + str(maxCycle(int(data[0]),int(data[1])))
