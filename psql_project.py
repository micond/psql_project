#! /usr/bin/env python3
import psycopg2


def get_most_popular_articles():
    """Returns the most popular three articles of all time"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select title, count(*) as views from log join articles
                 on log.path = concat('/article/', articles.slug) group by
                 title order by views desc limit 3;""")

    print("1. What are the most popular three articles of all time?")
    for row in c:
        print(" *", row[0], "-", row[1])

    db.close()


def get_most_popular_authors():
    """Returns the most viewed author"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select authors.name, COALESCE(t.count,'0') from authors left
                 join (select articles.author, count(log.path) from log join
                 articles ON concat('/article/', articles.slug) = log.path
                 GROUP BY articles.author ORDER BY count DESC)
                 AS t ON authors.id = t.author;""")

    print("2. Who are the most popular article authors of all time?")
    for row in c:
        print(" *", row[0], "-", row[1])

    db.close()


def get_lead_errors():
    """Returns day with more than 1% of requests lead to error"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select to_char(date,'Mon DD, YYYY'), round((((err/total)*100)
                 ::float)::numeric,2)|| '% errors' as percentage from
                 (select time::date as date, count(*) as total,
                 sum((status != '200 OK')::int)::float as err from log group
                 by date) as foo where ((err/total)*100) > 1;""")

    print("3. On which days did more than 1% of requests lead to errors?")
    for row in c:
        print(" *", row[0], "-", row[1])

    db.close()


if __name__ == '__main__':
    get_most_popular_articles()
    get_most_popular_authors()
    get_lead_errors()
