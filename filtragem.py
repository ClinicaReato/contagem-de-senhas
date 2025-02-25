import tratamento_de_linha
import pandas as pd

def filtrar_planilha(caminho_da_planilha):
    
    planilha = pd.read_excel(caminho_da_planilha)
    
    Planilha_filtrada = {
        'Nome_do_prestador':[],
        'Nome_do_paciente':[],
        'Data_do_atendimento':[],
        'Observacoes':[],
        'Paciente_faltou':[],
        'Paciente_cancelou_atendimento':[],
        'Comentario_de_eventualidade':[]
    }

    # lista_de_prestadores = []
    # Devo_adicionar_o_proficional_a_lista = 0

    #Filtragem da planilha para a planilha filtrada
    for index,row in planilha.iterrows():
        #Converte as duas variaveis data e hora em uma variavel com data e hora.
        data_do_atendimento = tratamento_de_linha.data_e_hora(row)
        
        #Adicionar linha as planilhas filtradas
        if(((type(row['Atendido em']) != pd._libs.tslibs.nattype.NaTType) and (type(row['Agendamento excluido em']) == pd._libs.tslibs.nattype.NaTType))or(type(row['Observações']) != float)):
            
            # Preenchimento da planilha_Filtrada
            Planilha_filtrada['Nome_do_prestador'].append(row['Profissional'])
            Planilha_filtrada['Nome_do_paciente'].append(row['Paciente'])
            Planilha_filtrada['Data_do_atendimento'].append(data_do_atendimento)
            Planilha_filtrada['Observacoes'].append(row['Observações'])
            Planilha_filtrada['Paciente_faltou'].append(True)
        
            if(type(row['Cancelado pelo paciente em']) == pd._libs.tslibs.timestamps.Timestamp or type(row['Cancelado por SMS em']) == pd._libs.tslibs.timestamps.Timestamp):
                Planilha_filtrada['Paciente_cancelou_atendimento'].append(True)
            else:
                Planilha_filtrada['Paciente_cancelou_atendimento'].append(False)

            comentarios = []
            #Agendamentos feitos para o passado
            if(data_do_atendimento < row['Agendado em']):
                comentarios.append('Agendamento feito para o passado?')

            #Atendimento normal
            if((type(row['Agendado em'])!=pd._libs.tslibs.nattype.NaTType)and(type(row['Atendido em']!=pd._libs.tslibs.nattype.NaTType))):
                comentarios.append('Paciente atendido normalmente')
            
            #Atendimento Cancelado pelo paciente
            if((type(row['Agendamento excluido em']) != pd._libs.tslibs.nattype.NaTType )and((type(row['Cancelado por SMS em']) != pd._libs.tslibs.nattype.NaTType)or(type(row['Cancelado pelo paciente em']) != pd._libs.tslibs.nattype.NaTType))):
                comentarios.append('Agendamento cancelado pelo paciente precisa verificar o motivo')

            Planilha_filtrada['Comentario_de_eventualidade'].append(comentarios)

            #preenchimento da planilha de prestadores
            # if len(lista_de_prestadores) == 0:
            #     lista_de_prestadores.append(row['Profissional'])
            # else:
            #     for prestador in lista_de_prestadores:
            #         if(prestador == row['Profissional']):
            #             Devo_adicionar_o_proficional_a_lista += 1
            #             break    

            #     if(Devo_adicionar_o_proficional_a_lista<1):
            #         lista_de_prestadores.append(row['Profissional'])
                
            #     Devo_adicionar_o_proficional_a_lista=0
    return Planilha_filtrada