import pymysql
db = pymysql.connect("localhost","root","ipuemipuem","python",\
    use_unicode=True,charset='utf8')
    # use_unicode=True,charset='utf8' เปิด utf8 เพื่อลองรับภาษาไทย
cursor = db.cursor()
def showuse():
    try:
        # sql = "SELECT * FROM user WHERE id = 1"
        sql = "SELECT * FROM user WHERE id BETWEEN 1 AND 10"
        cursor.execute(sql)
        # fetchall() คือ method ที่นำข้อมูลออกมาเก็บในตัวเเปล
        results = cursor.fetchall()
        for row in results:
        # "for row in results",loop เเต่ละเเถวจากตัวเเปล results เก็บไว้ในตัวเเปล
        # row ในรูปเเบบ Array
            print(row[0],'\t',row[1],row[2])
    except:
        print("Error")
showuse()
db.close()

#Cr.PuemMTH("กูเอง")
