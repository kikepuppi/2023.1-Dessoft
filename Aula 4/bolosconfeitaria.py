# Bolos confeitaria AAAAA

t = input('Qual o tamanho do bolo? [XP, P, M, G, XG]')
o = float(input('Qual o orçamento?'))

if t == 'XP':
    bolos = o//5
    a = o % 5
    if a == 0:
        print ('sem acompanhamento')
    elif bolos <= 4:
        cheesecake = a // 2
        brownie = (a % 2)
        if cheesecake != 0:
            print ('{0:.0f} cheesecake'.format(cheesecake))
        if brownie != 0:
            print ('{0:.0f} brownie'.format(brownie))
    elif bolos > 4:
        cupcake = a // 2
        banoffe = (a % 2)
        if cupcake != 0:
            print ('{0:.0f} cupcake'.format(cupcake))
        if banoffe != 0:
            print ('{0:.0f} banoffee'.format(banoffe))


if t == 'P':
    bolos = o//7
    a = o % 7
    if a == 0:
        print ('sem acompanhamento')
    elif bolos <= 4:
        cheesecake = a // 2
        brownie = (a % 2)
        if cheesecake != 0:
            print ('{0:.0f} cheesecake'.format(cheesecake))
        if brownie != 0:
            print ('{0:.0f} brownie'.format(brownie))
    elif bolos > 4:
        cupcake = a // 2
        banoffe = (a % 2)
        if cupcake != 0:
            print ('{0:.0f} cupcake'.format(cupcake))
        if banoffe != 0:
            print ('{0:.0f} banoffee'.format(banoffe))

if t == 'M':
    bolos = o//20
    a = o % 20
    if a == 0:
        print ('sem acompanhamento')
    elif bolos <= 4:
        cheesecake = a // 2
        brownie = (a % 2)
        if cheesecake != 0:
            print ('{0:.0f} cheesecake'.format(cheesecake))
        if brownie != 0:
            print ('{0:.0f} brownie'.format(brownie))
    elif bolos > 4:
        cupcake = a // 2
        banoffe = (a % 2)
        if cupcake != 0:
            print ('{0:.0f} cupcake'.format(cupcake))
        if banoffe != 0:
            print ('{0:.0f} banoffee'.format(banoffe))

if t == 'G':
    bolos = o//31
    a = o % 31
    if a == 0:
        print ('sem acompanhamento')
    elif bolos <= 4:
        cheesecake = a // 2
        brownie = (a % 2)
        if cheesecake != 0:
            print ('{0:.0f} cheesecake'.format(cheesecake))
        if brownie != 0:
            print ('{0:.0f} brownie'.format(brownie))
    elif bolos > 4:
        cupcake = a // 2
        banoffe = (a % 2)
        if cupcake != 0:
            print ('{0:.0f} cupcake'.format(cupcake))
        if banoffe != 0:
            print ('{0:.0f} banoffee'.format(banoffe))

if t == 'XG':
    bolos = o//50
    a = o % 50
    if a == 0:
        print ('sem acompanhamento')
    elif bolos <= 4:
        cheesecake = a // 2
        brownie = (a % 2)
        if cheesecake != 0:
            print ('{0:.0f} cheesecake'.format(cheesecake))
        if brownie != 0:
            print ('{0:.0f} brownie'.format(brownie))
    elif bolos > 4:
        cupcake = a // 2
        banoffe = (a % 2)
        if cupcake != 0:
            print ('{0:.0f} cupcake'.format(cupcake))
        if banoffe != 0:
            print ('{0:.0f} banoffee'.format(banoffe))