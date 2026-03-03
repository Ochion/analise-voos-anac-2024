-- Top 20 rotas com maior atraso médio
SELECT
    icao_aeródromo_origem AS origem,
    icao_aeródromo_destino AS destino,
    COUNT(*) AS total_voos,
    ROUND(AVG(atraso_partida_min), 1) AS atraso_medio_min
FROM voos
WHERE situação_voo = 'REALIZADO'
  AND atraso_partida_min > 0
GROUP BY origem, destino
HAVING total_voos > 100
ORDER BY atraso_medio_min DESC
LIMIT 20;