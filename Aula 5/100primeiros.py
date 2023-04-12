# 100primeiros
a = 1
soma = 0

while True:
    if a == 100:
        break
    else:
        b = 1/(2**a)
        a = a + 1
        soma += b
result = 1 + soma
print(result)