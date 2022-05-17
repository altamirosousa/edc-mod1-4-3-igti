# ...::: Instruções :::...
# Executar preparação S3: aws configure

import boto3
import pandas as pd

# Cria um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

# Caminho local
path = 'C:\\Users\\altamiro.sousa\\OneDrive\\PARTICULAR\\Pós-Graduação\\Bootcamp - EDC-EngDeDadosCloud\\Modulo 1\\_ExerciciosPraticos\\'

#Upload de arquivos para o S3
s3_client.upload_file(path+'data\\MICRODADOS_ENEM_2020_MG.csv',
                      'datalake-igti-altamiro-aula-3-1',
                      'upload/MICRODADOS_ENEM_2020_MG_UPLOAD.csv')
print('Upload realizado com sucesso!')

#Download de arquivos do S3
s3_client.download_file('datalake-igti-altamiro-aula-3-1',
                        'upload/MICRODADOS_ENEM_2020_MG_UPLOAD.csv',
                        path+'data\\download\\MICRODADOS_ENEM_2020_MG_DOWNLOAD.CSV')
print('Download realizado com sucesso!')

#Exibição de dados
df = pd.read_csv(path+'data\\download\\MICRODADOS_ENEM_2020_MG_DOWNLOAD.CSV', sep=';')
print(df)
