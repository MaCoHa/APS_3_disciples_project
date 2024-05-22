N = int(input())
MAX = pow(10,9)+1

total_delegates = 0
possible_states = []

for _ in range(N):
    d, c_votes, f_votes, u_votes = map(int, input().split())
    total_delegates += d
    
    needed_votes = max((c_votes+f_votes+u_votes)//2 - c_votes + 1, 0)
    possible_states.append((needed_votes, d, u_votes))

needed_delegates = total_delegates//2+1
opt = [[MAX for _ in range(0, needed_delegates+1)] for _ in range(N)]
for i in range(0, N):
    needed_votes, delegates, undicided_votes = possible_states[i]
    for j in range(0, needed_delegates+1):
        if j == 0:
            opt[i][j] = 0
        elif i == 0:
            if delegates >= j and needed_votes <= undicided_votes:
                opt[i][j] = needed_votes
        elif needed_votes > undicided_votes:
            opt[i][j] = opt[i-1][j]
        else:
            take = needed_votes + opt[i-1][j-delegates] if delegates < j else needed_votes
            ignore = opt[i-1][j]
            
            opt[i][j] = min(take, ignore)
            
min_votes = opt[N-1][needed_delegates]

if min_votes >= MAX:
    print("impossible")
else:
    print(min_votes)