# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa 

# Seu programa deverá realizar a operação solicitada em cada caso

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while n1 != 0:

    print('\n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa') 
    opcao = int(input('>>>>>> Sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('-'*25)
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
        print('-'*25)

    elif opcao == 2:
        mult = n1 * n2
        print('-'*25)
        print('A soma entre {} x {} = {}'.format(n1, n2, mult))
        print('-'*25)
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('-'*25)
            print('Entre {} e {}, maior número é {}'.format(n1, n2, maior))
            print('-'*25)
        else: 
            maior = n2
            print('-'*25)
            print('Entre {} e {}, maior número é {}'.format(n1, n2, maior))
            print('-'*25)
            
    elif opcao == 4:
        n1 = int(input('\nDigite novamente o primeiro valor: '))
        n2 = int(input('\nDigite novamente o segundo valor: '))
    
    elif opcao == 5:
        n1 = 0
    
    else:
        print('\nOpção inválida')
        
            
