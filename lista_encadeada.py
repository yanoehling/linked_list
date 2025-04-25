class Elemento:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

    def setProximo(self, prox):
        self.proximo = prox



class ListaEncadeada:
    def __init__(self):
        self.primeiro_elem = None
        self.ultimo_elem = None
        self.tamanho = 0      

    ## INSERÇÃO:

    def inserirNoInicio(self, valor):
        prox = self.primeiro_elem
        novo = Elemento(valor, prox)
        self.primeiro_elem = novo
        if self.tamanho == 0:
            self.ultimo_elem = novo
        self.tamanho += 1  
    
    def inserirNoFim(self, valor):
        if self.tamanho == 0:
            self.inserirNoInicio(valor)
        else:
            prox = None
            novo = Elemento(valor, prox)
            self.ultimo_elem.setProximo(novo)
            self.ultimo_elem = novo
            if self.tamanho == 0:
                self.primeiro_elem = novo
            self.tamanho += 1        
    
    def inserirNaPosicao(self, posicao, valor):
        if posicao < 0 or posicao > self.tamanho:
            print("Posicao inválida.")
        elif posicao == 0:
            self.inserirNoInicio(valor)
        elif posicao == self.tamanho:
            self.inserirNoFim(valor)
        else:
            elem_atual = self.primeiro_elem
            i = 1
            while elem_atual != None:
                prox = elem_atual.proximo
                if posicao == i:
                    novo = Elemento(valor, prox)
                    elem_atual.setProximo(novo)
                    self.tamanho += 1
                    break
                elem_atual = prox
                i += 1
            
    def inserirAntesDe(self, procurado, valor):
        elem_atual = self.primeiro_elem
        while elem_atual != None:
            prox = elem_atual.proximo
            if prox.valor == procurado:
                novo = Elemento(valor, prox)
                elem_atual.setProximo(novo)
                self.tamanho += 1
                return prox
            elem_atual = prox
        print("Valor de referência não encontrado.")

    def inserirDepoisDe(self, procurado, valor):
        elem_atual = self.primeiro_elem
        while elem_atual != None:
            prox = elem_atual.proximo
            if elem_atual.valor == procurado:
                novo = Elemento(valor, prox)
                elem_atual.setProximo(novo)
                self.tamanho += 1
                return elem_atual
            elem_atual = prox
        print("Valor de referência não encontrado.")

    ## REMOÇÃO:

    def removerPrimeiro(self):
        if self.tamanho > 0:
            self.primeiro_elem = self.primeiro_elem.proximo
            self.tamanho -= 1
        else:
            print(f"Lista já vazia")

    def removerUltimo(self):
        elem_atual = self.primeiro_elem
        if elem_atual == self.ultimo_elem:
            self.removerPrimeiro()
        else:
            while elem_atual != None:
                if elem_atual.proximo.proximo == None:
                    self.ultimo_elem = elem_atual
                    elem_atual.setProximo(None)
                    self.tamanho -= 1
                    break
                elem_atual = elem_atual.proximo
        
    def removerNaPosicao(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            print("Posicao inválida.")
        elif posicao == 0:
            self.removerPrimeiro()
        elif posicao == self.tamanho - 1:
            self.removerUltimo()  
        else:      
            elem_atual = self.primeiro_elem
            i = 1
            while elem_atual != None:
                prox = elem_atual.proximo
                if posicao == i:
                    elem_atual.setProximo(prox.proximo)
                    self.tamanho -= 1
                    break
                elem_atual = prox
                i += 1

    def removerValor(self, procurado):
        elem_atual = self.primeiro_elem
        while elem_atual != None:
            prox = elem_atual.proximo
            if prox.valor == procurado:
                elem_atual.setProximo(prox.proximo)
                self.tamanho -= 1
                return prox
            elem_atual = prox
        print("Valor não encontrado.")

    ## CONSULTA / ACESSO

    def acessaPrimeiro(self):
        if self.primeiro_elem != None:
            return self.primeiro_elem.valor
    
    def acessaUltimo(self):
        if self.ultimo_elem != None:
            return self.ultimo_elem.valor
    
    def acessaNaPosicao(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            print("Posicao inválida.")
        elif posicao == 0:
            return self.acessaPrimeiro()
        elif posicao == self.tamanho - 1:
            return self.acessaUltimo()
        else:
            elem_atual = self.primeiro_elem.proximo
            i = 1
            while elem_atual != None:
                if posicao == i:
                    return elem_atual.valor
                elem_atual = elem_atual.proximo
                i += 1
                
    def busca(self, valor_buscado):
        elem_atual = self.primeiro_elem
        for i in range(self.tamanho - 1):
            if elem_atual.valor == valor_buscado:
                return i
            elem_atual = elem_atual.proximo
        print("Valor não encontrado na lista.")

    # FUNCAO EXTRA (PRINTA COMO LISTA)

    def prt(self):
        lista_string = "["
        elem_atual = self.primeiro_elem
        if elem_atual != None:
            while True:
                lista_string += str(elem_atual.valor)
                if elem_atual.proximo == None:
                    break
                elem_atual = elem_atual.proximo
                lista_string += ", "
        lista_string += "]"
        print(lista_string) 
            