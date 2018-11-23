#!/usr/bin/env python3

import psycopg2

try:
    db = psycopg2.connect(database="news")
except:
        print("Unable to connect to the database")
        
c = db.cursor()

c.execute("create view log_details as select path, count(*) as views FROM log group by path order by views desc")
c.execute("create view articles_Details as select articles.title, articles.slug, authors.name FROM articles, authors where articles.author=authors.id ")
c.execute("create view request_view as select date(time), count(*) as total_requests from log group by date(time)")
c.execute("create view request_error as select date(time), count(*) as total_errors from log where status='404 NOT FOUND' group by date")

c.execute("select articles_Details.title, log_details.views as view from log_details, articles_Details where log_details.path= '/article/'|| articles_Details.slug order by view desc limit 3")
post= c.fetchall()

c.execute("select result.name, sum(result.view) as sum_view from (select articles_Details.title, articles_Details.name, log_details.views as view from log_details, articles_Details where log_details.path= '/article/'|| articles_Details.slug) as result group by result.name order by sum_view desc ")
result2=c.fetchall()

c.execute("select request_view.date, (100.0*request_error.total_errors/request_view.total_requests) as precentage from request_view, request_error where request_view.date=request_error.date and (100.0*request_error.total_errors/request_view.total_requests) > 1 order by request_view.date")
result3=c.fetchall()

db.close()

print("What are the most popular three articles of all time?")
for row in post:
        print("\"{}\" -- {} views".format(row[0], row[1]))

print("\nWho are the most popular article authors of all time?")
for row in result2:
    print("{} -- {} views".format(row[0], row[1]))

print("\nOn which days did more than 1% of requests lead to errors?")
for row in result3:
    print("{} -- {}% errors".format(row[0], round(row[1],2)))
