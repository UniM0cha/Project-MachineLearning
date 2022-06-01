import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='machine',
    passwd='learning',
    db='easy_order',
    charset='utf8'
)

cursor = db.cursor()


def select_item():
    sql = """SELECT * FROM sale"""
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result


select_item()
