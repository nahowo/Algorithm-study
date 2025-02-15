WITH SALE AS (
    SELECT WRITER_ID AS USER_ID, SUM(PRICE) AS TOTAL_SALES
    FROM USED_GOODS_BOARD
    WHERE
        STATUS = 'DONE'
    GROUP BY WRITER_ID
    HAVING SUM(PRICE) >= 700000
)

SELECT A.USER_ID, B.NICKNAME, A.TOTAL_SALES
FROM SALE AS A
JOIN USED_GOODS_USER AS B
    USING (USER_ID)
ORDER BY TOTAL_SALES