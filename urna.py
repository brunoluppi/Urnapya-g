import time
c1 = 0
c2 = 0
c3 = 0
b = 0
n = 0
print('URNA ELETRONICA')
while True:
    senha = input('Digite a Senha: ')
    if senha == '1234':
        print('iniciando sistema')
        print('|', end="")
        time.sleep(0.5)
        print('|', end="")
        time.sleep(0.5)
        print('|', end="")
        time.sleep(0.5)
        print('|', end="")
        time.sleep(0.5)
        print('|')
        time.sleep(0.5)
        print('sistema iniciado')
        break
    else:
        print('senha invalida')
        continue
while True:
    print('===========================')    
    print('Candidatos: ')
    print('')
    print('CHAPA: 001')
    print('')
    print('| Presidente: Bob   |')
    print('| Vice: Patrick     |')
    print('')
    print('CHAPA: 002')
    print('')
    print('| Presidente: Roger |')
    print('| Vice: João        |')
    print('')
    print('CHAPA: 003')
    print('')
    print('| Presidente: Cosmo |')
    print('| Vice: Wanda       |')
    print('')
    print('===========================')
        
    voto = int(input('Digite o seu voto: '))

    if voto == 1:
        print('Voto na chapa 001')
        print('')
        print('| Presidente: Bob   |')
        print('| Vice: Patrick     |')
        print('')

        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                c1 = c1 + 1
                print('voto computado')
                break
            elif confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue

    elif voto == 2:
        print('Voto na chapa 002')
        print('')
        print('| Presidente: Roger |')
        print('| Vice: João        |')
        print('')
        
        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                c2 = c2 + 1
                print('voto computado')
                break
            elif confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue
            
    elif voto == 3:
        print('Voto na chapa 003')
        print('')
        print('| Presidente: Cosmo |')
        print('| Vice: Wanda       |')
        print('')

        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                c3 = c3 + 1
                print('voto computado')
                break
            elif confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue

    elif voto == 0:
        print('Voto em Branco')
        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                b = b + 1
                print('voto computado')
                break
            if confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue

    else:
        print('voto nulo')
        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                n = n + 1
                print('voto computado')
                break
            elif confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue
    
    nvoto = input('Deseja realizar uma nova operação? S/N: ')

    if nvoto == 's':
        print('Novo voto')
        continue
    elif nvoto == 'n':
        while True:
            print('Digite a senha para encerrar a seção')
            senha = input('Senha: ')
            if senha == '1234':
                break
            else:
                print('senha invalida')
                continue
                break
        break
print('Contando Votos ')
print('|', end="")
time.sleep(0.5)
print('|', end="")
time.sleep(0.5)
print('|', end="")
time.sleep(0.5)
print('|', end="")
time.sleep(0.5)
print('|')
time.sleep(0.5)
print('Contagem realizada: ')

total = c1 + c2 + c3 + b + n
totalc1 = (c1 / total) * 100
totalc2 = (c2 / total) * 100
totalc3 = (c3 / total) * 100
totalb = (b / total) * 100
totaln = (n / total) * 100

print('Total de votos: ', total)

print('Votos chapa 001: ', totalc1,'% | ',c1 ,'(votos)')

print('Votos chapa 002: ', totalc2,'% | ',c2 ,'(votos)')

print('Votos chapa 003: ', totalc3,'% | ',c3 ,'(votos)')

print('Votos Brancos: ', totalb,'% | ',b ,'(votos)')

print('Votos Nulos: ', totaln,'% | ',n ,'(votos)')

print ('')

if c1 > c2 and c1 > c3:
    print('| VITÓRIA CHAPA 001 |')
    print('| Presidente: Bob   |')
    print('| Vice: Patrick     |')

elif c2 > c1 and c2 > c3:
    print('| VITÓRIA CHAPA 002 |')
    print('| Presidente: Roger |')
    print('| Vice: João        |')

elif c3 > c1 and c3 > c2:
    print('| VITÓRIA CHAPA 003 |')
    print('| Presidente: Cosmo |')
    print('| Vice: Wanda       |')

print('Fim da seção')
