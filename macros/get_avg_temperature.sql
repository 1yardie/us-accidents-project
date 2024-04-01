{% macro get_avg_temperature(State) -%}

    SELECT
        State,
        AVG(COALESCE(CAST(Temperature_F_ AS NUMERIC), 0)) AS avg_temp
    FROM
        {{ source("staging", "accidents") }}
    GROUP BY
        State

{%- endmacro%}