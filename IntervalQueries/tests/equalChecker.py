

x = input()

def loadFileInArray(s:str):
    file = open(s, "r")
    s = file.read()
    file.close()
    alst = s.split()
    return alst


ans_ = loadFileInArray(x+".ans")
#ans_.reverse()
cal_ = loadFileInArray(x+".cal")
#cal_.reverse

file1 = open(x+".dif", "w")
print(f"Length of solvers answers: {len(ans_)}")
print(f"Length of solutions answers: {len(cal_)}")
diffs = 0
for x in range(len(ans_)):
    if ans_[x] != cal_[x]:
        diffs += 1
        file1.write(f"{x+1}, {ans_[x]}, {cal_[x]}\n")
file1.close
print(f"There are {diffs} differences in answers")