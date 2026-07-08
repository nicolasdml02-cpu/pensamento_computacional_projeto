# O projeto barbearia:
"""
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
"""

# isso é um comentario de linha única.
p1_nome = "corte"
p1_barbeiro = "Gustavo, Nicolas, felipe, victor"
p1_preco = 30.00
p1_validade = "7 dias"
p1_descricao = "o melhor corte da regiao."
p1_estoque = 10  # Inicializado para evitar erro na opção 3

p2_nome = "barba"
p2_barbeiro = "Gustavo, Nicolas, felipe, victor"
p2_preco = 20.00
p2_validade = "7 dias"
p2_descricao = "melhor barbearia da regiao."
p2_estoque = 10

p3_nome = "sombrancelha"
p3_barbeiro = "Gustavo, Nicolas, felipe, victor"
p3_preco = 7.00
p3_validade = "7 dias"
p3_descricao = "o melhor estilo."
p3_estoque = 10

p4_nome = "luzes"
p4_barbeiro = "Gustavo, Nicolas, felipe, victor"
p4_preco = 50.00
p4_validade = "1 mes"
p4_descricao = "o melhor estilo."
p4_estoque = 10

p5_nome = "alisamento"
p5_barbeiro = "Gustavo, Nicolas, felipe, victor"
p5_preco = 50.00
p5_validade = "1 mes"
p5_descricao = "o melhor estilo."
p5_estoque = 10

print('olá, mundo!')

# O primeiro bloco de menu foi removido/integrado diretamente no laço "while" 
# para evitar que o código ficasse repetitivo ou quebrasse antes de entrar no loop.

while True:
    print('\n' + '-' * 48 + '\n')
    print('bem-vindo sistema de agendamento da barbearia\n')
    print('1 - cadastrar serviço')
    print('2 - agendar corte')
    print('3 - ver trabalhos feitos / realizar venda')
    print('4 - nossa localização')
    print('5 - nosso contato')
    print('6 - sobre nós')
    print('7 - funcionamento')   
    print('8 - creditos')
    print('0 - sair do sistema')
    print('\n---------------------------------\n')

    opcao = input('digite a opção desejada: ')

    if opcao == '1':
        print('Cadastrando produtos...\n')

        # Se o nome estiver vazio, ele permite cadastrar
        if p1_nome == '':
            p1_nome = input('corte: ')
            p1_estoque = int(input('gustavo, victor, nicolas, felipe (quantidade): '))
            p1_preco = float(input('30.00: '))
            p1_validade = input('7 dias: ')
            p1_descricao = input('o melhor corte da regiao: ')
            print(f'\n📦 Produto "{p1_nome}" cadastrado na vaga 1!')

        elif p2_nome == '':
            p2_nome = input('barba: ')
            p2_estoque = int(input('gustavo, victor, nicolas, felipe (quantidade): '))
            p2_preco = float(input('20.00: '))
            p2_validade = input('7 dias: ')
            p2_descricao = input('a melhor barbearia da regiao: ')
            print(f'\n📦 Produto "{p2_nome}" cadastrado na vaga 2!')

        elif p3_nome == '':
            p3_nome = input('sombrancelha: ')
            p3_estoque = int(input('gustavo, victor, felipe, nicolas (quantidade): '))
            p3_preco = float(input('7.00: '))
            p3_validade = input('7 dias: ')
            p3_descricao = input('o melhor estilo: ')
            print(f'\n📦 Produto "{p3_nome}" cadastrado na vaga 3!')

        elif p4_nome == '':
            p4_nome = input('luzes: ')
            p4_estoque = int(input('gustavo, victor, felipe, nicolas (quantidade): '))
            p4_preco = float(input('50.00: '))
