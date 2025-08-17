-- Query 1: Overall Performance
SELECT
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit,
    (SUM(Profit) / SUM(Sales)) * 100 AS OverallProfitMargin
FROM
    superstore;