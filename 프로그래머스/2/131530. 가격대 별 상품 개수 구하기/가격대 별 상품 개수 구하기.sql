WITH P AS (
    SELECT FLOOR(PRICE / 10000) * 10000 AS PRICE_GROUP
    FROM PRODUCT)

SELECT PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM P
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP
