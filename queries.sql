----------------------------------------BEGIN SQL QUERY----------------------------------------
--------------------NAME: GET ORDER DATA BY ORDER DATE--------------------
SELECT * 
FROM order
WHERE order_date = {% for od_date in list_order_dates %}'{{ od_date }}' {% if not loop.last %} 
OR order_date = {% endif %}{% endfor %};
----------------------------------------END SQL QUERY----------------------------------------

----------------------------------------BEGIN SQL QUERY----------------------------------------
--------------------NAME: ANY NAME HERE 2--------------------
--30 lines of code here
SELECT * 
FROM some_others_tables
WHERE column_name_1 = 'value1';
----------------------------------------END SQL QUERY----------------------------------------

----------------------------------------BEGIN SQL QUERY----------------------------------------
--------------------NAME: ANY NAME HERE 3--------------------
--30 lines of code here
SELECT * 
FROM some_other_tables;
----------------------------------------END SQL QUERY----------------------------------------