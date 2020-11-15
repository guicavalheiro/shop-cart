class Pagamento:

    def __init__(self):
        self.pagamentos = {}
        
    def add_metodo(self, choice, nome, 
                   numero_cartao=False, validade=False, seguranca=False,
                   cpf=False, endereco=False, numero_casa=False, complemento=False):
        
        if choice == 1:
            return self.add_debito(nome, numero_cartao, validade, seguranca)
        
        elif choice == 2:
            return self.add_credito(nome, numero_cartao, validade, seguranca)
        
        elif choice == 3:
            return self.add_boleto(nome, cpf, endereco, numero_casa, complemento)
    
    def add_debito(self, nome, numero, validade, seguranca):
        self.pagamentos['Debito'] = {'Nome': nome, 'Numero do cartao': numero, 'Validade': validade, 'Seguranca': seguranca}
        return self.pagamentos['Debito']
    
    def add_credito(self, nome, numero, validade, seguranca):
        self.pagamentos['Credito'] = {'Nome': nome, 'Numero do cartao': numero, 'Validade': validade, 'Seguranca': seguranca}
        return self.pagamentos['Credito']
    
    def add_boleto(self, nome, cpf, endereco, numero_casa, complemento):
        data_emissao  = '16/11/2020'
        data_validade = '19/11/2020'
        self.pagamentos['Boleto'] = {'Nome': nome, 'CPF': cpf, 'Endereço': endereco, 'Numero da casa': numero_casa, 'Complemento': complemento, 'Data de Emissao': data_emissao, 'Data de vencimento': data_validade}
        return self.pagamentos['Boleto']
        