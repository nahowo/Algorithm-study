WITH DURATION AS (
    SELECT CAR_ID, DATEDIFF(END_DATE, START_DATE) + 1 AS DU
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
)

SELECT CAR_ID, ROUND(AVG(DU), 1) AS AVERAGE_DURATION
FROM DURATION
GROUP BY CAR_ID
HAVING AVG(DU) >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC