#Estrutura de dados em dicionario
#Criando dicionario dentro de dicionario{} para estruturar os valores
#variavel AGENDA vai ser global

AGENDA = {}

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

def mostrar_contatos(contato = ''):
    for contato in AGENDA:
        #vai chamar a funcao buscar contato passando o for, no qual vai printar todos os contato da agenda
        buscar_contato(contato)
        print('##################################')


def buscar_contato(contato_procurado):
    try:
        print('Nome:', contato_procurado)
        print('Celular:', AGENDA[contato_procurado]['celular'])
        print('Email:', AGENDA[contato_procurado]['email'])
        print('Endereço:', AGENDA[contato_procurado]['endereco'])
    except:
        print('Contato não encontrado')

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
    AGENDA.pop(nome)
    print('>>>>>> {} removido com sucesso'.format(nome))
