{{
    config(
        materialized="view", 
        partition_by="Start_time", 
        cluster_by=["City", "State"]
    )
}}

-- Function 
    -- replaces null temperature values with the average temperature for that state and rounds the number, 
    -- Uses get_timezone macro to return the correct timezones

SELECT
    Start_time AS Start_Time,
    COALESCE(Description, 'Unknown') as Description,
    COALESCE(City, 'Unknown') as City,
    accidents.State as State,
    {{ get_timezone('accidents.State') }} as Timezone,
    ROUND(COALESCE(cast(Temperature_F_ as numeric), avg_temperature.avg_temp)) AS Temperature_F,
    ROUND(COALESCE(cast(Visibility_mi_ as numeric), avg_visibility.median_vis)) AS Visibility_Miles,
    COALESCE(Weather_condition, 'Unknown') AS Weather_Condition,
    CAST(Severity AS NUMERIC) AS Severity
FROM
    {{ source("staging", "accidents") }} AS accidents
LEFT JOIN (
    {{ get_avg_temperature() }}
) AS avg_temperature ON accidents.State = avg_temperature.State
LEFT JOIN (
    {{ get_avg_visibility() }}
) AS avg_visibility ON accidents.State = avg_visibility.State