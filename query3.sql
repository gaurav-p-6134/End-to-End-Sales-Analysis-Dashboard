-- Query 3: Loss-making Sub-categories
SELECT
    "Sub-Category",
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM
    superstore
GROUP BY
    "Sub-Category"
HAVING
    TotalProfit < 0
ORDER BY
    TotalProfit ASC;