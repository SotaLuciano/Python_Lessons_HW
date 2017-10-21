#CREATING BOOK CLASS AND LEAVE COMMENTS


class BOOK:
    def __init__(self):
        self.name = input('Enter name of book: ')
        self.author = input('Name of author: ')
        self.year = int(input('Year edition: '))
        self.otzuv = []
    
    @classmethod
    def change_name(self):
        self.name = input('Enter name of book: ')

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author and self.year == other.year
    def __repr__(self):
        return "{} ,{} ,{}, {}".format(self.author, self.name, self.year, self.otzuv)
    def __str__(self):
        return """Book: '{}', author - {}, year - {}
        Otzuvu: {}
        """.format(self.name,self.author,self.year, self.otzuv)


class Make_Otzuv:
    @staticmethod
    def make_otzuv(book):
        book.otzuv.append(input("Say something about {} : ".format(book.name)))



def main():
    first_book = BOOK()
    #second_book = BOOK()
    Make_Otzuv.make_otzuv(first_book)
    Make_Otzuv.make_otzuv(first_book)
    Make_Otzuv.make_otzuv(first_book)

    print(first_book)
    #print(first_book.__repr__())



if __name__ == '__main__':
    main()




