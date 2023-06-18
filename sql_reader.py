# filename sql_reader.py
import re
import jinja2
with open('queries.sql', 'r') as f:
    all_queries = f.read()

RE_GET_SQL = '(?<=-{{40}}BEGIN SQL QUERY-{{40}}\n-{{20}}NAME: {sql_query_name}-{{20}}\n)(?:(?!-{{40}}END SQL QUERY-{{40}})[\s\S])*(?=-{{40}}END SQL QUERY-{{40}})'
sql_query_name = 'GET ORDER DATA BY ORDER DATE'
re_pattern = RE_GET_SQL.format(sql_query_name=sql_query_name)
print(re_pattern)
print('--------------------------------')

match = re.search(re_pattern, all_queries)
try:
    query_template = match.group()
    print(query_template)
    print('--------------------------------')
except:
    query_template = "No query template"
    print("No query template matched")

jinja_template = jinja2.Template(query_template)
param = {'list_order_dates': ['2023-01-01', '2020-01-02', '2020-01-04']}
query = jinja_template.render(param)
print(query)
print('--------------------------------')

# Execute query
print('Executing query')
# database_connection.execute(query)
print('Query executed successfully')
