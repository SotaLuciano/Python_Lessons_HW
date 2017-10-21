#raise ValueError('inv') #raise - ��������� ���������� ValueError - ���� �������� BaseException � ������ - ����


## TRY-EXCEPT
#try :               #������� 䳿 ���������
#    pass
#except Exception1:  #�������� ��������� ������������ � ��������
#    pass
#except Exception2:  #�������� ���������
#    pass
#except:             #��������� �� ����������
#    pass
#else:               #���� �� ���� ���������
#    pass
#finally:            #��� ���������� � ����-����� �������
#    pass
##�� ����� ���������� ����� ����� ����� �����, ��� ����� �� ����������
##����� � ���� ��������������� ������� ��������� "except (Exception1, Exception2)"
##"except Exception4 as exception:" - ��������, ���� ������� ����� Exception4 � ��� ��'��� ���������� ����� ����'����� �� ���� "exception"


#********************************************************************************************************************************************


#print('Calculator')

#try:
#    a = float(input('a = '))
#    b = float(input('b = '))
#    print(a / b)

##except ZeroDivisionError:
##    print('division by zero')
##except ValueError as error:
##    print(error)
## ��'�������� ��� ��������� � ����, �� ���� ��������� ���� � ���

#except (ZeroDivisionError, ValueError) as error:
#    print(error)



#print('Stopping the calculator.')


#************************************************************************************************************************


#def main():
#    while True:
#        try:
#            first_number= float(input('First number: '))
#            second_number = float(input('Second number: ')) 
#            print('Result: ', first_number / second_number)
#            break
#        except (ValueError, ZeroDivisionError) as error:
#            print('Error: ', error)
#            print('Please try again.')


#if __name__ == '__main__':
#    main()

#*************************************************************************************************************************

#def main():
#    try:
#        raise ValueError('value is incorrect')
#    except ValueError as error:
#        print('Exception: ', error )
#        raise

#try:
#    main()
#except ValueError:
#    print('ValueError detected')

##raise ValueError from ZeroDivisionError - value - __cause__ of zero 

#********************************************************************************************************

#                                   WARNING
import warnings

name = input('Input your first and last name: ')

if name.count(' ') != 1:
    warnings.warn('Name format may be incorrect')

print('Hello', name, '!', sep=' ')