"""
    __________________________________
   /        Nome          |   RA      \
  | Allan Silva Oliveira  | G375068    |
  | Matheus Lopes Ribeiro | N6318G1    |
   \__________________________________/
    """





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


    def InsertIntoFinal(self, value):
        """Insere no final"""
        current_node = self.head.next

        while current_node.next != self.head:
            current_node = current_node.next

        if self.head is None:
            self.head = Node(value)
            self.head.next = self.head
            self.head.before = self.head
            self.size = 1
        else:
            before_node = current_node

            current_node = Node(value)
            current_node.before = before_node
            before_node.next = current_node
            current_node.next = self.head
            self.head.before = current_node
            self.size += 1
    
    def Insert(self, value, position):
        cont = 1
        current_node = self.head

        if position <= 0:
            self.InsertIntoInit(value)
        
        while cont != position:
            current_node = current_node.next
            cont += 1

        if self.head is None:
            self.head = Node(value)
            self.head.next = self.head
            self.head.before = self.head
            self.size = 1

        elif position > self.size:
            self.InsertIntoFinal(value)
        
        else:
            before_node = current_node.before
            next_node = before_node.next
            
            current_node = Node(value)
            current_node.before = before_node
            current_node.next = next_node
            before_node.next = current_node
            next_node.before = current_node
            self.size += 1

    def SearchIndex(self, position):
        cont = 1
        current_node = self.head
        while cont != position:
            current_node = current_node.next
            cont += 1
        print(current_node.data)

    def SearchElement(self, element):
        cont = 1
        current_node = self.head
        while current_node.data != element:
            current_node = current_node.next
            cont += 1
            if cont > self.size:
                print("A value out of range the list")
                return
        print(f'The value [{element}] is in the position: [{cont}] ')
        
          

if __name__ == '__main__':
    # Making the List
    list = LinkedList()
    
    # Inserting a value to the list
    list.InsertIntoInit(6)
    list.InsertIntoInit(7)
    list.InsertIntoInit(8)
    list.InsertIntoInit(9)
    list.InsertIntoInit(11)
    list.InsertIntoInit(12)
    list.InsertIntoInit(13)
    list.InsertIntoInit(14)
    list.InsertIntoInit(15)
    list.InsertIntoInit(16)
    list.InsertIntoInit(18)
    # Display the list after entering the data
    
    
    list.LengthList()
    #Inserting a value at the end of the list
    list.InsertIntoFinal(19)
    list.InsertIntoFinal(20)

    # 
    list.LengthList()



    print("----------------")
    list.SearchElement(11)