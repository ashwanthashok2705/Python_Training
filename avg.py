n=int(input())
numbers=[int(input()) for _ in range(n)]
average=sum(numbers)/n
print(f"The average is: {average:.2f}")
