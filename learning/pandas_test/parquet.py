import pandas as pd

pessoas_df = pd.DataFrame([
    {"nome":"Pedro", "idade": 15},
    {"nome":"João", "idade":30},
    {"nome":"Maria", "idade":19},
    {"nome":"Marcelo", "idade":18},
    {"nome":"Alex", "idade":38},
    {"nome":"Otavio", "idade":44},
    {"nome":"Ricardo", "idade":23},
    {"nome":"Camila", "idade":12},
    {"nome":"Alice", "idade":24},
    {"nome":"Marlei", "idade":32},
    {"nome":"Marilene", "idade":56},
    {"nome":"Judite", "idade":60},
])
print("DataFrame original:/n")
print(pessoas_df)

# Salva o DataFrame em um arquivo Parquet
pessoas_df.to_parquet("./dataset/pessoas.pq")
# Lê o arquivo Parquet e exibe o conteúdo
parquet_df = pd.read_parquet("dataset/pessoas.pq")
print("\nDataFrame lido do arquivo Parquet:/n")
print(parquet_df)
pessoas_df.to_csv("./dataset/pessoas.csv", index=False)
# Lê o arquivo CSV e exibe o conteúdo
csv_df = pd.read_csv("dataset/pessoas.csv")
print("\nDataFrame lido do arquivo CSV:/n")
print(csv_df)

