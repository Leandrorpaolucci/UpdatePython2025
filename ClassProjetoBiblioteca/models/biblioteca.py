from UpdatePython2025.ClassProjetoBiblioteca.models.avaliacao import Avaliacao
from UpdatePython2025.ClassProjetoBiblioteca.models.itens.item_biblioteca import ItemBiblioteca
class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False # Atributo Privado com "_"
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(15)} {str('Nota média'.ljust(15))}| {'Status'.ljust(15)}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} | {biblioteca.ativo} | {biblioteca.media_avaliacoes}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "Ativada" if self._ativo else "Desativada"
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        
        return f"A média da avaliação é de {media}"
    
    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def exibir_itens(self):
        print(f"Itens da Biblioteca: {self.nome}\n")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, 'isbn'):
                msg_livro = f"{i}. (Livro) - Titulo: {item._titulo} | Autor: {item._autor} |  Preço R$: {item._preco} | ISBN: {item.isbn}"
                print(msg_livro)
            else:
                msg_revista = f"{i}. (Revista) - Titulo: {item._titulo} | Autor: {item._autor} |  Preço R$: {item._preco} | ISBN: {item.edicao}"
                print(msg_revista)
                 


        
    

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()

Biblioteca.listar_bibliotecas()
