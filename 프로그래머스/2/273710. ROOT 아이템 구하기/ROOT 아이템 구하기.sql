SELECT A.ITEM_ID, B.ITEM_NAME
FROM ITEM_TREE AS A
JOIN ITEM_INFO AS B
    USING (ITEM_ID)
WHERE
    A.PARENT_ITEM_ID IS NULL
ORDER BY ITEM_ID