-- Query 4: Performance by Customer Segment
SELECT
    Segment,
    COUNT(DISTINCT "Customer ID") AS NumberOfCustomers,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM
    superstore
GROUP BY
    Segment
ORDER BY
    TotalProfit DESC;