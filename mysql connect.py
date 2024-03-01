import pymysql
db=pymysql.connect(host='localhost',user='root',password='pooja',database='school')
cursor=db.cursor()

insert_statement="insert into screen1(name,school,place) values(%s,%s,%s)"
name=input("enter your name:")
school=input("enter name of school:")
place=input("enter place :")
data=(name,school,place)
try:
    cursor.execute(insert_statement,data)

    db.commit()
    print("value inserted")
except:
    db.rollback()
    print("error")
db.close()
