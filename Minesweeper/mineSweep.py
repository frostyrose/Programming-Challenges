minefield = []
def checkSurround(x,y,m,n):
    count = 0
    global minefield
    #Check North
    if(0 <= y - 1 and 0 <= x and minefield[x][y-1] == "*"):
        count += 1
    #Check NorthWest
    if(0 <= y - 1 and 0 <= x - 1 and minefield[x-1][y-1] == "*"):
        count += 1
    #Check West
    if(0 <= y and 0 <= x -1 and minefield[x-1][y] == "*"):
        count += 1
    #Check SouthWest
    if(n > y + 1 and 0 <= x - 1 and minefield[x-1][y+1] == "*"):
        count += 1
    #Check South
    if(n > y + 1 and 0 <= x and minefield[x][y+1] == "*"):
        count += 1
    #Check SouthEast
    if(n > y + 1 and m > x + 1 and minefield[x+1][y+1] == "*"):
        count += 1
    #Check East
    if(0 <= y and m > x + 1 and minefield[x+1][y] == "*"):
        count += 1
    #Check NorthEast
    if(0 <= y - 1 and m > x + 1 and minefield[x+1][y-1] == "*"):
        count += 1
    return str(count)

def mineSweep():
    global minefield
    restrictions = raw_input().split(" ")
    m = int(restrictions[0])
    n = int(restrictions[1])
    field = 1
    while not(m == 0) and not(n == 0):
        minefield = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            raw = raw_input()
            data = []
            for char in raw:
                data.append(char)
            for j in range(n):
                minefield[i][j] = data[j]
        for i in range(m):
            for j in range(n):
                if(not minefield[i][j] == "*"):
                    minefield[i][j] = checkSurround(i, j, m, n)
        print "Field #" + str(field) + ":"
        for i in range(m):
            print "".join(minefield[i])
        field += 1
        restrictions = raw_input().split(" ")
        m = int(restrictions[0])
        n = int(restrictions[1])

    
