import sys 

n = int(input("Enter number of student btn 2 & 10 : "))

student_marks = {}

if n < 2 or n >10:
    print("Invalid number,Please Enter number btn 2 and 10 ")
else:
    for r in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))

        if len(scores) > 3:
            print("Please Enter Marks not greater than 3")
            sys.exit()
        elif len(scores) < 3:
            print("Please Enter marks not less than 3")
            sys.exit()
        else:
            for q in scores:
                if float(q) > 100 or float(q) < 0:
                    print("invalid marks, Marks must be between 0 and 100.")
                    sys.exit()
                else:
                    student_marks[name] = scores
                
    query_name = input()
    marks=0
    for i in student_marks[query_name]:
        marks=marks+i
    Average=marks/3
    print("%.2f"%Average)
