import pandas as pd
import sqlite3 as sql
import glob
import os

# Aponta para a pasta onde estão os 12 CSVs
PASTA = "data/raw/"
DB_PATH = "voos.db"

# Lê e concatena todos os arquivos
arquivos = glob.glob(os.path.join(PASTA, "VRA_2024*csv"))

dfs = []
for arquivo in sorted(arquivos):
    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="utf-8-sig", # remore o BOM do início
        skiprows=1,           # pula a linha "Atualizado em:"
        low_memory=False,
        keep_default_na = False
    )
    dfs.append(df)
    print(f"Carregada: {os.path.basename(arquivo)} - {len(df):,} linhas")

df_total = pd.concat(dfs, ignore_index=True)
# print(df_total.columns.tolist())
print(f"\nTotal combinado: {len(df_total):,} linhas")

# Renomeia colunas para snake_case sem espaços (facilita SQL)
df_total.columns = (
    df_total.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

print(df_total.columns.tolist())

colunas_uteis = [
    "icao_empresa_aérea",
    "código_tipo_linha",
    "icao_aeródromo_origem",
    "icao_aeródromo_destino",
    "partida_prevista",
    "partida_real",
    "chegada_prevista",
    "chegada_real",
    "situação_voo",
    "código_justificativa"
]

df_total = df_total[colunas_uteis]

# Força conversão explícita após o concat
df_total["partida_real"] = pd.to_datetime(df_total["partida_real"], errors="coerce")
df_total["partida_prevista"] = pd.to_datetime(df_total["partida_prevista"], errors="coerce")

df_total["atraso_partida_min"] = (
    (df_total["partida_real"] - df_total["partida_prevista"])
    .dt.total_seconds() / 60
)

# Cria coluna de atraso na partida em minutos
df_total["atraso_partida_min"] = (
    (df_total["partida_real"] - df_total["partida_prevista"])
    .dt.total_seconds() / 60
)

# Carrega no SQLite
conn = sql.connect(DB_PATH)
df_total.to_sql("voos", conn, if_exists="replace", index=False)
conn.close()

print(f"\nBanco criado: {DB_PATH}")
print("Colunas disponíveis:", df_total.columns.tolist())