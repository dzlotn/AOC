file = open("AOC122/aoc122.txt","r")
def testblank(line):
    if line.strip() == "":
        return True
    return False

listofLists = []
lista = []
dict = {}
for line in file: 
    if not testblank(line):
        lista.append(int(line))
    else:
        listofLists.append(sum(lista))
        lista=[]
# for index,ele in enumerate(listofLists):
#     dict[index] = ele
s = sorted(listofLists)

print(s[-1]+s[-2]+s[-3])


        