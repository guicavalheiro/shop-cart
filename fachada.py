from carrinho import Carrinho
from produto import Produto
from pagamento import Pagamento

nome_cli    = 'Guilherme Cavalheiro'
cpf         = '111.111.111-11'
endereco    = 'Avenida Assis Brasil'
numero_casa = '666'
complemento = '1510'

carrinho  = Carrinho.get_instance(Carrinho, "Carrinho")
pagamento = Pagamento()

def menu():
    
    def listar_produtos(dictio):
        for produto in dictio:
            print(f"\nProduto: {dictio[produto].name}\nPreço: {dictio[produto].price}")

    def listar_carrinho():
        carrinho.print_produtos()
    
    def remover_produto(dictio):
        
        produto = ''
        while True:
            print("\nEscolha o produto a ser removido")
            carrinho.print_produtos()

            produto = input("\nProduto: ")
            
            result = produto in dictio
            
            if result:
                carrinho.deletar_produto(dictio[produto])
                print("\nProduto removido!")
                break
            
            else:
                print("\nProduto não encontrado.")    
          
    def fechar_compra():
        
        metodo = ''
        while True:
            print(f"\nO valor total da sua conta é de: {carrinho.total_value} R$")
     
            print("\n--- Escolha o método de pagamento ---")
            print("\n(1) - Cartão de débito")
            print("(2) - Cartão de crédito")
            print("(3) - Boleto bancário")
            
            choice = int(input("\nEscolha: "))
            
            if choice == 3:
                metodo = pagamento.add_metodo(choice, nome_cli, cpf= cpf, endereco= endereco, numero_casa= numero_casa, complemento= complemento)
                break
                
            elif choice == 1 or choice == 2:
                print("\nInsira as informações do seu método de pagamento.")
                numero_cartao   = input("Numero do cartão   : ")
                validade        = input("Validade           : ")
                seguranca       = input("Código de segurança: ")
                metodo = pagamento.add_metodo(choice, nome_cli, numero_cartao= numero_cartao, validade= validade, seguranca= seguranca)
                break
            
            else:
                print("\nEscolha uma opção de pagamento válida.")
                
        print("\nSua compra foi finalizada com os seguintes dados:\n")
        for dado in metodo:
            print(f"{dado}: {metodo[dado]}")
        print()
        
        carrinho.dict_produto = {}
        
    def adicionar_produto_a_lista(dictio):
        
        while True:
            print("\nEscolha o produto")
            listar_produtos(dictio)

            produto = input("\nProduto: ")
            
            result = produto in dictio
            
            if result:
                produto = dictio[produto]
                break
            
            else:
                print("\nEscolha um produto presente na lista.")
                
        while True:
            print("\nEscolha a quantidade")
            qntd = int(input("\nQuantidade: "))
            
            if qntd > 0 and type(qntd) is int:
                carrinho.adicionar_produto(produto, qntd)
                break
            else:
                print("\nInsira uma quantidade válida.")
    
    tv          = Produto(1, 'TV', 1000)
    notebook    = Produto(2, 'Notebook', 2000)
    modem       = Produto(3, 'Modem', 200)
    teclado     = Produto(4, 'Teclado', 100)
    monitor     = Produto(5, 'Monitor', 750)
    mouse       = Produto(6, 'Mouse', 5)
    
    dict_produtos = {'TV': tv, 
                     'Notebook': notebook, 
                     'Modem': modem, 
                     'Teclado': teclado,
                     'Monitor': monitor,
                     'Mouse': mouse }
    
    print("🗲🗲🗲🗲🗲🗲 Loja Eleletro 🗲🗲🗲🗲🗲🗲")
    print("\n--------------- Menu ---------------")
    while True:    
        
        print("\n(1) - Comprar produto")
        print("(2) - Remover produto do carrinho")
        print("(3) - Fechar compra")
        print("(4) - Listar produtos")
        print("(0) - Sair")
        
        choice = int(input("\nEscolha: "))
        
        if choice == 0:
            break
        
        elif choice == 1:
            adicionar_produto_a_lista(dict_produtos)
        
        elif choice == 2:
            remover_produto(dict_produtos)
        
        elif choice == 3:
            fechar_compra() 
        
        elif choice == 4:
            listar_carrinho()
            
if __name__ == "__main__":
    menu()