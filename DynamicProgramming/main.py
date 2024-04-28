import math
N = int(input())
MAX = pow(10,9)

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
    if possible_win:
        TOTAL_POSSIBLE_C_DELEGATES += d
        possible_states.append((needed_votes, d))
    else:
        N -= 1
if TOTAL_POSSIBLE_C_DELEGATES <= (TOTAL_DELEGATES//2):
    print("impossible")
else:
    possible_states.sort(key=lambda s : s[0]/(s[1]+1))
    needed_delegates = TOTAL_DELEGATES//2+1
    opt = [[MAX for _ in range(0, TOTAL_POSSIBLE_C_DELEGATES+1)] for _ in range(N)]
    for i in range(0, N):
        needed_votes, delegates = possible_states[i]
        #print(possible_states[i])
        for j in range(0, TOTAL_POSSIBLE_C_DELEGATES+1):
            if j == 0:
                opt[i][j] = 0
            elif i == 0:
                if delegates >= j:
                    opt[i][j] = needed_votes
                else:
                    opt[i][j] = MAX
            else:
                if delegates >= j:
                     opt[i][j] = min(needed_votes, opt[i-1][j])
                else:
                    opt[i][j] = min(needed_votes+opt[i-1][j-delegates], opt[i-1][j])

    #for l in opt:
    #    print(l)
    #print(opt)
    print(opt[N-1][needed_delegates])


