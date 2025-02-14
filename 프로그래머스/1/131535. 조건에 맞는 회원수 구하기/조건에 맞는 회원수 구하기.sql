-- 코드를 입력하세요
SELECT count(USER_ID) AS USERS
FROM USER_INFO
WHERE
    20 <= AGE
    AND
    AGE <= 29
    AND
    YEAR(JOINED) = '2021'