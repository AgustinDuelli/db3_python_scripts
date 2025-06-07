SET DATEFIRST 1;

DECLARE @startDate DATE = CONVERT(DATE, ?, 103);
DECLARE @endDate   DATE = CONVERT(DATE, ?, 103);

WITH DateSeries AS (
    SELECT @startDate  AS [date]  -- Parameter 0: startDate
    UNION ALL
    SELECT DATEADD(DAY, 1, [date])
    FROM DateSeries
    WHERE [date] < @endDate 
),
DateInfo AS (
    SELECT
        [date],
        YEAR([date]) AS año,
        DATEPART(QUARTER, [date]) AS trimestre,
        MONTH([date]) AS mes,
        DATEFROMPARTS(YEAR([date]), MONTH([date]), 1) AS first_day_of_month,
        (DATEDIFF(DAY, DATEFROMPARTS(YEAR([date]), MONTH([date]), 1), [date]) 
            + DATEPART(WEEKDAY, DATEFROMPARTS(YEAR([date]), MONTH([date]), 1)) - 1) / 7 + 1 AS semana
    FROM DateSeries
)
INSERT INTO [DIM_Tiempo] ([año], [trimestre], [mes], [semana])
SELECT DISTINCT año, trimestre, mes, semana
FROM DateInfo
WHERE NOT EXISTS (
    SELECT 1
    FROM [DIM_Tiempo] dt
    WHERE dt.año = DateInfo.año
      AND dt.trimestre = DateInfo.trimestre
      AND dt.mes = DateInfo.mes
      AND dt.semana = DateInfo.semana
)
OPTION (MAXRECURSION 0);
