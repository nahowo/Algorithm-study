WITH UI AS (
    SELECT *
    FROM USER_INFO
    WHERE
        YEAR(JOINED) = '2021'
)
, J AS (
    SELECT COUNT(USER_ID) AS CNT
    FROM UI
)

SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, 
    COUNT(DISTINCT USER_ID) AS PURCHASED_USERS, 
    ROUND(COUNT(DISTINCT USER_ID) / (SELECT CNT FROM J), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE
WHERE
    USER_ID IN (SELECT USER_ID FROM UI)
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH