# Análise de Atrasos de Voos Brasileiros — ANAC 2024

## Pergunta de negócio
Quais companhias, rotas e períodos do ano concentram os maiores atrasos nos voos domésticos e internacionais do Brasil em 2024?

## Principais achados
- Gráfico 1 — Distribuição de atrasos: Os picos entre 1 e 2 na escala log correspondem a atrasos de 1 a 7 minutos — a maioria dos atrasos é curta. O comportamento irregular (dentes de serra) sugere que a ANAC arredonda os horários em intervalos fixos.
- Gráfico 2 — Evolução mensal: Janeiro e dezembro são os piores meses, o que faz sentido pelo volume de voos no verão e nas festas de fim de ano. O ponto zerado em janeiro de 2025 é um dado incompleto, pois o dataset cobre apenas 2024.
- Gráfico 3 — Por companhia: GTI (Tampa Cargo) registrou o maior atraso médio de 2024: ~414 minutos (quase 7 horas), em 2.318 voos operados — sugerindo atraso estrutural característico de operações de carga aérea.

## Stack
Python · Pandas · SQLite · Plotly · SQL

## Pipeline
1. `ingestao.py` — concatena os 12 CSVs mensais e carrega em SQLite
2. `queries/` — perguntas de negócio respondidas em SQL puro
3. `analise.ipynb` — Python lê os resultados e gera visualizações

## Fonte
ANAC — Histórico de Voos (VRA) 2024
