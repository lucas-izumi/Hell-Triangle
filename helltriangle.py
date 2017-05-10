import sys
import time

# Testa se o numero de linhas informado é menor ou igual a zero
class ErroLinhasInvalidas(Exception):
    def __init__(self, numLinhas):
        if numLinhas <= 0:
            self.error = 'Numero de linhas invalido. Insira um valor de linhas maior que zero'

    def __str__(self):
        return self.error

# Excecao para caso o triangulo possua uma configuração invalida
# (Cada linha deve possuir um elemento a mais que a linha anterior)
class ErroTrianguloInvalido(Exception):
    def __init__(self):
        self.error = 'Triangulo invalido. Encerrando execução'

    def __str__(self):
        return self.error

# Excecao para qualquer caso em que o numero de linhas informado
# seja maior que o numero de linhas do triangulo.
class ErroLinhaMaiorTriangulo(Exception):
    def __init__(self):
        self.error = 'Numero de linhas informado nao corresponde ao numero de linhas do triangulo'

    def __str__(self):
        return self.error

# Função privada. Retorna o maior elemento da linha e sua posicao
def _maiorElemento(linha, posicaoAnterior, triangulo):
    maior = -1
    posicaoAtual = -1
    i = 0
    # Percorre todos os elementos da linha e verifica qual o maior
    # Um elemento só pode ser selecionado como maior se for próximo do maior elemento
    # selecionado da linha anterior
    for elemento in triangulo[linha]:
        if int(elemento) > int(maior) and (posicaoAnterior == i or posicaoAnterior+1 == i):
            maior = elemento
            posicaoAtual = i
        i += 1

    # Retorna uma array contendo o valor do maior elemento e sua posição
    # A posição será utilizada como condição para encontrar o elemento da próxima linha
    resultado = [maior, posicaoAtual]
    return resultado


def HellTriangle(numLinhas, vetorTriangulo):
    # Verificação para valor de linha menor ou igual a zero
    if numLinhas <= 0:
        raise ErroLinhasInvalidas(numLinhas)

    # Verificação para triangulo invalido (linhas em tamanho desproporcionais)
    numElementos = 1
    for elementos in vetorTriangulo:
        if numElementos != len(elementos):
            raise ErroTrianguloInvalido()
        else:
            numElementos += 1
    
    soma = []
    numSomados = 0
    posicao = 0

    # Inicializando o vetor
    for i in range(0, numLinhas):
        soma += [0]

    # Faz a chamada da função maiorElemento para cada linha da pirâmide
    for i in range(0, numLinhas):
        try:
            resultados = _maiorElemento(i, posicao, vetorTriangulo)
        except:
            raise ErroLinhaMaiorTriangulo()

        # Adiciona o maior valor encontrado ao vetor de soma e guarda sua posicao
        soma[numSomados] = resultados[0]
        posicao = resultados[1]
        numSomados += 1
    # Imprime a lista de maiores elementos
    print(soma)

    # Soma os maiores elementos e imprime o total máximo
    totalMaximo = 0
    for elementos in soma:
        totalMaximo += int(elementos)
    print(totalMaximo)
    return totalMaximo


# Main Program
argList = sys.argv
if len(argList) == 3:
    tempoInicial = time.time()
    HellTriangle(argList[1], argList[2])
    print("Tempo de execucao: %s segundos" % (time.time() - tempoInicial))
