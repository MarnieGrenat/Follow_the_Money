import depedencies as dp

# Constants
GOTCHA          =   "#"
POSICAO_INICIAL =   [0, 0]
ESQUERDA        =   [-1, 0]
DIREITA         =   [1, 0]
ACIMA           =   [0, -1]
ABAIXO          =   [0, 1]
# Functions
def receber_parametro(path:str) -> str:
    pass
def reestruturar_matriz(_map:str) -> list:
    pass
def percorrer_matriz(matriz:list) -> float, list:
    posicao_atual = [0,0]
    direcao = verificar_direcao(matriz, posicao_atual)
    lista_dinheiro = []
    valor_total = 0
    try:
        while (matriz[posicao_atual] != GOTCHA):
            _, valor_atual, posicao_atual = verificar_valor(matriz, posicao_atual)
            if (_):
                valor_total += valor_atual 
                lista_dinheiro.append(valor_atual)

            direcao = verificar_direcao(matriz, posicao_atual, direcao)
    except:
        print("Erro! A execução não foi finalizada.")
    return valor_total, lista_dinheiro

def verificar_direcao(matriz:list, current_position:list, current_direction:list=[0,0]) -> list:
    direction = current_direction
    __list = ['-','/','\\', '|', '#']
    if matriz[current_position + direction] in __list:
        return current_direction
    
    if matriz[current_position + []]


    
def verificar_valor(matriz:list, current_position:list) -> bool, int, tuple:
    __list = ['-','/','\\', '|', '#']
    if matriz[current_position] in __list:
        return False, 0, []
    iteracao = current_direction
    value = str(matriz[current_position])
    while matriz[current_position + iteracao] not in __list:
        value += str(matriz[current_position + iteracao])
        iteracao += current_direction
    return True, int(value), (current_position + iteracao)


if __name__ == "__main__":
    _ = receber_parametro()
    mapa = reestruturar_matriz(_)
    valor_total, lista_ordenada = percorrer_matriz(mapa)

    print(f"Valor total do dinheiro derrubado: {valor_total}")
    print(f"Lista ordenada de dinheiro derrubado: /n{lista_ordenada}")