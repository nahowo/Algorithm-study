WITH AI AS (
    SELECT *
    FROM ANIMAL_INS
    WHERE
        ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
)

SELECT NAME, DATETIME
FROM AI
ORDER BY DATETIME
LIMIT 3