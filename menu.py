def linha(tamanho_da_linha):
    print('##'+'-'*tamanho_da_linha+'##')

def titulo(titulo,tamanho_da_linha):
    print(f'##{titulo:^{tamanho_da_linha}}##')

def alinhado_a_esquerda(escolha,tamanho_da_linha):
    print(f'##{escolha:<{tamanho_da_linha}}##')