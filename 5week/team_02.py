def grader(student,answer):
    
    print(student)
    
    name = list()
    num = list()
    for k in range(0,5):
        n,m = student[k].split(',')
        name.append(n)
        num.append(m)
        num[k] = list(num[k])

    grade = list()
    for i in range(0,5):
        count = 0
        for j in range(0,10):
            if answer[j] == num[i][j]:
                count = count + 10
        grade.append(count)
        
    final = list()
    for l in range(0,5):
        final.append(str(grade[l])+name[l])
    final.sort(reverse=True)

    for rank in range(0,5):
        print("학생:",final[rank][2:],"점수:",final[rank][:2],"점", str(rank+1)+"등")
        
    
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

a = [3,2,4,2,5,2,4,3,1,2]
a = list(map(str, a))
        
grader(s,a)