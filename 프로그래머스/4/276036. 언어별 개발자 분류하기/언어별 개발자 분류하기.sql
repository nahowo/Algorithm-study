WITH FE AS (
    SELECT SUM(CODE)
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
    GROUP BY CATEGORY
)
, G AS (
    SELECT
        CASE
            WHEN 
                (SELECT * 
                FROM FE) & SKILL_CODE > 0
                AND
                (SELECT CODE
                FROM SKILLCODES 
                WHERE NAME = 'Python') & SKILL_CODE > 0
            THEN 'A'
            WHEN 
                (SELECT CODE
                 FROM SKILLCODES 
                 WHERE NAME = 'C#') & SKILL_CODE > 0
            THEN 'B'
            WHEN 
                (SELECT * 
                 FROM FE) & SKILL_CODE > 0
            THEN 'C'
            ELSE NULL
        END AS GRADE,
        ID,
        EMAIL
    FROM DEVELOPERS
)

SELECT GRADE, ID, EMAIL
FROM G
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID