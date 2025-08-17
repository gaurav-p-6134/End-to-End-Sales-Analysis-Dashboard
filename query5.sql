-- Query 5: Top 10 States by Sales
SELECT
    State,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM
    superstore
GROUP BY
    State
ORDER BY
    TotalSales DESC
LIMIT 10;