WITH UI AS (
    SELECT *
    FROM USER_INFO
    WHERE
        GENDER IS NOT NULL
)

SELECT YEAR(A.SALES_DATE) AS YEAR, MONTH(A.SALES_DATE) AS MONTH, B.GENDER, COUNT(DISTINCT A.USER_ID) AS USERS
FROM ONLINE_SALE AS A
JOIN UI AS B
    USING (USER_ID)
GROUP BY YEAR(A.SALES_DATE), MONTH(A.SALES_DATE), B.GENDER
ORDER BY YEAR(A.SALES_DATE), MONTH(A.SALES_DATE), B.GENDER