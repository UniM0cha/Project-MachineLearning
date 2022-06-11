import pymysql
import pandas as pd

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='machine',
    passwd='learning',
    db='easy_order',
    charset='utf8'
)

cursor = db.cursor()


def select_product_stock(store_id):
    sql = '''SELECT p.product_id, p.product_name, s.stock
    FROM stock s, product p
    WHERE s.product_id = p.product_id
    AND s.store_id = %s'''
    cursor.execute(sql, (store_id, ))
    result = cursor.fetchall()
    return result


def select_product_stock_page(store_id, page):
    sql = '''SELECT p.product_id, p.product_name, s.stock
    FROM stock s, product p
    WHERE s.product_id = p.product_id
    AND s.store_id = %s
    LIMIT 5
    OFFSET %s'''
    cursor.execute(sql, (store_id, (page-1)*5))
    result = cursor.fetchall()
    return result


def select_stock_product_id(store_id, product_id):
    sql = '''SELECT p.product_id, p.product_name, s.stock
    FROM stock s, product p
    WHERE s.product_id = p.product_id
    AND s.store_id = %s
    AND s_product_id = %s'''
    cursor.execute(sql, (store_id, product_id))
    result = cursor.fetchone()
    return result


def select_sale(store_id, product_id):
    sql = """SELECT * FROM sale WHERE store_id=%s AND product_id=%s"""
    cursor.execute(sql, (store_id, product_id))
    result = cursor.fetchall()
    data = pd.DataFrame(result)
    data.columns = ['index', 'y', 'ds', 'product_id', 'store_id']
    data = data[['ds', 'y']]

    return data


def select_product(store_id, page):
    return


def select_stock(store_id):
    sql = '''SELECT * FROM stock WHERE store_id=%s'''
    return


def select_all_store():
    sql = '''SELECT store_id FROM store'''
    cursor.execute(sql)
    result = list(cursor.fetchall())
    return result


def select_all_product():
    sql = '''SELECT product_id FROM product'''
    cursor.execute(sql)
    result = list(cursor.fetchall())
    return result
