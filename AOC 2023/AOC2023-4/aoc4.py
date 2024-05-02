with open("AOC 2023/AOC2023-4/input.txt", "r") as file:
    a = [i.split(" | ") for i in file]  
b=[]
for i in a:
    x= i[1].split(" ")
    b.append(x)
    
print(b)
