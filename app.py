from carrinho import Carrinho
from produto import Produto

def main():
    teste  = Carrinho.get_instance(Carrinho, "Im test")
    
    teste.adicionar_produto("Vibrador", 2)
    print(teste.dict_produto)
    print()

    teste_2 = Carrinho.get_instance(Carrinho, "Vai se fuder")
    print(teste_2.dict_produto)

if __name__ == "__main__":
    main()