#ASKING USER NUMBER AND BASE OF THE POWER
n1 = int(input('\nWrite the number that you want to raise: '))
n2 = int(input('\nWrite the base of the power: '))


#DEFINING FUNCTION WITH THESES TWO PARAMETERS
def power(n1, n2):
    result = n1 
    for a in range(1, n2):
        result *= n1
    return result


def main():
    print('\nThe result is {}.'.format(power(n1, n2)))


if __name__ == '__main__':
    main()