{% macro get_avg_visibility(Visibility_mi_) %}
    SELECT
        State,
        AVG(COALESCE(CAST(Visibility_mi_ AS NUMERIC), 0)) AS avg_vis
    FROM
        {{ source("staging", "accidents") }}
    WHERE
        Visibility_mi_ IS NOT NULL
    GROUP BY
        State
{% endmacro %}