import copy
from collections import defaultdict
class Grafo:
    def __init__(self):
        self.lista_adjacencias = defaultdict(list)

    # Cria um array dentro da chave do dicionario em que a chave é o nome do vertice
    def adiciona_vertice(self,vertice):
        if not vertice in self.lista_adjacencias:
            self.lista_adjacencias[vertice] = []

    # Verifica se os vertices passados por parametro realmente existem, caso não existam, são criados, e após isso é adcionado uma aresta ponderada entre eles
    def adiciona_aresta(self,vertice1,vertice2,peso):
        if not vertice1 in self.lista_adjacencias:
            self.lista_adjacencias[vertice1] = []
        if not vertice2 in self.lista_adjacencias:
            self.lista_adjacencias[vertice2] = []
        self.lista_adjacencias[vertice1].append((vertice2,peso))

    # Remove a aresta entre os vertices1 e vertice2, caso o vertice 1 exista dentro da lista de adjacencias, aresta[0]
    def remove_aresta(self,vertice1,vertice2):
        listaAdj = copy.deepcopy(self.lista_adjacencias[vertice1])
        if vertice1 in self.lista_adjacencias:
            for aresta in listaAdj:
                if aresta[0] == vertice2:
                    self.lista_adjacencias[vertice1].remove(aresta)
        else:
            return "Vertice não existe"
    # Remove todas as arestas do vertice usado como parametro na função, para só então remover seu respectivo vertice do dicionario
    def remove_vertice(self,vertice):
        listaAdj = copy.deepcopy(self.lista_adjacencias)
        if vertice in self.lista_adjacencias:
            for v, arestas in listaAdj.items():
                for a in arestas[:]:
                    if a[0] == vertice:
                        self.lista_adjacencias[v].remove(a)

        self.lista_adjacencias.pop(vertice)

    # Verifica se dois vertices possuem arestas entre si, retorna um boolean
    def tem_aresta(self,vertice1,vertice2):
        for aresta in self.lista_adjacencias[vertice1]:
            if aresta[0] == vertice2:
                return True
        for aresta in self.lista_adjacencias[vertice2]:
            if aresta[0] == vertice1:
                return True
        return False

    # Numero de vertices que possuem entrada ao vertice passado no parametro
    def grau_entrada(self,vertice):
        cont = 0
        for vert in self.lista_adjacencias:
            for arestas in self.lista_adjacencias[vert]:
                if arestas[0] == vertice:
                    cont += 1
        return cont
    # Quantidade de arestas que X vertice possui
    def grau_saida(self,vertice):
        return len(self.lista_adjacencias[vertice])
    def print_lista(self):
        for vertice in self.lista_adjacencias:
            print(f"{vertice}:",end='')
            for aresta in self.lista_adjacencias[vertice]:
                print(f"{aresta} ->",end='')
            print()
        print('\n')


grafo = Grafo()
grafo.adiciona_vertice("Pedro")
grafo.adiciona_aresta("Victor", 'Guilherme', 2)
grafo.adiciona_aresta("Victor", 'Rafaela', 2)
grafo.adiciona_aresta("Victor", 'Henrique', 2)
grafo.adiciona_aresta("Henrique", 'Rafaela', 2)

grafo.print_lista()
grafo.remove_vertice("Rafaela")
grafo.print_lista()

print(grafo.tem_aresta("Victor","Guilherme"))
grafo.remove_aresta("Victor","Guilherme")
print(grafo.tem_aresta("Victor","Guilherme"))
print('\n')

grafo.print_lista()


