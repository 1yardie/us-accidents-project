{{
    config(
        materialized="table",
        schema='production'
    )
}}

with data as (
    SELECT *
    from {{ ref('stg_data') }}
)
SELECT
    Start_Time,
    Description,
    City,
    State,
    Timezone,
    Temperature_F,
    Visibility_Miles,
    Weather_Condition,
    Severity
FROM  
    data