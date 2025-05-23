SELECT B.PRODUCT_CODE, (SUM(SALES_AMOUNT) * B.PRICE) AS SALES
FROM OFFLINE_SALE AS A
JOIN PRODUCT AS B
    USING (PRODUCT_ID)
GROUP BY PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE