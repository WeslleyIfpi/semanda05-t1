def calcular(a, b, c):
    return 2 * a + 5 * b - c

def main():
    print('Esse programa calcula 2 * a + 5 * b - c.')
    a = int(input('Digite a: '))
    b = int(input('Digite b: '))
    c = int(input('Digite c: '))
    
    print(f'Resultado: {calcular(a, b, c)}')
    
if __name__ == '__main__':
    main()