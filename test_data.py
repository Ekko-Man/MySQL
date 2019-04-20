from app import db
from app.models import User, Post, Product, ProductMysqlServer, ProductXDevAPI, ProductMySQLNDBCluster, \
    EnterpriseDownload, ClusterDownload, MySQLCommunity, Topic, TopicGeneral, TopicAdministrator_Guides, \
    TopicHA_Scalability, Windows, ForumsTopic, ForumsPost, ForumsPostContect
from datetime import datetime, timedelta
import unittest

db.session.remove()
db.drop_all()
db.create_all()

# ---------------------------DOCUMENTATION---------------------------
p1 = Product(title="MysqlServer")
p2 = Product(title="XDevAPI")
p3 = Product(title="MySQLNDBCluster")

pm1 = ProductMysqlServer(url="https://dev.mysql.com/doc/refman/8.0/en/", name="MySQL8.0ReferenceManual",
                         title_id="MysqlServer")
pm2 = ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.7/en/", name="MySQL 5.7 Reference Manual",
                         title_id="MysqlServer")
pm3 = ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.6/en/", name="MySQL 5.6 Reference Manual",
                         title_id="MysqlServer")
pm4 = ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.6/ja/", name="MySQL 5.6 Reference Manual (Japanese)",
                         title_id="MysqlServer")
pm5 = ProductMysqlServer(url="https://dev.mysql.com/doc/refman/5.5/en/", name="MySQL 5.5 Reference Manual",
                         title_id="MysqlServer")

px1 = ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-cpp/8.0/",
                     name="MySQL Connector/C++ X DevAPI Reference", title_id="XDevAPI")
px2 = ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-j/8.0/", name="MySQL Connector/J X DevAPI Reference",
                     title_id="XDevAPI")
px3 = ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-net/8.0/",
                     name="MySQL Connector/NET X DevAPI Reference", title_id="XDevAPI")
px4 = ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-nodejs/8.0/",
                     name="MySQL Connector/Node.js X DevAPI Reference", title_id="XDevAPI")
px5 = ProductXDevAPI(url="https://dev.mysql.com/doc/dev/connector-python/8.0/",
                     name="MySQL Connector/Python X DevAPI Reference", title_id="XDevAPI")

pc1 = ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/ndbapi/en/", name="NDB Cluster API Developer Guide",
                             title_id="MySQLNDBCluster")
pc2 = ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/ndb-internals/en/index.html",
                             name="NDB Cluster Internals Manual", title_id="MySQLNDBCluster")
pc3 = ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/ndbapi/en/ndbmemcache.html",
                             name="memcache and NDB Cluster", title_id="MySQLNDBCluster")
pc4 = ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/mysql-cluster-manager/1.4/en/",
                             name="MySQL Cluster Manager 1.4", title_id="MySQLNDBCluster")
pc5 = ProductMySQLNDBCluster(url="https://dev.mysql.com/doc/mysql-cluster-manager/1.3/en/",
                             name="MySQL Cluster Manager 1.3", title_id="MySQLNDBCluster")

down1 = EnterpriseDownload(name='MySQLDatabase', MainID=2)
down2 = EnterpriseDownload(name='MySQL Storage Engines (InnoDB, MyISAM, etc.)', MainID=2)
down3 = EnterpriseDownload(name='MySQL Connectors (JDBC, ODBC, .Net, etc.)', MainID=2)
down4 = EnterpriseDownload(name='MySQL Replication', MainID=2)
down5 = EnterpriseDownload(name='MySQL Partitioning', MainID=2)
down6 = EnterpriseDownload(name='MySQL Utilities', MainID=2)
down7 = EnterpriseDownload(name='MySQL Workbench', MainID=2)
down8 = EnterpriseDownload(name='MySQL Enterprise Backup', MainID=2)
down9 = EnterpriseDownload(name='MySQL Enterprise Monitor', MainID=2)

down10 = ClusterDownload(name='MySQL Cluster', MainID=2)
down11 = ClusterDownload(name='MySQL Cluster Manager', MainID=2)
down12 = ClusterDownload(name='Plus, everything in MySQL Enterprise Edition', MainID=2)

com1 = MySQLCommunity(name='MySQL Community Server', version='(Current Generally Available Release: 8.0.15)',
                      description='MySQL Community Server is the world most popular open source database.',
                      com_link='#', MainID=2)
com2 = MySQLCommunity(name='MySQL Cluster', version='(Current Generally Available Release: 7.6.9)',
                      description='MySQL Cluster is a real-time, open source transactional database.',
                      com_link='#', MainID=2)
com3 = MySQLCommunity(name='MySQL Router', version='(Current Generally Available Release: 8.0.15)',
                      description='MySQL Router is lightweight middleware that provides transparent routing between your application and any backend MySQL Servers.',
                      com_link='#', MainID=2)

win1 = Windows(name='MySQL Installer',
               description='MySQL Installer provides an easy to use, wizard-based installation experience for all MySQL software on Windows.',
               win_link='#')
win2 = Windows(name='MySQL Connectors',
               description='MySQL offers industry standard database driver connectivity for using MySQL with applications and tools.',
               win_link='#')
win3 = Windows(name='MySQL Workbench',
               description='MySQL Workbench provides DBAs and developers an integrated tools environment for database design, administration, SQL development and database migration.',
               win_link='#')
win4 = Windows(name='MySQL for Excel',
               description='MySQL for Excel enables users to import, export and edit MySQL data using Microsoft Excel. Available with MySQL Installer.',
               win_link='#')
win5 = Windows(name='MySQL Notifier',
               description='MySQL Notifier enables developers and DBAs to easily monitor, start and stop MySQL database instances. Available with MySQL Installer.',
               win_link='#')
win6 = Windows(name='MySQL for Visual Studio',
               description='MySQL for Visual Studio provides access to MySQL objects and data using Visual Studio. Available with MySQL Installer.',
               win_link='#')

t1 = Topic(title="General")
t2 = Topic(title="Administrator Guides")
t3 = Topic(title="HA/Scalability")

tg1 = TopicGeneral(url="https://dev.mysql.com/doc/refman/8.0/en/server-administration.html",
                   name="Server Administration", title_id="General")
tg2 = TopicGeneral(url="https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html", name="SQL Syntax", title_id="General")
tg3 = TopicGeneral(url="https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html",
                   name="InnoDB Storage Engine", title_id="General")
tg4 = TopicGeneral(url="https://dev.mysql.com/doc/refman/8.0/en/storage-engines.html",
                   name="Alternative Storage Engines", title_id="General")

tag1 = TopicAdministrator_Guides(url="https://dev.mysql.com/doc/mysql-security-excerpt/8.0/en/index.html",
                                 name="Security", title_id="Administrator Guides")
tag2 = TopicAdministrator_Guides(url="https://dev.mysql.com/doc/mysql-secure-deployment-guide/8.0/en/index.html",
                                 name="Secure Deployment Guide", title_id="Administrator Guides")
tag3 = TopicAdministrator_Guides(url="https://dev.mysql.com/doc/mysql-startstop-excerpt/8.0/en/index.html",
                                 name="Startup / Shutdown", title_id="Administrator Guides")
tag4 = TopicAdministrator_Guides(url="https://dev.mysql.com/doc/mysql-backup-excerpt/8.0/en/index.html",
                                 name="Backup and Recovery Overview", title_id="Administrator Guides")

ts1 = TopicHA_Scalability(url="https://dev.mysql.com/doc/refman/8.0/en/mysql-innodb-cluster-userguide.html",
                          name="MySQL InnoDB cluster", title_id="HA/Scalability")
ts2 = TopicHA_Scalability(url="https://dev.mysql.com/doc/refman/en/ha-memcached.html", name="memcached",
                          title_id="HA/Scalability")
ts3 = TopicHA_Scalability(url="https://dev.mysql.com/doc/ndbapi/en/ndbmemcache.html", name="memcached with NDB Cluster",
                          title_id="HA/Scalability")
ts4 = TopicHA_Scalability(url="https://dev.mysql.com/doc/refman/en/innodb-memcached.html", name="memcached with InnoDB",
                          title_id="HA/Scalability")

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

db.session.add(com1)
db.session.add(com2)
db.session.add(com3)

db.session.add(win1)
db.session.add(win2)
db.session.add(win3)
db.session.add(win4)
db.session.add(win5)
db.session.add(win6)

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)

db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)
db.session.add(tag4)

db.session.add(tg1)
db.session.add(tg2)
db.session.add(tg3)
db.session.add(tg4)

db.session.add(ts1)
db.session.add(ts2)
db.session.add(ts3)
db.session.add(ts4)

# ---------------------------DOCUMENTATION---------------------------

# ---------------------------DeveloperZone---------------------------
ft1 = ForumsTopic(name="Announcements", description="MySQL related Product and Service announcements.",
                  url="ForumsTopic/Announcements", type="Forums")
ft2 = ForumsTopic(name="Perl", description="Forum for MySQL and Perl.", url="ForumsTopic/Perl", type="Languages")
ft3 = ForumsTopic(name="PHP", description="Forum for MySQL and PHP.", url="ForumsTopic/PHP", type="Languages")
ft4 = ForumsTopic(name="Ruby", description="Forum for MySQL and Ruby", url="ForumsTopic/Ruby", type="Languages")
ft5 = ForumsTopic(name="InnoDB", description="Forum for InnoDB Storage Engine.", url="ForumsTopic/InnoDB",
                  type="Storage Engines")
ft6 = ForumsTopic(name="MyISAM", description="Forum for MyISAM Storage Engine.", url="ForumsTopic/MyISAM",
                  type="Storage Engines")

db.session.add(ft1)
db.session.add(ft2)
db.session.add(ft3)
db.session.add(ft4)
db.session.add(ft5)
db.session.add(ft6)
# ---------------------------DeveloperZone---------------------------


db.session.commit()
