#Task 1 

#def midarf(first, *other):
#    sum_ = sum(other[0]) + first
#    return sum_/(len(other[0]) + 1)

#def diap(first, second):
#    tmp = (first + second)/2
#    print('MidArf = ', tmp)
#    if first <= second:
#        a = range(first + 1, second + 1)
        
#        sum = midarf(first, a)
#        print('MidArfRange = ', sum)
#    else:
#        print('Wrong range')

#def main():
#    first = int(input('Enter first number: '))
#    second = int(input('Enter second number: '))
#    diap(first, second)

#if __name__ == '__main__':
#    main()


#******************************************************************************************************

def sort_string(string):
    tmp = string.lower()
    tmp_list = tmp.split()
    tmp_list.sort()
    sorted_string = ''
    for i in tmp_list:
        sorted_string += str(i)
        sorted_string += ' '
    return sorted_string.capitalize()

def main():
    string = input('Enter string : ')
    sorted = sort_string(string)
    print(sorted)

if __name__ == '__main__':
    main()