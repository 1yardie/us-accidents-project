-- Replace NULL values for Timezone with correct time zone for each state
{% macro get_timezone(state) -%}

    case {{state}}
        when 'AL' then 'US/Central'
        when 'AK' then 'US/Alaska'
        when 'AZ' then 'US/Mountain'
        when 'AR' then 'US/Central'
        when 'CA' then 'US/Pacific'
        when 'CO' then 'US/Mountain'
        when 'CT' then 'US/Eastern'
        when 'DC' then 'US/Eastern'
        when 'DE' then 'US/Eastern'
        when 'FL' then 'US/Eastern'
        when 'GA' then 'US/Eastern'
        when 'HI' then 'US/Hawaii'
        when 'ID' then 'US/Mountain'
        when 'IL' then 'US/Central'
        when 'IN' then 'US/Eastern'
        when 'IA' then 'US/Central'
        when 'KS' then 'US/Central'
        when 'KY' then 'US/Eastern'
        when 'LA' then 'US/Central'
        when 'ME' then 'US/Eastern'
        when 'MD' then 'US/Eastern'
        when 'MA' then 'US/Eastern'
        when 'MI' then 'US/Eastern'
        when 'MN' then 'US/Central'
        when 'MS' then 'US/Central'
        when 'MO' then 'US/Central'
        when 'MT' then 'US/Mountain'
        when 'NE' then 'US/Central'
        when 'NV' then 'US/Pacific'
        when 'NH' then 'US/Eastern'
        when 'NJ' then 'US/Eastern'
        when 'NM' then 'US/Mountain'
        when 'NY' then 'US/Eastern'
        when 'NC' then 'US/Eastern'
        when 'ND' then 'US/Central'
        when 'OH' then 'US/Eastern'
        when 'OK' then 'US/Central'
        when 'OR' then 'US/Pacific'
        when 'PA' then 'US/Eastern'
        when 'RI' then 'US/Eastern'
        when 'SC' then 'US/Eastern'
        when 'SD' then 'US/Central'
        when 'TN' then 'US/Central'
        when 'TX' then 'US/Central'
        when 'UT' then 'US/Mountain'
        when 'VT' then 'US/Eastern'
        when 'VA' then 'US/Eastern'
        when 'WA' then 'US/Pacific'
        when 'WV' then 'US/Eastern'
        when 'WI' then 'US/Central'
        when 'WY' then 'US/Mountain'
        else 'Unknown'
    end

{%- endmacro %}