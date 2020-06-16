ficha = []
while True:
    nome = str(input("Insira um nome: "))
    sexo = str(input("Insira seu sexo [M/F]: "))

    nota1 = float(input("Insira a nota 1: "))
    while nota1 < 0 or nota1 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota1 = float(input("Insira a nota 1: "))

    nota2 = float(input("Insira a nota 2: "))
    while nota2 < 0 or nota2 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota2 = float(input("Insira a nota 2: "))

    nota3 = float(input("Insira a nota 3: "))
    while nota3 < 0 or nota3 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota3 = float(input("Insira a nota 3: "))

    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        status = "Aprovado"
    elif media < 7 and media >= 4:
        status = "Exame"
    else:
        status = "Reprovado"

    ficha.append([nome, sexo, [nota1, nota2, nota3], media, status])

    resposta = str(input("Quer continuar? [S/N]"))
    if resposta in 'Nn':
        break

tx_reprovados = 0
tx_exame = 0
tx_aprovado = 0

m_aprovado = 0
f_aprovado = 0
m_exame = 0
f_exame = 0
m_reprovado = 0
f_reprovado = 0

for i in range(0, len(ficha), 1):
    if ficha[i][4] == "Reprovado":
        tx_reprovados += 1
        if ficha[i][1] in 'Ff':
            f_reprovado += 1
        else:
            m_reprovado += 1

    elif ficha[i][4] == "Exame":
        tx_exame += 1
        if ficha[i][1] in 'Ff':
            f_exame += 1
        else:
            m_exame += 1

    elif ficha[i][4] == "Aprovado":
        tx_aprovado += 1
        if ficha[i][1] in 'Ff':
            f_aprovado += 1
        else:
            m_aprovado += 1


print("Taxas de status: ")
print(f'Alunos aprovados: {(tx_aprovado/len(ficha))*100}%')
print(f'Alunos para exame: {(tx_exame/len(ficha))*100}%')
print(f'Alunos reprovados: {(tx_reprovados/len(ficha))*100}%')

print('-' * 45)

print('Visualizacao por sexo:')
print(f'Alunas aprovadas: {f_aprovado}')
print(f'Alunas para exame: {f_exame}')
print(f'Alunas reprovadas: {f_reprovado}')

print('')

print(f'Alunos aprovados: {m_aprovado}')
print(f'Alunos para exame: {m_exame}')
print(f'Alunos reprovados: {m_reprovado}')
