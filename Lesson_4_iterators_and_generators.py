#values = [3, 2, 6, 5]
#it= iter(values) #create iterator
#while True:
#    try:
#        print(next(it))
#    except StopIteration:
#            break

#********************************************************

#class SimpleIterator:
#    def __getitem__(self, index): # "__getitem__" = "[ ]"
#        if 0 <= index <= 5:
#            return index * 2
#        else:
#            raise IndexError

#iterable = SimpleIterator()
#for value in iterable:
#    print(value)

#******************************************************************

import math

class MyRange:
    def __init__(self, first, second = None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second
        if step != 0:
            self.step = step
        else:
            raise ValueError('Step cannot be zero')
        self.lenght = math.ceil((self.end - self.start) / self.step)

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else: 
            raise IndexError('MyRange index out of range')
    
    def __iter__(self):
        return RangeIteratot(self)

    def __repr__(self):
        return 'MyRange({}, {}, {})'.format(self.start, self.end, self.step)


class RangeIteratot:
    def __init__(self, range_instance):
        self.range = range_instance
        self.current_value = range_instance.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value >= self.range.end and self.range.step > 0 or \
            self.next_value <= self.range.end and self.range.step < 0:
            raise StopIteration
        result = self.next_value
        self.next_value += self.range.step

        return result

#********************************************************************************************


# LIST CREATE 
#class List:
#    class _Node:
#        __slots__ = ('value', 'next') #Slots - attribute data. dont create dictionar

#        def __init__(self, value, next=None):
#            self.value = value
#            self.next = next

#    class _NodeIterator:
#        def __init__(self, first):
#            self._next_node = first

#        def __iter__(self): #must have each iterator
#            return self

#        def __next__(self):
#            if self._next_node is None:
#                raise StopIteration
#            value = self._next_node.value
#            self._next_node = self._next_node.next

#            return value

#    def __init__(self, iterable = None):
#        self._head = None
#        self._tail = None
#        self._lenght = 0

#        if iterable is not None:
#            self.extend(iterable)

#    def __len__(self):
#        return self._lenght

#    def append(self,value):
#        node = List._Node(value)

#        if len(self) == 0:
#            self._head = self._tail = node
#        else:
#            self._tail.next = node
#            self._tail = node

#        self._lenght += 1

#    def extend(self, iterable):
#        for value in iterable:
#            self.append(value)

#    def __getitem__(self, index):
#        if index < 0:
#            index += len(self)

#        if not 0 <= index < len(self):
#            raise IndexError

#        node = self._head
#        for _ in range(index):
#            node = node.next

#        return node.value

#    def __iter__(self): #if there is no __iter__ , python will build his own iterator on base __getitem__
#        return List._NodeIterator(self._head)

#*************************************************************************************************************

#                   GENERATOR

#yeild - operator - визначає генератор. (повертає значення при використовуванні цього оператора)
# START example:

#def generator():
#    yield 'hello'
#    yield 'world'

#def main():
#    g = generator()
#    print(g.__next__())
#    print(g.__next__())
#    print(g.__next__())
#if __name__ == '__main__':
#    main()

# END example

#*************************************************************
# START example:

#def fibonacci(count):
#    first, second = 0, 1
#    for _ in range(count):
#        yield second
#        first, second = second, first + second

#def main():
#    count = int(input('How many Fibonacci numbers to print? '))
#    for fib in fibonacci(count):
#        print(fib)
#if __name__ == '__main__':
#    main()

# END example

#*************************************************************

#  GENERATOR EXPRESSIONS

# function(x,y) for x in range(10) for y in range(5) if x != y

# START example:

#def generator_function():
#    for x in range(5):
#        for y in range(3):
#            if (x+y) % 2 == 0:
#                yield x + y

#gen = generator_function()
#fen = (x + y for x in range(5) for y in range(3) if(x + y) % 2 == 0)
## GEN = FEN - THE SAME SHIT - GENERETOR (just little expression)
#for value in fen:
#    print(value)

# END example

#*************************************************************

# SUBGENERATOR can called in GENERATOR by using 'yield from subgenerator()'

#*************************************************************