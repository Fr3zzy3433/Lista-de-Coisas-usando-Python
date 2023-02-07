import os

lista_compras = ['maçã']




while True:
    selecao = input('[L]listar \n[A]Adicionar \n[D] Deletar: \n').lower()

    if len(selecao) >1:
        print('Selecione apenas uma ação')
        continue
    
    elif selecao not in 'lad':
        print('Selecione uma ação válida')
        continue

    else:
        if selecao == 'l':
            os.system('cls')
            print('Sua Lista contem os seguintes itens:')
            for i, valor in enumerate(lista_compras):
                print(i, valor)
                
            print('O que deseja fazer agora?')
            continue
        
        elif selecao == 'a':
            os.system('cls')
            adicionar = input('Adicione seu item: ')
            lista_compras.append(adicionar)
            print('Seu item foi adicionado!')
            print('O que deseja fazer agora?')
            

        elif selecao == 'd':
            os.system('cls')
            try:
                print('Sua lista contém: ')
                for i, valor in enumerate(lista_compras):
                    print(i, valor)
                indice_lista = input('Digite o indice que deseja apagar: ')
                indice = int(indice_lista)
                del lista_compras[indice]
                
            
            except ValueError:
                print('Digite numeros int. apenas')

            except IndexError:
                print('Não foi possivel apagar esse número.')
                