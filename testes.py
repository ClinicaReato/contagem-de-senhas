import csv

Planilha_filtrada = {
    'Nome_do_prestador': ['Prestador A', 'Prestador B', 'Prestador C'],
    'Nome_do_paciente': ['Paciente 1', 'Paciente 2', 'Paciente 3'],
    'Data_do_atendimento': ['2024-05-16', '2024-05-17', '2024-05-18'],
    'Atendimento_excluido': [False, True, False],
    'Paciente_faltou': [True, False, False],
    'Paciente_cancelou_atendimento': [False, False, True],
    'Comentario_de_eventualidade': ['', 'Cancelado pelo paciente', '']
}

with open('nome_do_arquivo.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    cabecalho = Planilha_filtrada.keys()
    escritor.writerow(cabecalho)

    linhas = zip(*Planilha_filtrada.values())
    escritor.writerows(linhas)

print("Arquivo CSV criado com sucesso!")