-- Ranking de companhias por atraso médio (apenas voos realizados)
SELECT
    icao_empresa_aérea AS companhia,
    COUNT(*) AS total_voos,
    ROUND(AVG(atraso_partida_min), 1) AS atraso_medio_min,
    SUM(CASE WHEN atraso_partida_min > 60 THEN 1 ELSE 0 END) AS voos_criticos
FROM voos
WHERE situação_voo = 'REALIZADO'
  AND atraso_partida_min IS NOT NULL
GROUP BY companhia
HAVING total_voos > 500        -- filtra companhias com volume relevante
ORDER BY atraso_medio_min DESC;