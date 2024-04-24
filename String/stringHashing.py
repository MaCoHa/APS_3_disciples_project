

text = input()




n = int(input())
prime = 2**19 - 1 
a = 26 
hash_lst = [ord(text[0])] * (len(text)) 
prefix_lst = [1] * (len(text))

for i in range(1,len(text)):
    print(hash_lst)
    
    hash_lst[i] =  (hash_lst[i-1] * a + ord(text[i])) % prime
    prefix_lst[i] = (prefix_lst[i-1]*a) % prime
    
print(hash_lst)
print(prefix_lst)


for i in range(n):
    L,R = map(int, input().split())
    hash_val = 0
    if L == 0:
        hash_val = hash_lst[R]
    else:
        hash_val = (hash_lst[R]-hash_lst[L-1]*prefix_lst[R-L+1]) % prime
    print(hash_val)