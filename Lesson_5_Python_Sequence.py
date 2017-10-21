#sequence -iterable object =  must have __getitem__() and __len__()

# [] = getitem
# 1:5 = class 'slice'

 # list = []

 # list can be SORTED list.sort()

 #  !!! �Ѳ ���� ������ � ϲ��Ͳ ������Ͳ !!!

 # TUPLE - KORTE}|{ КОРТЕЖ

 # my_tuple = (1, 'a string')
 # zip(list1, list2) - creating list of tuples

def function(x , *tmp): #tmp is creating tuple where saving all paramethers
     print(x)
     print(type(tmp))
     print(tmp)

function(2,3,6,7)