SET DATEFIRST 1;

DECLARE @startDate DATE = CONVERT(DATE, ?, 103);
DECLARE @endDate   DATE = CONVERT(DATE, ?, 103);

WITH DateSeries AS (
    SELECT @startDate AS [date]
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
             (DATEDIFF(DAY, DATEFROMPARTS(YEAR([date]), MONTH([date]), 1), [date])
                  + DATEPART(WEEKDAY, DATEFROMPARTS(YEAR([date]), MONTH([date]), 1)) - 1) / 7 + 1 AS semana
         FROM DateSeries
     )
DELETE FROM FT_Ventas
WHERE id_tiempo IN (
    SELECT dt.id_tiempo
    FROM DIM_Tiempo dt
             JOIN (
        SELECT DISTINCT año, trimestre, mes, semana
        FROM DateInfo
    ) d ON dt.año = d.año
        AND dt.trimestre = d.trimestre
        AND dt.mes = d.mes
        AND dt.semana = d.semana
)
OPTION (MAXRECURSION 0);
