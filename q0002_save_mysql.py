from q0001_random_series import random_series_list
import MySQLdb
import sys

def save_series(series):
    try:
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="123456",
                             db="app")

        cur = db.cursor()
        sql = "INSERT INTO series(series) VALUES (%s)"
        cur.execute(sql, (series))
        db.commit()

    finally:
        db.close()

def save_series_list(series_list):
    for series in series_list:
        # print series
        save_series(series)

def save_series_list_one_time(series_list):
    try:
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="123456",
                             db="app")
        cur = db.cursor()
        sql = "INSERT INTO series(series) VALUES (%s)"
        result = cur.executemany(sql, series_list)
        print result
        db.commit()

    finally:
        db.close()
        print "Finished!"

def search_series_with_more_queries():
    try:
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="123456",
                             db="app")
        cur = db.cursor()
        sql = "SELECT * FROM series WHERE series = %s"
        result = cur.executemany(sql, ['uiBjvnGZiO', 'CRqHG04eYt'])
        print result
        # results = cur.fetchall()
        # print results
        # db.commit()

    finally:
        db.close()

def main(series_list):
    # save_series_list(series_list)
    # save_series_list_one_time(series_list)
    search_series_with_more_queries()

if __name__ =="__main__":
    series_list = random_series_list(10)
    main(series_list)
