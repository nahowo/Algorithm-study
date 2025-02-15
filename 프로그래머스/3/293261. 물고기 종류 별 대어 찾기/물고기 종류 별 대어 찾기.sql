
SELECT A.ID, C.FISH_NAME, A.LENGTH
FROM FISH_INFO AS A
JOIN
    (SELECT FISH_TYPE, MAX(LENGTH) AS ML
    FROM FISH_INFO
    GROUP BY FISH_TYPE) AS B
    ON A.FISH_TYPE = B.FISH_TYPE AND A.LENGTH = B.ML
JOIN
    FISH_NAME_INFO AS C
    ON A.FISH_TYPE = C.FISH_TYPE
ORDER BY ID