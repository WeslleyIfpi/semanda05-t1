def horasEMinutos(totalMinutos):
    horas = totalMinutos // 60
    minutos = totalMinutos % 60
    return horas, minutos

def main():
    totalMinutos = int(input("Digite uma quantidade de minutos para ser convertido em horas e minutos: "))
    horas, minutos = horasEMinutos(totalMinutos)
    print(f'{totalMinutos} correspondem a: {horas}:{minutos:02}')

if __name__ == '__main__':
    main()