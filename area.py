import math
a=float(input())
b=float(input())
c=float(input())
if a+b>c and b+c>a and a+c>b:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("Invalid Triangle")
