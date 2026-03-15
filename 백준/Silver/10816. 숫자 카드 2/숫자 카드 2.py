N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

# 딕셔너리로 A에 어떤숫자가 몇개있는지 한번 훑음
counts={}
for i in A:
     if i in counts:
            counts[i] += 1
     else:
        counts[i] = 1
r = []
for j in B:
    if j in counts:
        r.append(counts[j])
    else:
        r.append(0)
    
print(*r)