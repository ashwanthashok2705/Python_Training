inputstring=input()
outputstring=''
for i in inputstring:
    if i.isupper():
        o=i.lower()
    elif i.islower():
        o=i.upper()
    else:
        o=i
    outputstring += o
print(outputstring)
