from app import db
from app.models import User, Post,Product,ProductMysqlServer,ProductXDevAPI,ProductMySQLNDBCluster, Download
from datetime import datetime, timedelta
import unittest

db.session.remove()
db.drop_all()
db.create_all()


p1=Product(title="MysqlServer")
p2=Product(title="XDevAPI")
p3=Product(title="MySQLNDBCluster")


pm1=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/8.0/en/", name="MySQL8.0ReferenceManual", title_id="MysqlServer")
pm2=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.7/en/", name="MySQL 5.7 Reference Manual", title_id="MysqlServer")
pm3=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.6/en/",name="MySQL 5.6 Reference Manual",title_id="MysqlServer")
pm4=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.6/ja/",name="MySQL 5.6 Reference Manual (Japanese)",title_id="MysqlServer")
pm5=ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.5/en/",name="MySQL 5.5 Reference Manual",title_id="MysqlServer")

px1=ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-cpp/8.0/",name="MySQL Connector/C++ X DevAPI Reference",title_id="XDevAPI")
px2=ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-j/8.0/",name="MySQL Connector/J X DevAPI Reference",title_id="XDevAPI")
px3=ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-net/8.0/",name="MySQL Connector/NET X DevAPI Reference",title_id="XDevAPI")
px4=ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-nodejs/8.0/",name="MySQL Connector/Node.js X DevAPI Reference",title_id="XDevAPI")
px5=ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-python/8.0/",name="MySQL Connector/Python X DevAPI Reference",title_id="XDevAPI")

pc1=ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/ndbapi/en/",name="NDB Cluster API Developer Guide",title_id="MySQLNDBCluster")
pc2=ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/ndb-internals/en/index.html",name="NDB Cluster Internals Manual",title_id="MySQLNDBCluster")
pc3=ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/ndbapi/en/ndbmemcache.html",name="memcache and NDB Cluster",title_id="MySQLNDBCluster")
pc4=ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/mysql-cluster-manager/1.4/en/",name="MySQL Cluster Manager 1.4",title_id="MySQLNDBCluster")
pc5=ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/mysql-cluster-manager/1.3/en/",name="MySQL Cluster Manager 1.3",title_id="MySQLNDBCluster")

down1 = Download(Type='MySQL Enterprise Edition', name='MySQLDatabase', MainID=2)
down2 = Download(Type='MySQL Enterprise Edition', name='MySQL Storage Engines (InnoDB, MyISAM, etc.)', MainID=2)
down3 = Download(Type='MySQL Enterprise Edition', name='MySQL Connectors (JDBC, ODBC, .Net, etc.)', MainID=2)
down4 = Download(Type='MySQL Enterprise Edition', name='MySQL Replication', MainID=2)
down5 = Download(Type='MySQL Enterprise Edition', name='MySQL Partitioning', MainID=2)
down6 = Download(Type='MySQL Enterprise Edition', name='MySQL Utilities', MainID=2)
down7 = Download(Type='MySQL Enterprise Edition', name='MySQL Workbench', MainID=2)
down8 = Download(Type='MySQL Enterprise Edition', name='MySQL Enterprise Backup', MainID=2)
down9 = Download(Type='MySQL Enterprise Edition', name='MySQL Enterprise Monitor', MainID=2)

down10 = Download(Type='MySQL Enterprise Edition', name='MySQL Cluster', MainID=2)
down11 = Download(Type='MySQL Enterprise Edition', name='MySQL Cluster Manager', MainID=2)
down12 = Download(Type='MySQL Enterprise Edition', name='Plus, everything in MySQL Enterprise Edition', MainID=2)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)



db.session.add(pm1)
db.session.add(pm2)
db.session.add(pm3)
db.session.add(pm4)
db.session.add(pm5)

db.session.add(px1)
db.session.add(px2)
db.session.add(px3)
db.session.add(px4)
db.session.add(px5)

db.session.add(pc1)
db.session.add(pc2)
db.session.add(pc3)
db.session.add(pc4)
db.session.add(pc5)

db.session.add(down1)
db.session.add(down2)
db.session.add(down3)
db.session.add(down4)
db.session.add(down5)
db.session.add(down6)
db.session.add(down7)
db.session.add(down8)
db.session.add(down9)
db.session.add(down10)

db.session.add(down11)
db.session.add(down12)

db.session.commit()