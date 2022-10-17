class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertIntoInit(self, value):
        """Insere ao inicio"""
        if self.head is None:
            self.head = Node(value)
            self.head.next = self.head
            self.head.before = self.head
            self.size = 1
        else:
            current_node = self.head
            last_node = self.head.before

            self.head = Node(value)
            current_node.before = self.head
            self.head.next = current_node
            self.head.before = last_node
            last_node.next = self.head
            self.size += 1
    
    def LengthList(self):
        """Exibe os dados da lista"""
        cont = 1
        current_node = self.head
        while cont <= self.size:
            print(current_node.data)
            current_node = current_node.next
            cont += 1

    
    def RmvFirstPosition(self): 
        """Método que irá remover a primeira posição"""
        if self.head is None:
            print("A lista está vazia!")
            return
        
        current_node = self.head
        last = self.head.before

        self.head = current_node.next
        self.head.before = last
        self.head.next = current_node.next.next
        last.next = self.head
        self.size -= 1
        del current_node

    def RmvLastPosition(self):
        """Remove a ultima posição"""
        init = self.head
        current_node = self.head.next

        if self.head is None:
            print("A lista está vazia!")
            return
        while current_node.next != init:
            current_node = current_node.next

        preveous = current_node.before
        preveous.next = init
        self.head.before = preveous
        self.size -= 1
        del current_node

    def RmvCertainPosition(self, position):
        """Remove a posição escolhida do usuário"""
        current_node = self.head
        cont = 1

        if self.head is None:
            print("A lista está vazia")
            return
        elif position == 1:
            self.RmvFirstPosition()
            return
        elif position == self.size:
            self.RmvLastPosition()
            return
        
        while cont < position:
            current_node = current_node.next
            cont += 1
        
        preveous = current_node.before
        DelValue = current_node
        NextPosition = current_node.next
        NextPosition.before = preveous
        preveous.next = NextPosition

        if self.head == DelValue:
            self.head = NextPosition
        del DelValue
        self.size -= 1

    def RmvDeterminedValue(self, value):
        """Remove o valor escolhido do usuário"""
        if self.head is None:
            print("A Lista está vazia!")
            return
        else:
            current_node = self.head
            cont = 1
            while current_node.data != value:
                current_node = current_node.next
                cont += 1
            self.RmvCertainPosition(cont)

    
    



            

if __name__ == '__main__':
    #criando a lista
    lista = LinkedList()
    
    #Insere valor na lista
    lista.InsertIntoInit(5)
    lista.InsertIntoInit(6)
    lista.InsertIntoInit(7)  
    lista.InsertIntoInit(8)
    lista.InsertIntoInit(9)
    lista.InsertIntoInit(10)
    lista.InsertIntoInit(11)
    lista.InsertIntoInit(12)
    lista.InsertIntoInit(13)
    lista.InsertIntoInit(14)
    
    print('--------- Lista ----------')
    lista.LengthList() #Exibe a lista para o usuário 
    print('--------------------------')

    print("Removendo primeira posição: ")
    lista.RmvFirstPosition() #Remove a primeira posição da lista
    lista.LengthList()
    print('--------------------------')

    print("Removendo ultima posição: ")
    lista.RmvLastPosition()
    lista.LengthList()
    print('--------------------------')

    n = int(input('Digite qual posição deseja remover: '))
    lista.RmvCertainPosition(n)
    
    print('--------------------------')
    print(f"Lista após remoção da posiçaõ ({n}): ")
    lista.LengthList()

    n = int(input("Digite o valor que deseja remover: "))
    lista.RmvDeterminedValue(n)
    lista.LengthList()

    print("Tamanho da lista: ")
    print(lista.size)

    n = int(input("add o valor que deseja procurar na lista: "))
    print(lista.Search(n))

    
 """
        testar dps
        def Search(self, item):
        current_node = self.head
        found = False
        stop = False

        while current_node != None and not found and not stop:
            if current_node.LengthList() == item():
                found = True
            else:
                if current_node.LengthList() > item():
                    stop = True
                else:
                    current_node = current_node.next
        return found"""