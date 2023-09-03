souls, questions_count =  map(int,input().split())
teams = [[i] for i in range(souls+1)]
d ={}
for i in range(1,souls+1):
    d[i]=  1
questions = []

for  i in range(questions_count):
    question = list(map(int,input().split()))
    questions.append(question)
    # print(question, i)

for question in questions:
    if question[0] == 1:
        team1, team2 = -1, -1
        for idx, team in enumerate(teams):
            if question[1] in team:
                team1 = idx
            if question[2] in team:
                team2 = idx

            if team1 != -1 and team2 != -1:
                teams[team1]+= teams[team2]
                for soul in teams[team1]:
                    d[soul] += 1
                teams.pop(team2)
                break
    if question[0]==2:
        in_one =0
        for team in teams:
            if question[1] in team and  question[2] in team:
                print("YES")
                in_one = 1
                break
        if not in_one:
            print("NO")


    if question[0]==3:
        print(d[question[1]])

