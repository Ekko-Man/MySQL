from app import db
from app.models import User, Post,Product,ProductMysqlServer,ProductXDevAPI,ProductMySQLNDBCluster
from datetime import datetime, timedelta
import unittest

db.session.remove()
db.drop_all()
db.create_all()


p1=Product(title="MysqlServer")
p2=Product(title="XDevAPI")
p3=Product(title="MySQLNDBCluster")

MySQL8_0ReferenceManual=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/8.0/en/",name="MySQL8_0ReferenceManual",title_id="MysqlServer")
MySQL5_7ReferenceManual=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.7/en/",name="MySQL 5.7 Reference Manual",title_id="MysqlServer")

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(MySQL8_0ReferenceManual)
db.session.add(MySQL5_7ReferenceManual)

db.session.commit()