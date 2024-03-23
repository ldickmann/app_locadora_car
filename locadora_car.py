class Cliente:
    def __init__(self, nome, cpf, idade, data_nascimento, num_carteira_motorista, ano_vencimento_carteira_motorista, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.num_carteira_motorista = num_carteira_motorista
        self.ano_vencimento_carteira_motorista = ano_vencimento_carteira_motorista
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

class Clientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente_nome(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                return cliente
        return None

cliente1 = Cliente('João', '202.123.565-54', 65, '25/10/1958', 253659326, '20/05/2025', 'Rua Dr. Blumenau, 65', '47 988953625', 'joãoernesto@gmail.com')
cliente2 = Cliente('Maria', '302.657.982-15', 45, '12/03/1978', 326618935, '30/08/2024', 'Rua Tamandaré, 215', '48 999326515', 'mariagenoveva@gmail.com')
cliente3 = Cliente('Guilherme', '326.256.258-56', 22, '29/10/2000', 326598745, '03/03/2023', 'Rua Pedro Nestor Neto, 200', '47 988963520','guiperto@gmail.com ')


class Funcionario:
    def __init__(self, nome, cpf, idade, endereco, data_contratacao, salario, qtd_alugueis_realizados, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.data_contratacao = data_contratacao
        self.salario = salario
        self.qtd_alugueis_realizados = qtd_alugueis_realizados
        self.telefone = telefone
        self.status = True

func1 = Funcionario('Miguel', '258.326.285-56', 35, 'Rua  Miguel José, 325', '16/08/2017', 'R$2.700,00', '9', '47 988569230')
func1.status = False
func2 = Funcionario('Luana', '203.268.268-69', 40, 'Rua Joana Silva, 1230', '01/02/2019', 'R$2.300,00', '7', '47 989896253')

class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao

class Esportivo(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, tempo_para_100km_por_hora, melhorias):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.tempo_para_100km_por_hora = tempo_para_100km_por_hora
        self.melhorias = melhorias

carro_esportivo1 = Esportivo('GHI9012', 2019, 'Branco', 'Camaro', 25000, 'R$300,00', 'Carro impecavél', 5.5, ['Rodas de liga-leve', 'Sistema de som premium'])

class Utilitario(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, qtde_passageiros, tamanho_bagageiro, km_por_litro_gasolina):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.qtde_passageiros = qtde_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_por_litro_gasolina = km_por_litro_gasolina

carro_utilit1 = Utilitario("JKL3456", 2021, "Prata", "Hilux", 10000, 'R$250,00', 'Trincado no parabrisa', 5, 'Médio', 10.5)
carro_utilit2 = Utilitario('KLB2363', 2022, 'Preto', 'Toro', 18000, 'R$300,00', 'Sem obeservação', 5, 'Médio', 12.5)

class Reserva:
    def __init__(self, carro, cliente, codigo, status, data_inicio, data_fim):
        self.carro = carro
        self.cliente = cliente
        self.codigo = codigo
        self.status = status
        self.data_inicio = data_inicio
        self.data_fim = data_fim

reserva1 = Reserva(carro_utilit1, cliente1, '001', 'Ativa', '22/03/2023', '23/05/2023')
reserva2 = Reserva(carro_esportivo1, cliente2, '002', 'Ativa', '15/03/2023', '30/04/2023')

class Promocao:
    def __init__(self, titulo, descricao, data_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_validade = data_validade
        
promocao1 = Promocao('10% em um mes', 'Se alugar um carro nosso por um mês ganhe 10% de desconto', '05/06/2023')

carros = [carro_esportivo1, carro_utilit1, carro_utilit2]

reservas = [reserva1, reserva2]

print('Bem-vindo(a) ao sistema de aluguel de carros!\n')


clientes = Clientes()

while True:
    opcao = input('Escolha uma opção:\n1. Realizar reserva\n2. Cancelar reserva\n3. Consultar reservas\n4. Sair\n')

    if opcao == '1':
        for i, carro in enumerate(carros):
            print(f'{i} - {carro.modelo} \n')
        carro_escolhido = int(input('Qual carro é do seu interesse? '))
        if 0 <= carro_escolhido < len(carros):
            cliente_escolhido = input('Qual seu nome? ')
            cliente_existente = clientes.buscar_cliente_nome(cliente_escolhido)
            if not cliente_existente:
                # Cadastro de novo cliente
                cpf_novo_cliente = input('Digite o seu CPF: ')
                idade_novo_cliente = int(input('Qual a sua idade? '))
                data_nascimento = input('Qual a sua data de nascimento? ')
                num_carteira_motorista = int(input('Qual o número da sua CNH? '))
                ano_vencimento_carteira_motorista = int(input('Qual o ano de vencimento da sua CNH? '))
                endereco = str(input('Qual a rua que você reside ? '))
                telefone = int(input('Qual seu número de celular? '))
                email = input('Informe seu email: ')
                novo_cliente = Cliente(cliente_escolhido, cpf_novo_cliente, idade_novo_cliente)
                clientes.adicionar_cliente(novo_cliente)
                print('Tu foi cadastrado com sucesso!')
            else:
                print('Cliente encontrado!')
            # Realiza a reserva
            data_inicio = input('Qual a data de reserva (dd/mm/aaaa): ')
            data_fim = input('Qual a data para a devolução do veículo (dd/mm/aaaa): ')
            codigo_reserva = input('Informe o código da reserva: ')
            nova_reserva = Reserva(carros[carro_escolhido], cliente_existente, codigo_reserva, 'Ativa', data_inicio, data_fim)
            reservas.append(nova_reserva)
            print('Reserva realizada com sucesso!')
        else:
            print('Opção inválida.')
    elif opcao == '2':
        print('Você escolheu cancelar uma reserva.\n')
    elif opcao == '3':
       for i, reserva in enumerate(reservas):
            print(f'{i} - {reserva.carro.modelo}, {reserva.data_inicio}, {reserva.data_fim} \n')
    elif opcao == '4':
        print('Obrigado por utilizar nosso sistema. Volte sempre!')
        break
    else:
        print('Opção inválida. Escolha uma opção válida.\n')
