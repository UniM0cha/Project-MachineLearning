import pymysql
import pandas as pd
from soupsieve import select

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='machine',
    passwd='learning',
    db='easy_order',
    charset='utf8'
)

cursor = db.cursor()


def select_sale(store_id, product_id):
    sql = """SELECT * FROM sale WHERE store_id=%s AND product_id=%s"""
    cursor.execute(sql, (store_id, product_id))
    result = cursor.fetchall()
    print(result)
    data = pd.DataFrame(result)
    data.columns = ['index', 'y', 'ds', 'product_id', 'store_id']
    data = data[['ds', 'y']]

    return data


select_sale(2, 2)
