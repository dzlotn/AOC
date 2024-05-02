file = open("AOC1/input1.txt", "r")
sum=0
letters = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine": 9   
}

updatedSentence= []
for sent in file:
    for x in letters: 
        if x in sent:
            sent = sent.replace(x,str(letters[x]))
    print(f"Sentence Updated: {sent}")    
            
    tempArray = []
    listChar = [*sent]
    for i in listChar:
        if i.isdigit():
            tempArray.append(int(i))
    print(f"All Nums Found: {tempArray}")
    truncated = (tempArray[0]*10)+tempArray[-1]
    
    print(f"Truncated: {truncated}")
    # print(truncated)
    sum+=truncated
    print(f"Sum: {sum}")
print(sum)