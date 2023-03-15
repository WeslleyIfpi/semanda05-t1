def calculaPreco(preco, porcentagem):
    calcPorcentagem = preco*(porcentagem / 100)
    return preco + calcPorcentagem, preco - calcPorcentagem

def main():
    print('Esse programa calcula o aumento e o desconto no valor de um produto:')
    valor = float(input('Digite o valor do produto: R$'))
    porcentagem = float(input('Digite a porcentagem do aumento e desconto: '))
    valorAumento,  valorDesconto = calculaPreco(valor, porcentagem)
    print(f'Preço com aumento: R${valorAumento:.2f}')
    print(f'Preço com desconto: R${valorDesconto:.2f}')

if __name__ == '__main__':
    main()