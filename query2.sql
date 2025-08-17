-- Query 2: Profitability by Category
SELECT
    Category,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM
    superstore
GROUP BY
    Category
ORDER BY
    TotalProfit DESC;