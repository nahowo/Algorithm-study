WITH F_TYPE AS (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES) AS FAVORITES
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)

SELECT A.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
FROM REST_INFO AS A
JOIN F_TYPE AS B
    ON A.FOOD_TYPE = B.FOOD_TYPE AND A.FAVORITES = B.FAVORITES
ORDER BY FOOD_TYPE DESC