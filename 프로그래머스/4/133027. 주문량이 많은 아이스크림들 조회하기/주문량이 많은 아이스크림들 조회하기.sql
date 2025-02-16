WITH J AS (
    SELECT SUM(TOTAL_ORDER) AS TOTAL_ORDER, FLAVOR
    FROM JULY
    GROUP BY FLAVOR
)

, T_O AS (
    SELECT (A.TOTAL_ORDER + IFNULL(B.TOTAL_ORDER, 0)) AS TOTAL_ORDER, FLAVOR
    FROM FIRST_HALF AS A
    LEFT JOIN J AS B
        USING (FLAVOR)
    ORDER BY TOTAL_ORDER DESC
)

SELECT FLAVOR
FROM T_O
LIMIT 3