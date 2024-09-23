n = int(input())
stores = list(map(int, input().split()))
a, b = map(int, input().split())
total = 0

for store in stores :
    store-=a
    total+=1
    if store>0 :
        total+=(store-1)//b+1
print(total)
