SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS AS A
JOIN ANIMAL_INS AS B
    USING (ANIMAL_ID)
ORDER BY B.DATETIME - A.DATETIME
LIMIT 2