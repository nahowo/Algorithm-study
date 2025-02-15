WITH RECURSIVE GENERATION AS (
    SELECT ID, PARENT_ID, 1 AS GEN
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT A.ID, A.PARENT_ID, B.GEN + 1 AS GEN
    FROM ECOLI_DATA AS A
    JOIN GENERATION AS B
        ON A.PARENT_ID = B.ID
)

, CHILDLESS AS (
    SELECT ID
    FROM ECOLI_DATA
    WHERE
        ID NOT IN (SELECT PARENT_ID
                    FROM ECOLI_DATA
                    WHERE PARENT_ID IS NOT NULL)
)

SELECT COUNT(C.ID) AS COUNT, G.GEN AS GENERATION
FROM CHILDLESS AS C
JOIN GENERATION AS G
    USING (ID)
GROUP BY G.GEN
ORDER BY G.GEN