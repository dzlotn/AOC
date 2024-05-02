with open("AOC221/input.txt","r") as file:
    a = [i.split(" ") for i in file]

#challenge 1
def logic1(a):
    x,y=0,0
    for i in a:
        if i[0]=="forward":
            x+=int(i[1])
        elif i[0] =="down":
            y+=int(i[1])
        else:
            y-=int(i[1])
    return x*y

#challenge 2     
def logic2(a):
    x,y,b=0,0,0
    for i in a:
        if i[0]=="forward":
            x+=int(i[1])
            y+=b*int(i[1])
        elif i[0] =="down":
            b+=int(i[1])
        else:
            b-=int(i[1])
    return x*y

print(f"Challenge 1: {logic1(a)}\nChallenge 2: {logic2(a)}")    