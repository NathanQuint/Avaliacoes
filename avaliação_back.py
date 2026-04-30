#Condições especiais
    # Aprovado: Média >= 7.0
    # Recuperação: Média >= 5.0 e < 7.0
    # Reprovado: Média < 5.0

#Variaveis

nome_lista = []
nota_1_lista = []
nota_2_lista = []
nota_3_lista = []
media_lista = []
resultado_lista = []


#Condicionais
while True:
    print ("Olá Professor!👋 Bem vindo ao Cadastro de alunos! ")    
    escolha = input('''            
            [1] - Cadastrar Aluno
            [2] - Ver boletim da turma
            [3] - Sair
                    
Digite uma das opções acima ⬆️  ! ''')

    if escolha == "3":
        print("Desligando sistema... ")
        break

    elif escolha == "1":

        qnt_alunos = int(input("Quantos alunos deseja Cadastrar? "))
    
        for i in range (qnt_alunos):
                
                nome_aluno = input("Qual o nome do Aluno? ")
                    
                nota_1 = float(input("Qual foi a nota (de 0 a 10) da primeira prova feita por esse aluno?  ").replace(",", "."))
                nota_2 = float(input("Qual foi a nota (de 0 a 10) da segunda prova feita por esse aluno? ").replace(",", "."))
                nota_3 = float(input("Qual foi a nota (de 0 a 10) da terceira prova feita por esse aluno? ").replace(",", "."))
                media = (nota_1 + nota_2 + nota_3) / 3

                if media >= 7:
                        resultado = "✅ Aprovado ✅ "     
                    
                elif media >= 5:
                        resultado = "⏳ Recuperação ⏳ "
                    
                else:
                        resultado = "❌ Reprovado ❌ "
                    
                    
                nome_lista.append (nome_aluno) 
                nota_1_lista.append (nota_1)
                nota_2_lista.append (nota_2)
                nota_3_lista.append (nota_3)
                media_lista.append (f"{media: .2f}")
                resultado_lista.append (resultado)
                    
                print (f"{nome_aluno} cadastrado(a) com sucesso!!")
    
    else:
        for aluno in range (len(nome_lista)):
            print (f'''Aluno: {nome_lista[aluno]}
                    Primeira nota: {nota_1_lista[aluno]}
                    Segunda nota: {nota_2_lista[aluno]}
                    Terceira nota: {nota_3_lista[aluno]}
                    Média: {media_lista[aluno]}
                    Situação: {resultado_lista[aluno]}
                    ----------------------------''')