#Estrutura de dados em dicionario
#Criando dicionario dentro de dicionario{} para estruturar os valores
#variavel AGENDA vai ser global


AGENDA = {
    'leo': {
        'celular': '449987-5210',
        'email': 'leonardo@email.com',
        'endereco': 'Rua X'
    },
    'ana': {
        'celular': '449956-4520',
        'email': 'ana@email.com',
        'endereco': 'Rua Y'
    },
    'joao': {
        'celular': '449958-6310',
        'email':'joao@email.com',
        'endereco': None
    }
}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            #vai chamar a funcao buscar contato passando o for, no qual vai printar todos os contato da agenda
            buscar_contato(contato)
            print('##################################')
    else:
        print('Agenda vazia')


def buscar_contato(contato_procurado):
    try:
        print('Nome:', contato_procurado)
        print('Celular:', AGENDA[contato_procurado]['celular'])
        print('Email:', AGENDA[contato_procurado]['email'])
        print('Endereço:', AGENDA[contato_procurado]['endereco'])
    except KeyError:
            print('Contato inexistente')
    except Exception as erro:
            print('Um erro inesperado ocorreu')
            print(erro)

def incluir_contato(nome, celular, email, endereco):
    AGENDA[nome] = {'celular': celular,
                    'email': email,
                    'endereco': endereco,
    }
    print('>>>>>>Contato {} adicionado com sucesso'.format(nome))


def editar_contato(nome, campo, novo_valor):
    AGENDA[nome][campo] = novo_valor
    print('>>>>>> {} de {} alterado com sucesso'.format(campo, nome))

def excluir_contato(nome):
    try:
        AGENDA.pop(nome)
        print('>>>>>> {} removido com sucesso'.format(nome))
    except KeyError:
        print('Contato inexistente')
    except Exception as erro:
        print('Um erro inesperado ocorreu')
        print(erro)
def exportar_contato():
    try:
        with open('agenda.csv', 'w') as arquivo:
            #especificando itens na primeira linha
            arquivo.write('nome, celular, email, endereco\n')
            for contato in AGENDA:
                celular = AGENDA[contato]['celular']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato, celular, email, endereco))
        print('>>>>>>Arquivo exportado com sucesso')
    except Exception as erro:
        print('>>>>>>Algum erro ocorreu durante a exportação')
        print(erro)
def mostrar_menu():
    print('##############################')
    print('0 - Fechar agenda')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Adicionar contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para .CSV')
    print('##############################')

def selecao_menu(opcao):
    # mostrando todos contatos
    if opcao == '1':
        mostrar_contatos()
    # buscando contato
    elif opcao == '2':
        proc = input('Digite o nome do contato: ')
        buscar_contato(proc)
    # adicionando contato
    elif opcao == '3':
        nome = input('Nome: ')
        celular = input('Celular: ')
        email = input('Email: ')
        endereco = input('Endereço: ')
        incluir_contato(nome, celular, email, endereco)
    # editando contato
    elif opcao == '4':
        try:
            nome = input('Nome do contato: ')
            AGENDA[nome]
            print('>>>>>> Editando contato: {}'.format(nome))
            campo = input('Campo a ser alterado: [celular], [email], [endereço]: ')
            valor = input('Novo valor: ')
            editar_contato(nome, campo, valor)
        except:
            print('Contato não existe')
    # excluindo contato
    elif opcao == '5':
        nome = input('Nome: ')
        excluir_contato(nome)
    #exportando contatos
    elif opcao == '6':
        exportar_contato()
    else:
        print('Opção inválida')

opcao = None
while(opcao != '0'):
    mostrar_menu()
    opcao = input('Escolha uma opção: ')
    selecao_menu(opcao)

