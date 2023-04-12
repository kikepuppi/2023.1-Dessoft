# nota media da sala
quantosalunos = 0
soma = 0
a = 0
r = 0
while True:
    add = input('Quer adicionar mais um aluno?')
    if add != 'não':
        q1 = float(input('Quiz 1?'))
        q2 = float(input('Quiz 2?'))
        q3 = float(input('Quiz 3?'))
        q4 = float(input('Quiz 4?'))
        q5 = float(input('Quiz 5?'))
        ai = float(input('AI?'))
        af = float(input('AF?'))
        ep1 = float(input('EP1?'))
        ep2 = float(input('EP2?'))
        pf = float(input('PF?'))
        quantosalunos += 1
        Q = (q1+q2+q3+q4+q5-min(q1,q2,q3,q4,q5))/4
        NI = 0.4*ai + 0.5*af + 0.1*Q
        NG = 0.1*ep1 + 0.2*ep2 + 0.7*pf
        if NI >= 5 and NG >= 5:
            NF = (NI + NG)/2
        if NI < 5 or NG < 5:
            NF = min(NI,NG)
        soma += NF
        if NF >= 5:
            a += 1
        if NF < 5:
            r += 1
        print('Nota final do aluno: {0:.2f}'.format(NF))
    else:
        break
if quantosalunos == 0:
    mediasala = 0
    aprovados = 0
    reprovados = 0
else:
    mediasala = soma/quantosalunos
    aprovados = a*100/quantosalunos
    reprovados = r*100/quantosalunos
    
print('Média da sala: {0:.2f}'.format(mediasala))
print('Aprovados: {0:.2f}%'.format(aprovados))
print('Reprovados: {0:.2f}%'.format(reprovados))
        




