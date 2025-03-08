WITH RECURSIVE time AS (
    SELECT
        0 AS HOUR
    UNION ALL
    SELECT
        HOUR + 1
    FROM
        time
    WHERE
        HOUR < 23
)

SELECT
    time.HOUR,
    IFNULL(b.COUNT, 0) AS 'COUNT'
FROM
    time
LEFT JOIN (
    SELECT
        HOUR(DATETIME) AS HOUR,
        COUNT(*) AS 'COUNT'
    FROM
        ANIMAL_OUTS
    GROUP BY
        HOUR(DATETIME)
) AS b
ON
    time.HOUR = b.HOUR
ORDER BY
    HOUR