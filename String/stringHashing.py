text = input()

n = int(input())

h = [0] * (len(text))
p = [0] * (len(text))

h[0] = ord(text[0])
p[0] = 1


A = 911382323
B = 2**63 - 1

for i in range(1,len(text)):    
    h[i] = (h[i-1]*A + ord(text[i])) % B
    p[i] = (p[i-1]*A) % B
    


for i in range(n):
    a,b = map(int, input().split())
    b -= 1
    if a == 0:
        print(h[b])
    else:
        print((h[b]-h[a-1]*p[b-a+1]) % B)
        
    
 