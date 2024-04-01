{% macro get_avg_temperature(State) -%}

    SELECT
        '{{ state }}' AS State,
        AVG(COALESCE(CAST(Temperature_F_ as decimal), 0)) AS avg_temp
    FROM
        {{ source("staging", "accidents") }}
    WHERE 
        State = '{{State}}'
        AND Temperature_F_ IS NOT NULL
    GROUP BY State
{%- endmacro%}