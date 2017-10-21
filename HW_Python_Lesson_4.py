## TASK 1
## REVERSED ITERATOR

#class RIterator:
#    def __iter__(self):
#        return self
   
#    def __next__(self, list_w):
#        value = list_w.pop()
#        return value
## TASK 2
## REVERSED GENERATOR
#def rev(t_list):
#    for i in range(len(t_list)):
#        value = t_list.pop()
#        yield value

#def main():
#    mlist = [1,2,3,4,5,6]
#    it = RIterator()
#    for i in rev(mlist):
#        print(i)

#if __name__ == '__main__':
#    main()
#************************************************************************************


##                      TASK 2


#class MyList(object):

#    class _ListNode(object):


#        __slots__ = ('value', 'prev', 'next')

#        def __init__(self, value, prev=None, next=None):
#            self.value = value
#            self.prev = prev
#            self.next = next

#        def __repr__(self):
#            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

#    class _Iterator(object):


#        def __init__(self, list_instance):
#            self._list_instance = list_instance
#            self._next_node = list_instance._head

#        def __iter__(self):
#            return self

#        def __next__(self):
#            if self._next_node is None:
#                raise StopIteration

#            value = self._next_node.value
#            self._next_node = self._next_node.next

#            return value

#    def __init__(self, iterable=None):

#        self._length = 0

#        self._head = None

#        self._tail = None


#        if iterable is not None:
#            for element in iterable:
#                self.append(element)

#    def append(self, element):



#        node = MyList._ListNode(element)

#        if self._tail is None:

#            self._head = self._tail = node
#        else:

#            self._tail.next = node
#            node.prev = self._tail
#            self._tail = node

#        self._length += 1

#    def __len__(self):
#        return self._length

#    def __repr__(self):

#        return 'MyList([{}])'.format(', '.join(map(repr, self)))

#    def __getitem__(self, index):
#        if not 0 <= index < len(self):
#            raise IndexError('list index out of range')

#        node = self._head
#        for _ in range(index):
#            node = node.next

#        return node.value

#    def __iter__(self):
#        return MyList._Iterator(self)
    
#    def clear(self):
#        if self._length == 0:
#            print('List is empty!')
#            return
#        while self._length >= 0:
#            if self._length == 1:
#                self._tail.value = None
#                self._tail = self._head = None
#                print('Cleared!')
#                return
#            self._tail.value = None
#            self._tail = self._tail.prev
#            self._tail.next = None
#            self._length -= 1

#    def add(self, index, value):
#        new_node = MyList._ListNode(value)
#        f_node = self._head
#        for _ in range(index - 2):
#            f_node = f_node.next
        
#        n_node = self._head
#        for _ in range(index - 1):
#            n_node = n_node.next

#        f_node.next = new_node
#        new_node.prev = f_node
#        n_node.prev = new_node
#        new_node.next = n_node
#        self._length += 1
    

       


#def main():

#    my_list = MyList([1, 2, 3,4,5,6,7,8,9,10])


#    print(len(my_list))


#    print(my_list)

#    print()


#    for element in my_list:
#        print(element)

#    print()
#    my_list.add(4, 99)

#    for element in my_list:
#        print(element)
#    print()
#    print(len(my_list))
#    my_list.clear()


#if __name__ == '__main__':
#    main()

#****************************************************************************

#                               TASK 4 (N)

def Eratosfen(number):
    list = []
    for i in range(number + 1):
        list.append(True)
    list[0] = list[1] = False
    p = 2
    #2step
    while(p*p < number):
         i = p * 2
         #3step
         for k in range(number):
             if i > number:
                 break
             list[i] = False
             i += p
         # 4 step
         for k in range(p+1,number):
             if list[k] == True:
                 p = k
                 break
    for tmp in range(number):
        if list[tmp]:
            yield tmp

def main():
    count = int(input('Enter number: '))
    for k in Eratosfen(count):
        print(k)

if __name__ == '__main__':
    main()
#list = [0,1,2,3,4,5,6,7,8,9]
#p = 2
#i= p * 2
#for k in list:
#    print(list[i])
#    i += p 