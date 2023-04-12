# Valida CPF

n1 = int(input('qual o numero 1?'))
n2 = int(input('qual o numero 2?'))
n3 = int(input('qual o numero 3?'))
n4 = int(input('qual o numero 4?'))
n5 = int(input('qual o numero 5?'))
n6 = int(input('qual o numero 6?'))
n7 = int(input('qual o numero 7?'))
n8 = int(input('qual o numero 8?'))
n9 = int(input('qual o numero 9?'))
n10 = int(input('qual o numero 10?'))
n11 = int(input('qual o numero 11?'))


def valida_cpf(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11):
    if n1==n2==n3==n4==n5==n6==n7==n8==n9==n10==n11:
        return False

    else:
        a = ((n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2)*10)%11

        if a == 10:
            a = 0
        
        b = ((n1*11 + n2*10 + n3*9 + n4*8 + n5*7 + n6*6 + n7*5 + n8*4 + n9*3 + n10*2)*10)%11

        if b == 10:
            b = 0

        if n10 == a and n11 == b:
            return True
        else:
            return False
        
