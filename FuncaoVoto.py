from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return 'Sua situação eleitoral é: Negado'
    elif 18 < idade < 65:
        return 'Sua situação eleitoral é: Obrigatório'
    else:
        return 'Sua situação eleitoral é: Opcional'


# programa principal
nasc = int(input('Qual seu ano de nascimento? '))
print(voto(nasc))
