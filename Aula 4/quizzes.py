# Quizzes

q1 = 5
q2 = 2
q3 = 10
q4 = 10
q5 = 5

def nota_quizzes(q1,q2,q3,q4,q5):
    if q1 < 0 or q2 < 0 or q3 < 0 or q4 < 0 or q5 < 0 or q1 > 10 or q2 > 10 or q3 > 10 or q4 > 10 or q5 > 10:
        return 0
    else:
        media = (q1+q2+q3+q4+q5-(min(q1,q2,q3,q4,q5)))/4
        return media

media = nota_quizzes(q1,q2,q3,q4,q5)
print(media)