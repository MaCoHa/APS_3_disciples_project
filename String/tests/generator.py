import random
import string

N = 300000  # Change N to any positive integer value

def generate_long_string(length):
    return ''.join(random.choices(string.ascii_letters , k=length))

long_string = generate_long_string(N)


print(long_string)
print(N)

def generate_L_R(N):
    L = random.randint(0, N - 1)
    R = random.randint(L + 1, N)
    return L, R


for _ in range(N):
    L, R = generate_L_R(N)
    print(L, " " , R)