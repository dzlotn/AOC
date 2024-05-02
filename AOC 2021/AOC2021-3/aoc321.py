with open ("AOC321/aoc321.txt","r") as file:
    lista = [x.strip() for x in file]
n = []
for j in range(len(lista[0])):
    a=[]
    for i in range(len(lista)):     
        a.append(int(lista[i][j]))   
    n.append(a) 

g = "" 
e=""
for i in n: 
    g+=str(max(i,key=i.count))
    e+=str(min(i,key=i.count))
print(f"Gamma: {g} or {int(g,2)}")
print(f"Epsilon: {e} or {int(e,2)}")
print(int(g,2)*int(e,2))


