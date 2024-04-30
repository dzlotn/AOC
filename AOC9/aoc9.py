def checkZeros(list):
    if list[0]==0:
        return True
    else: return False

def recursion(line):
    newData = []
    for i in range(len(line)-1):
        newData.append(line[i]-line[i+1])
    print(newData)
    
    if checkZeros(newData):
        return 0
        
    return recursion(newData) +line[-1]

def main():
    sum = 0
    n = []
    file = open("AOC9/aoc9.txt","r")
    for line in file:
        converted = [int(i) for i in line.split(" ")]
        x=recursion(converted)
        sum+=x
        n.append(x)
        
    print(sum)
    print(n)
    
main()
    