#                       NASLIDYVANN9

#class Base:
#    def method(self):
#        print("Hello")

#class Child(Base):
#    def child_method(self):
#        print("Hello from child method")
#    def method(self):
#        print("Hello from redefined method")

#obj = Child()
#obj.method()

#**********************************************************************************

#class Figure:
#    def __init__(self, side = 0.0):
#        self.side = side

#class Square(Figure):
#    def draw(self):
#        for i in range(self.side):
#            print('* ' * self.side)

#class Triangle(Figure):
#    def draw(self):
#        for i in range(1, self.side + 1):
#            print('* ' * i)

#class Test(Triangle, Square ):
#    pass

#def main():
#    square = Square(2)
#    triangle = Triangle(5)
#    square.draw()
#    print()
#    triangle.draw()

#    test = Test(5)
#    test.draw()

#if __name__ == '__main__':
#    main()

#*****************************************************************************************************************
#                                        HOME WORK
#2.1 Naslidyvann9

class Editor:
    def __init__(self, ver = 2.7):
        self.version = ver

    def edit_document(self, way):
        print('Sorry, but you are using free version, buy ProVersion to use editor')
    
    def view_document(self, way):
        try:
            file = open(way, 'r')
        except ValueError:
            print('Wrong value "way"')
        else:
            str = file.read()
            print(str)
            file.close()
        finally:
            print('View ends')

class ProEditor(Editor):
    def __init__(self, ver = 3.0):
        self.version = ver     
    
    def edit_document(self, way):
        try:
            file = open(way, 'r+')
        except ValueError:
            print('Wrong value "way"')
        else:
            tmp = file.read()
            print(tmp)
            print("Do you want to write something?")
            answer = input('Y/N:\t')
            if(answer == 'Y' or answer == 'y'):
                print()
                str = input('Enter string: ')
                file.write('\n'+str)
                print()
                file.seek(0)
                tmp = file.read()
                print(tmp)
                file.close()
        finally:
            print('Edit ends')


def main():
    Key = 'AAAA-AAA1-FVAS-BL2F'
    KeyCheck = input('Enter key: ')
    if Key == KeyCheck:
        obj = ProEditor()
    else:
        obj = Editor()
    print('Welcome to Editor ver. {}'.format(obj.version))
    way = input('Enter way to file: ')
    obj.view_document(way)
    print()
    obj.edit_document(way)

if __name__ == '__main__':
        main()