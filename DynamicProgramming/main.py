N = int(input())
MAX = pow(10,9)+1

TOTAL_DELEGATES = 0
TOTAL_POSSIBLE_C_DELEGATES = 0

possible_states = []

for _ in range(N):
    d, c_votes, f_votes, u_votes = map(int, input().split())
    TOTAL_DELEGATES += d
    possible_win = False
    needed_votes = 0
    # Check if it is possible for c to win the majority. A tie means f wins.
    needed_votes = (c_votes+f_votes+u_votes)//2 - c_votes + 1
    possible_win = c_votes + u_votes > f_votes
    possible_states.append((needed_votes, d, u_votes))
    TOTAL_POSSIBLE_C_DELEGATES += d
    #if possible_win:
    #else:
    #    N -= 1
if TOTAL_POSSIBLE_C_DELEGATES <= (TOTAL_DELEGATES//2):
    print("impossible")
else:
    #possible_states.sort(key=lambda s : s[0]/(s[1]+1))
    needed_delegates = TOTAL_DELEGATES//2+1
    opt = [[MAX for _ in range(0, needed_delegates+1)] for _ in range(N)]
    for i in range(0, N):
        needed_votes, delegates, undicided_votes = possible_states[i]
        #print(possible_states[i])
        if needed_votes < 0:
            needed_votes = 0
        for j in range(0, needed_delegates+1):
            
            if j == 0:
                opt[i][j] = 0
            elif i == 0:
                if delegates >= j and needed_votes <= undicided_votes:
                    opt[i][j] = needed_votes
            elif needed_votes > undicided_votes:
                opt[i][j] = opt[i-1][j]
            else:
                if delegates >= j:
                    opt[i][j] = min(needed_votes, opt[i-1][j])
                else:
                    opt[i][j] = min(needed_votes + opt[i-1][j-delegates], opt[i-1][j])
            
    #for l in opt:
    #   print(l)
    
    min_votes = opt[N-1][needed_delegates]
    #print(min_votes)
    if min_votes >= MAX:
        print("impossible")
    else:
        print(min_votes)