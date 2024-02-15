from dotenv import load_dotenv
import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

load_dotenv()

#intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

#formaando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

#dados para api
city = 'Boston'
key = os.getenv("KEY")

URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
           f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')


#pandas
dados = pd.read_csv(URL)
print(dados.head())

#criar pasta
file_path = f'/home/stefan/Downloads/alura-air-flow/semana={data_inicio}/'
os.mkdir(file_path)

#salvar csv
dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
