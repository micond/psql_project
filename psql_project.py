import psycopg2


def get_most_popular_articles():
    """Returns the most popular three articles of all time"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select articles.title, count(log.path) from log join articles
                 ON articles.slug = trim(both from log.path, '/article/')
                 GROUP BY articles.title limit 3""")

    print("1. What are the most popular three articles of all time?")
    for row in c:
        print("* ", row[0], "-", row[1])

    db.close()


get_most_popular_articles()


def get_most_popular_authors():
    """Returns the most viewed author"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select authors.name, COALESCE(t.count,'0') from authors left
                 join (select articles.author, count(log.path) from log join
                 articles ON articles.slug = trim(both from log.path,
                 '/article/') GROUP BY articles.author ORDER BY count DESC)
                 AS t ON authors.id = t.author""")

    print("2. Who are the most popular article authors of all time?")
    for row in c:
        print("* ", row[0], "-", row[1])

    db.close()


get_most_popular_authors()


def get_lead_errors():
    """Returns day with more than 1% of requests lead to error"""
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select date, round((cnt/((select count(status) from (select
                 date(time),status from log where status like '%4%' OR status
                 like '%5%') as x)/100)::float)::numeric,2)|| '% errors' as
                 percentage from (select to_char(date, 'FMMonth DD,YYYY') as
                 date, count(status) as CNT from (select date(time),status
                 from log where status like '%4%' OR status like '%5%') as t
                 GROUP BY date order by CNT DESC) as y
                 where cnt > ((select count(status) from (select date(time),
                 status from log where status like '%4%' OR status like '%5%')
                 as x)/100);""")

    print("3. On which days did more than 1% of requests lead to errors?")
    for row in c:
        print("* ", row[0], "-", row[1])

    db.close()


get_lead_errors()
