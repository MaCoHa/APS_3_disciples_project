

def loadFileInArray(s:str):
    file = open(s, "r")
    s = file.read()
    file.close()
    alst = s.split()
    return alst


ans_ = loadFileInArray("3.ans")
cal_ = loadFileInArray("3.cal")

file1 = open("3.dif", "w")
for x in range(len(ans_)):
    if ans_[x] != cal_[x]:
        file1.write(f"{x+1}, {ans_[x]}, {cal_[x]}\n")
file1.close

ans2_ = loadFileInArray("4.ans")
cal2_ = loadFileInArray("4.cal")

file2 = open("4.dif", "w")
for x in range(len(ans2_)):
    if ans2_[x] != cal2_[x]:
        file2.write(f"{x+1}, {ans2_[x]}, {cal2_[x]}\n")
file2.close