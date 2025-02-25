import datetime
import pandas as pd
import os

# print(Planilha_filtrada)
def Salvar(Arquivo_a_ser_salvo):
    #print(f'Quantidade de nomes: {len(Planilha_filtrada["Nome_do_prestador"])}\nQuantidade de pacientes: {len(Planilha_filtrada["Nome_do_paciente"])}\nQuantidade de data do atendimento: {len(Planilha_filtrada["Data_do_atendimento"])}\nQuantidade de observações: {len(Planilha_filtrada["Observacoes"])}\nQuantidade de Faltas: {len(Planilha_filtrada["Paciente_faltou"])}\nQuantidade de cancelamentos: {len(Planilha_filtrada["Paciente_cancelou_atendimento"])}\nQuantidade de obs: {len(Planilha_filtrada["Comentario_de_eventualidade"])}')
    data_do_relatorio = str(datetime.date.today())
    planilha_para_salvar = pd.DataFrame(Arquivo_a_ser_salvo)
    os.system('cd Relatorio')
    planilha_para_salvar.to_excel('Relatorio/Planilha_filtrada'+data_do_relatorio+'.xlsx', index = False)
    os.system('cd ..')