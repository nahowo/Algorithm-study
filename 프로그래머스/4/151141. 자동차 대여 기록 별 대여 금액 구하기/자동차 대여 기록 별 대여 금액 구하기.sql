WITH DT AS (
SELECT DURATION_TYPE, DISCOUNT_RATE
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
WHERE CAR_TYPE = '트럭'
)
, CRP AS (
SELECT A.HISTORY_ID, A.CAR_ID, DATEDIFF(A.END_DATE, A.START_DATE) + 1 AS DURATION,
    B.CAR_TYPE, B.DAILY_FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS A
JOIN CAR_RENTAL_COMPANY_CAR AS B
    USING (CAR_ID)
WHERE
    B.CAR_TYPE = '트럭'
)
, CR AS (
SELECT *, 
    CASE
        WHEN DURATION >= 90 THEN (SELECT DISCOUNT_RATE FROM DT WHERE DURATION_TYPE LIKE '90%')
        WHEN DURATION >= 30 THEN (SELECT DISCOUNT_RATE FROM DT WHERE DURATION_TYPE LIKE '30%')
        WHEN DURATION >= 7 THEN (SELECT DISCOUNT_RATE FROM DT WHERE DURATION_TYPE LIKE '7%')
        ELSE 0
    END AS DISCOUNT_RATE
FROM CRP
)

SELECT HISTORY_ID, ROUND(A.DAILY_FEE * (1 - A.DISCOUNT_RATE / 100) * A.DURATION, 0) AS FEE
FROM CR AS A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
    USING (HISTORY_ID)
ORDER BY FEE DESC, HISTORY_ID DESC