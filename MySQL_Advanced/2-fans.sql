--  SQL script that ranks country origins of bands
SELECT origin, sum(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans desc;