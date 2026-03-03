-- Evolução mensal do atraso médio ao longo de 2024
SELECT
    SUBSTR(partida_prevista, 1, 7) AS mes,
    COUNT(*) AS total_voos,
    ROUND(AVG(atraso_partida_min), 1) AS atraso_medio_min,
    SUM(CASE WHEN situação_voo = 'CANCELADO' THEN 1 ELSE 0 END) AS cancelamentos
FROM voos
GROUP BY mes
ORDER BY mes;