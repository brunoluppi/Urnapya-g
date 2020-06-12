import time
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
                print('voto computado')
                break
            if confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue

    if voto == 2:
        print('Voto na chapa 002')
        print('')
        print('| Presidente: Roger |')
        print('| Vice: João        |')
        print('')
        
        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                print('voto computado')
                break
            if confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue


    if voto == 3:
        print('Voto na chapa 003')
        print('')
        print('| Presidente: Cosmo |')
        print('| Vice: Wanda       |')
        print('')

        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                print('voto computado')
                break
            if confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue
    if voto == 0:
        print('Voto em Branco')
        while True:
            confirma = input('Confima voto? S OU N: ')
            if confirma == 's':
                print('voto computado')
                break
            if confirma == 'n':
                print('voto descartado')
                break
            else:
                print('entrada invalida, utilize apenas S para sim ou N para não')
                continue

    nvoto = input('Deseja realizar uma nova operação? S/N: ')

    if nvoto == 's':
        print('Novo voto')
        continue
    if nvoto == 'n':
        print('sessão encerrada')
        break



