-- Visão geral: total de voos por situação
SELECT
    situação_voo,
    COUNT(*) AS total,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM voos), 2) AS percentual
FROM voos
GROUP BY situação_voo
ORDER BY total DESC;