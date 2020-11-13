class Carrinho(object):
    
    __create_key = object()
    
    def __init__(self, create_key, value):
        assert(create_key == Carrinho.__create_key), \
            "Carrinho objects must be created using Carrinho.get_instance"
        
        self.value = value
        self.instancia = False
        self.dict_produto = {}
    
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
        
    def adicionar_produto(self, produto, quantidade_desejada):
        
        quantidade_atual = 0
        
        if produto in self.dict_produto.keys():
            quantidade_atual = self.dict_produto[produto]
        
        nova_quantidade = quantidade_atual + quantidade_desejada
        self.dict_produto[produto] = nova_quantidade

    def deletar_produto(self, produto):
        
        if produto in self.lista_produto.keys():
            self.dict_produto.pop(produto)
            return True
        
        return False