#converts input to integer list
with open("AOC121/input.txt","r") as file:
    lista = [int(line) for line in file]
#iterates through list and sums the # of lines that are decreasing in size
count1 = sum(lista[i]< lista[i+1] for i in range(len(lista)-1))
count2 = sum(sum(lista[i:i+3])< sum(lista[i+1:i+4]) for i in range(len(lista)-3))
print(f"Challenge 1: {count1}\nChallenge 2: {count2}")
    
