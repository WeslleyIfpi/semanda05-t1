def fracionaNumero(numero):
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena =  ((numero % 1000)  % 100) // 10
    unidade = ((numero % 1000)  % 100) % 10

    return unidade, dezena, centena, milhar

def inverteNumero(numero):
    unidade, dezena, centena, milhar = fracionaNumero(numero)
    
    novaMilhar = unidade * 1000
    novaCentena = dezena * 100
    novaDezena = centena * 10
    novaUnidade = milhar * 1

    numeroInvertido = novaMilhar + novaCentena + novaDezena + novaUnidade

    return numeroInvertido

def main():
    numero = int(input('Digite um número de 4 dígitos para ser invertido: '))
    numeroInvertido = inverteNumero(numero)
    print(f'{numero} invertido é : {numeroInvertido}')

if __name__ == '__main__':
    main()
   