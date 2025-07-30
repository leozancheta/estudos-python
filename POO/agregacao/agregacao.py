class Produto:
    def __init__(self, nome: str, preco: int):
        self.nome = nome
        self.preco = preco
    def informacoes_produto(self) -> None:
        print(f"Produto: {self.nome}, Preço: {self.preco} reais")

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.produtos.append(produto)

    def fnalizar_compra(self) -> None:
        print("Finalizando compra...")
        print("Produtos no carrinho:")
        for produto in self.produtos:
            produto.informacoes_produto()
        print("Compra finalizada com sucesso!")

banana = Produto("Banana", 3)
maca = Produto("Maçã", 5)
uva = Produto("Uva", 7)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(banana)
carrinho.adicionar_produto(maca)
carrinho.adicionar_produto(uva)

carrinho.fnalizar_compra()