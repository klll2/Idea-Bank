sem = int(input('이수한 학기 수를 입력하시오 :'))
semi = 0
d = {}
d2 = {}
d3 = {}
for _ in range(sem):
    semi += 1
    d[semi] = {}
    lecs = int(input(str(semi)+'학기 수강 강의 수를 입력하시오 :'))
    for _ in range(lecs):
        lec = list(input('강의 정보를 입력하시오'+'('+'이름/1,2전공or교양/학점/성적'+') :').split('/'))
        d[semi][lec[0]] = lec[1:4]
    score1 = 0
    score2 = 0
    m1 = 0
    m2 = 0
    c = 0
    l1 = list(d[semi].keys())
    for i in l1:
        score1 += int(d[semi][i][1])*float(d[semi][i][2])
        score2 += int(d[semi][i][1])
        if d[semi][i][0] == '1전공':
            m1 += int(d[semi][i][1])
        elif d[semi][i][0] == '2전공':
            m2 += int(d[semi][i][1])
        else:
            c += int(d[semi][i][1])
    d3[semi] = [m1,m2,c]
    score = score1/score2
    d2[semi] = [score1,score2]
tscore1 = 0
tscore2 = 0
tm1 = 0
tm2 = 0
tc = 1
l2 = list(d2.keys())
for i in l2:
    tscore1 += d2[i][0]
    tscore2 += d2[i][1]
    tm1 += d3[i][0]
    tm2 += d3[i][1]
    tc += d3[i][2]
tscore = tscore1/tscore2

x = 0
while x == 0:
    x = int(input('1. 당해 학기 정보, 2. 총 이수 학기 정보, 3. 목표 학점 계산, 4. 종료'))
    if x == 1:
        y = int(input('원하는 학기를 입력하시오 :'))
        print(str(y)+'학기 '+'평균 학점 : '+str(d2[y][0]/d2[y][1])+', '+str(y)+'학기 '+'이수 학점 : '+'1전공 : '+str(d3[y][0])+'학점, '+'2전공 : '+str(d3[y][1])+'학점, '+'교양 : '+str(d3[y][2])+'학점')
        x = 0
    elif x == 2:
        print('총 평균 학점 : '+str(tscore)+', '+'총 이수 학점 : '+'1전공 : '+str(tm1)+'/54'+', 2전공 : '+str(tm2)+'/42'+', 교양 : '+str(tc)+'/32')
        x = 0
    elif x == 3:
        z1 = float(input('목표 평균 학점을 입력하시오 :'))
        z2 = int(input('목표 기간 동안 취득할 학점 수를 입력하시오 :'))
        z3 = (z1*(tscore2+z2) - tscore1)/z2
        print('귀하가 목표 평균 학점을 달성하기 위해 목표 기간 동안 취득해야 할 평균 학점은 :'+str(z3)+'점입니다.')
    else:
        print('이용해주셔서 감사합니다.')
        x = 4