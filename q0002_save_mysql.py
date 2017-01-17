from q0001_random_series import random_series_list
import MySQLdb

def save_series(series):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="123456",
                         db="app")

    cur = db.cursor()
    sql = "INSERT INTO series(series) VALUES (%s)"
    cur.execute(sql, (series))
    db.commit()

    db.close()

def save_series_list(series_list):
    for series in series_list:
        # print series
        save_series(series)

def save_to_mysql(series_list):
    save_series_list(series_list)

if __name__ =="__main__":
    import sys

    series_list = random_series_list(10)
    save_to_mysql(series_list)
