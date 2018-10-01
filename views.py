#! /usr/bin/env python3

import psycopg2
db = psycopg2.connect("dbname=news")
c = db.cursor()


PERCENT_ERROR = '''
    CREATE OR REPLACE VIEW percentage_error AS
    SELECT
        daily_error_view.time::date,
        CAST(daily_error_view.Error_Count AS FLOAT) /
            CAST(daily_request_view.request_count AS FLOAT)
            AS percentage_error_value
    FROM daily_error_view
    INNER JOIN daily_request_view
    ON daily_error_view.time::date=daily_request_view.time::date
    GROUP BY daily_error_view.time::date, daily_error_view.Error_Count,
    daily_request_view.request_count;
'''



c.execute(PERCENT_ERROR)
db.commit()
db.close()
