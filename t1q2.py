def areaQuadrado(lado):
    return lado**2

def perimetroQuadrado(lado):
    return lado*4

def main():
    print('Esse programa calcula a area e perimetro de um quadradado.')
    lado = float(input('Digite o tamanho do lado do quadrado: '))
    area = areaQuadrado(lado)
    perimetro = perimetroQuadrado(lado)
    print(f'Area: {area:10.4f}')
    print(f'Perimetro: {perimetro:10.4f}')

if __name__ == '__main__':
    main()