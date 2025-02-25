import pandas as pd
import datetime

def data_e_hora(linha):
    hora_str = linha['Hora']+":00"
    hora = datetime.datetime.strptime(hora_str,'%H:%M:%S').time()
    data = linha['Data'].to_pydatetime()
    dataEhora = datetime.datetime.combine(data,hora)

    return dataEhora