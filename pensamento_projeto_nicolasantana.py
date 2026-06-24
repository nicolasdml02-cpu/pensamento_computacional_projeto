'''
um bloco de comentarios.
projeto barbearia:

>PO (Como dono do projeto: quero um sistema para agendar serviços para a barbearia) 

>QA (como cliente:quero um sistema para agendar serviços para a barbearia
 para que eu possa agendar um horario com mais facilidade)

 >tech (como programador:quero um sistema para agendar serviços para a barbearia,
 para  que eu possa desenvolver um software eficiente e funcional)

 >dev (como programador:quero um sistema para agendar serviços para a barbearia,
 para que eu possa implementaras funcionalidades necessárias para meus clientes )
 
 >UX (como designer de experiência do usuário: quero um sistema para agendar serviços para minha barbearia,
 para que eu possa criar uma interface intuitiva,
  confortável e agradável para os usuários, garantindo uma experiência de agendamento fácil.)

>IA (Como analista de dados: Quero um sistema de agendamento para minha barbearia,
 para que possa coletar e analisar os dados de agendamneto, ajudando a indentificar padroes de estilos e otimizar
 as estrategias de marketing.)

'''

# isso é um comentario de linha única.
print('olá, mundo!')

print('_' * 48 + '\n')
print('Bem vindo ao sistema de agendamento da barbearia\n')
print('1 - cadastrar serviço')
print('2 - agendar corte')
print('3 - ver trabalhos feitos')
print('4 - nossa localização')
print('5 - nosso contato')
print('6 - sobre nos')
print('7 - funcionamento')
print('8 - creditos')
print('0 - sair do sistema')
print('\n---------------------------\n')

opcao__definida = int(input('digite a opçao desejda:'))

if opcao__definida == 1:
    print('opcao 1 - cadastrar serviço')

elif opcao__definida == 2:
    print('opcao 2 - agendar corte')

elif opcao__definida == 3:
    print('opcao 3 - ver trabalhos feitos')

elif opcao__definida == 4:
    print('opcao 4 - nossa localização')

elif opcao__definida == 5:
    print('opcao 5 - nosso contato')

elif opcao__definida == 6:
    print('opcao 6 - sobre nos')

elif opcao__definida == 7: 
    print('opcao 7 _ funcionamento')

elif opcao__definida == 8:
    print('opcao 8 - creditos')

else:
    print('opcao invalida')

while True:
    print('-' * 48 + '\n')
    print('bem-vindo sistema de agendamento da barbearia\n')
    print('1 - cadastrar serviço')
    print('2- agendar serviço')
    print('3- ver trabalhos feitos')
    print('4- nossa localização')
    print('5- nosso contato')
    print('6- sobre nós')
    print('7- funcionamento')
    print('8- creditos')
    print('0- sair do sistema')
    print('\n---------------------------------\n')

    if opcao__definida == '1':
        print('Cadastrando serviços...\n')

    # faça a lógica para cadastrar o produto aqui,
    # e somente a inserção dos dados usando input e os tipos de dados.

    if p1_nome == '':
        p1_nome = input('Corte: ')
        p1_barbeiros = int(input('Nicolas, gustavo, victor, felipe: '))
        p1_preco = float(input('30.00: '))
        p1_validade = input('7 dias: ')
        p1_descricao = input('à critério do cliente: ')
        print(f'\n📦 Produto "{p1_nome}" cadastrado na vaga 1!')

    elif p2_nome == '':
        p2_nome = input('Barba: ')
        p2_barbeiros = int(input('Nicolas, gustavo, victor, felipe: '))
        p2_preco = float(input('20.00: '))
        p2_validade = input('7 dias: ')
        p2_descricao = input('à critério do cliente: ')
        print(f'\n📦 Produto "{p2_nome}" cadastrado na vaga 2!')

    elif p3_nome == '':
        p3_nome = input('Sobrancelha: ')
        p3_barbeiros = int(input('Nicolas, gustavo, victor, felipe: '))
        p3_preco = float(input('15.00: '))
        p3_validade = input('7 dias: ')
        p3_descricao = input(': ')
        print(f'\n📦 Produto "{p3_nome}" cadastrado na vaga 3!')

    elif p4_nome == '':
        p4_nome = input('alisamento: ')
        p4_barbeiros = int(input('Nicolas, gustavo, victor, felipe: '))
        p4_preco = float(input('50.00: '))
        p4_validade = input('30 dias: ')
        p4_descricao = input('apicação do produto: ')
        print(f'\n📦 Produto "{p4_nome}" cadastrado na vaga 4!')        

    elif p5_nome == '':
        p5_nome = input('luzes: ')
        p5_barbeiros = int(input('Nicolas, gustavo, victor, felipe: '))
        p5_preco = float(input('75.00: '))
        p5_validade = input('30 dias: ')
        p5_descricao = input('apicação do produto: ')
        print(f'\n📦 Produto "{p5_nome}" cadastrado na vaga 5!')    

    else:
        print('❌ Sistema cheio! Limite de 5 produtos atingido.')

    
    elif opcao == '2':
        print('Realizando venda...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "" and p4_nome == "" and p5_nome == "":
            print(f'Não há serviços cadastrados para realizar vendas.')
        else:
            nome_venda = input('Digite o nome do serviço que deseja vender: ')

            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '(p1_nome)' deseja vender? "))
                if qtd_venda <= p1_barbeiros:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f' Estoque insuficiente! Temos apenas {p1_estoque}.')
