from app import db
from app.models import User, Post,Product,ProductMysqlServer,ProductXDevAPI,ProductMySQLNDBCluster
from datetime import datetime, timedelta
import unittest

MysqlServer=Product(title="MysqlServer")
XDevAPI=Product(title="XDevAPI")
MySQLNDBCluster=Product(title="MySQLNDBCluster")

MySQL8_0ReferenceManual=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/8.0/en/",name="MySQL8_0ReferenceManual",title_id="MysqlServer")