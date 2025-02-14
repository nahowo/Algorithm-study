SELECT ID, 
    CASE
        WHEN SC <= 100 THEN 'LOW'
        WHEN SC > 1000 THEN 'HIGH'
        ELSE 'MEDIUM'
    END AS SIZE
FROM (
    SELECT ID, SIZE_OF_COLONY AS SC
    FROM ECOLI_DATA) AS t
ORDER BY ID;