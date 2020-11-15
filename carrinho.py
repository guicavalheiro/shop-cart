class Carrinho(object):
    
    __create_key = object()
    
    def __init__(self, create_key, value):
        assert(create_key == Carrinho.__create_key), \
            "Carrinho objects must be created using Carrinho.get_instance"
        
        self.value = value
        self.instancia = False
        self.dict_produto = {}
        self.state = 'Vazio'
        self.total_value = 0
        
    @classmethod
    def get_instance(self, cls, value):
        
        try:
            if self.instancia != False:
                print("Já existe um objeto")
                return self.instancia
        
        except:        
            print("Criando objeto...")
            self.instancia = Carrinho(cls.__create_key, value)
            return self.instancia
    
    def set_state(self, state_code):
    
        if state_code == 0:
            self.state = 'Vazio'
        
        elif state_code == 1:
            self.state = 'Em Andamento'

        elif state_code == 2:
            self.state = 'Fechado'
        
    def adicionar_produto(self, produto, quantidade_desejada):
        
        quantidade_atual = 0
        
        if produto in self.dict_produto.keys():
            quantidade_atual = self.dict_produto[produto]
        
        nova_quantidade = quantidade_atual + quantidade_desejada
        self.dict_produto[produto] = nova_quantidade
        self.total_value += produto.price * quantidade_desejada
        self.produto_adicionado(produto)
        self.set_state(1)
        
    def deletar_produto(self, produto):
        
        if produto in self.dict_produto.keys():
            quantidade = self.dict_produto.pop(produto)
            self.total_value -= produto.price * quantidade
            
        else:
            return False
        
        if len(self.dict_produto) == 0:
            self.set_state(0)
        
        self.produto_deletado(produto)
        return True

    def finalizar_compra(self):
        self.set_state(2)
    
    def print_produtos(self):
        for produto in self.dict_produto:
            print(f"\nProduto: {produto.name}\nQuantidade: {self.dict_produto[produto]}")
    
    def produto_adicionado(self, produto):
        
        print(f"\n{produto.name} foi adicionado ao seu carrinho.")
        
        print("\nCarrinho:\n")
        for produto_key in self.dict_produto:
            print(f"- {self.dict_produto[produto_key]}x {produto_key.name}")
        
        print(f"\nTotal: {self.total_value} R$")
    
    def produto_deletado(self, produto):
        
        print(f"\n{produto.name} foi removido do seu carrinho.")
        
        print("\nCarrinho:\n")
        for produto_key in self.dict_produto:
            print(f"- {self.dict_produto[produto_key]}x {produto_key.name}")
        
        print(f"\nTotal: {self.total_value} R$")
    
    