total = int(input())
things = int(input())

cost = 0
for i in range(things):
    product, price = map(int, input().split())
    cost += product * price
    
if total == cost:
    print('Yes')
else:
    print('No')