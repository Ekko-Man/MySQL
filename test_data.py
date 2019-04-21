from app import db
from app.models import User, Post, Product, ProductMysqlServer, ProductXDevAPI, ProductMySQLNDBCluster, \
    EnterpriseDownload, ClusterDownload, MySQLCommunity, Topic, TopicGeneral, TopicAdministrator_Guides, \
    TopicHA_Scalability, Windows, index_product, Product_Cluster, Product_Enterprise, Product_SqlClound, \
    ProductForOME, CustomerLogo, TopicHA_Scalability, Windows, ForumsTopic, ForumsPost, ForumsPostContect, Mainbar, MySQLBar, DownloadBar, DocumentBar, DZBar

from datetime import datetime, timedelta
import unittest

db.session.remove()
db.drop_all()
db.create_all()

testUser1 = User(username='Cyrus', email='cyrus@example.com')
testUser2 = User(username='Kitson', email='kitson@example.com')
testUser3 = User(username='Jeff Bezos', email='jeff@example.com')
testUser4 = User(username='Bill Gates', email='gaygay@example.com')
testUser5 = User(username='Steve Jobs', email='apple@example.com')
testUser6 = User(username='Thomas Edison', email='edison@example.com')

db.session.add(testUser1)
db.session.add(testUser2)
db.session.add(testUser3)
db.session.add(testUser4)
db.session.add(testUser5)
db.session.add(testUser6)

# ---------------------------MainBar-------------------------------
M1 = Mainbar(Name='MYSQL.COM', url='/index')
M2 = Mainbar(Name='DOWNLOADS', url='/Download')
M3 = Mainbar(Name='DOCUMENTATION', url='/documentation')
M4 = Mainbar(Name='DEVELOPER ZONE', url='/developerzone')

# ---------------------------SubBar---------------------------------
My1 = MySQLBar(Name='Products', url='#', MainID=1)
My2 = MySQLBar(Name='Cloud', url='#', MainID=1)
My3 = MySQLBar(Name='Services', url='#', MainID=1)
My4 = MySQLBar(Name='Partners', url='#', MainID=1)
My5 = MySQLBar(Name='Customers', url='#', MainID=1)
My6 = MySQLBar(Name='Why MySQL?', url='#', MainID=1)
My7 = MySQLBar(Name='News & Events', url='#', MainID=1)
My8 = MySQLBar(Name='How to Buy', url='#', MainID=1)

Down1 = DownloadBar(Name='Enterprise', url='/Download', MainID=2)
Down2 = DownloadBar(Name='Community', url='/Download/community', MainID=2)
Down3 = DownloadBar(Name='Yum Repository', url='#', MainID=2)
Down4 = DownloadBar(Name='APT Repository', url='#', MainID=2)
Down5 = DownloadBar(Name='SUSE Repository', url='#', MainID=2)
Down6 = DownloadBar(Name='Windows', url='Download/windows.html', MainID=2)
Down7 = DownloadBar(Name='Archives', url='#', MainID=2)

Doc1 = DocumentBar(Name='MySQL Server', url='#', MainID=3)
Doc2 = DocumentBar(Name='MySQL Enterprise', url='#', MainID=3)
Doc3 = DocumentBar(Name='Workbench', url='#', MainID=3)
Doc4 = DocumentBar(Name='InnoDB Cluster', url='#', MainID=3)
Doc5 = DocumentBar(Name='MySQL NDB Cluster', url='#', MainID=3)
Doc6 = DocumentBar(Name='Connectors', url='#', MainID=3)
Doc7 = DocumentBar(Name='More', url='#', MainID=3)

DZ1 = DZBar(Name='Forums', url='forums', MainID=4)
DZ2 = DZBar(Name='Bugs', url='https://bugs.mysql.com/', MainID=4)
DZ3 = DZBar(Name='Worklog', url='https://dev.mysql.com/worklog/', MainID=4)
DZ4 = DZBar(Name='Labs', url='https://labs.mysql.com/', MainID=4)
DZ5 = DZBar(Name='Planet MySQL', url='https://planet.mysql.com/', MainID=4)
DZ6 = DZBar(Name='News and Events', url='https://www.mysql.com/news-and-events/web-seminars/', MainID=4)
DZ7 = DZBar(Name='Community', url='https://dev.mysql.com/community/', MainID=4)

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

# ------------------------------Download----------------------------

down1 = EnterpriseDownload(name='MySQLDatabase', MainID=1)
down2 = EnterpriseDownload(name='MySQL Storage Engines (InnoDB, MyISAM, etc.)', MainID=1)
down3 = EnterpriseDownload(name='MySQL Connectors (JDBC, ODBC, .Net, etc.)', MainID=1)
down4 = EnterpriseDownload(name='MySQL Replication', MainID=1)
down5 = EnterpriseDownload(name='MySQL Partitioning', MainID=1)
down6 = EnterpriseDownload(name='MySQL Utilities', MainID=1)
down7 = EnterpriseDownload(name='MySQL Workbench', MainID=1)
down8 = EnterpriseDownload(name='MySQL Enterprise Backup', MainID=1)
down9 = EnterpriseDownload(name='MySQL Enterprise Monitor', MainID=1)

down10 = ClusterDownload(name='MySQL Cluster', MainID=1)
down11 = ClusterDownload(name='MySQL Cluster Manager', MainID=1)
down12 = ClusterDownload(name='Plus, everything in MySQL Enterprise Edition', MainID=1)

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
               win_link='#', MainID=6)
win2 = Windows(name='MySQL Connectors',
               description='MySQL offers industry standard database driver connectivity for using MySQL with applications and tools.',
               win_link='#', MainID=6)
win3 = Windows(name='MySQL Workbench',
               description='MySQL Workbench provides DBAs and developers an integrated tools environment for database design, administration, SQL development and database migration.',
               win_link='#', MainID=6)
win4 = Windows(name='MySQL for Excel',
               description='MySQL for Excel enables users to import, export and edit MySQL data using Microsoft Excel. Available with MySQL Installer.',
               win_link='#', MainID=6)
win5 = Windows(name='MySQL Notifier',
               description='MySQL Notifier enables developers and DBAs to easily monitor, start and stop MySQL database instances. Available with MySQL Installer.',
               win_link='#', MainID=6)
win6 = Windows(name='MySQL for Visual Studio',
               description='MySQL for Visual Studio provides access to MySQL objects and data using Visual Studio. Available with MySQL Installer.',
               win_link='#', MainID=6)

# ----------------------Download----------------------------------

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
# ---------------------------MySQL---------------------------
IP1 = index_product(producttitle="MySQL Enterprise Edition", url='/MySQLCOM/Enterprise')
IP2 = index_product(producttitle="Oracle MySQL cloud Service", url='/MySQLCOM/Cloud')
IP3 = index_product(producttitle="MySQL Cluster CGE", url='https://www.mysql.com/products/cluster/')
IP4 = index_product(producttitle="MySQL for OEM/ISV", url='https://www.mysql.com/oem/')

PE1 = Product_Enterprise(name="MySQL Enterprise Edition", url="https://www.mysql.com/products/enterprise/", indexID=1)
PE2 = Product_Enterprise(name="MySQL Technical Specifications",
                         url="https://www.mysql.com/products/enterprise/techspec.html", indexID=1)
PE3 = Product_Enterprise(name="MySQL Database", url="https://www.mysql.com/products/enterprise/database/", indexID=1)
PE4 = Product_Enterprise(name="MySQL Document Store",
                         url="https://www.mysql.com/products/enterprise/document_store.html", indexID=1)

SQLC1 = Product_SqlClound(name="MySQL Cloud Service", url="https://www.mysql.com/cloud/", indexID=2)
SQLC2 = Product_SqlClound(name="Learn More", url="https://cloud.oracle.com/mysql", indexID=2)
SQLC3 = Product_SqlClound(name="Analyst Report",
                          url="https://www.mysql.com/why-mysql/white-papers/constellation-research-report-enterprise-class-mysql-meets-oracle-cloud/",
                          indexID=2)

CGE1 = Product_Cluster(name="Cluster CGE", url="https://www.mysql.com/products/cluster/", indexID=3)
CGE2 = Product_Cluster(name="Features & Benefits", url="https://www.mysql.com/products/cluster/features.html",
                       indexID=3)
CGE3 = Product_Cluster(name="Scalability", url="https://www.mysql.com/products/cluster/scalability.html", indexID=3)
CGE4 = Product_Cluster(name="High Availability", url="https://www.mysql.com/products/cluster/availability.html",
                       indexID=3)

OEM1 = ProductForOME(name="Embedded", url="https://www.mysql.com/oem/", indexID=4)
OEM2 = ProductForOME(name="Commercial License", url="https://www.mysql.com/about/legal/licensing/oem/", indexID=4)
OEM3 = ProductForOME(name="MySQL Customers", url="https://www.mysql.com/customers/", indexID=4)

CTR1 = CustomerLogo(name="YouTube", urlForimage="https://www.youtube.com/yts/img/yt_1200-vfl4C3T0K.png",
                    url="https://www.youtube.com/", indexID=5)
CTR2 = CustomerLogo(name="PayPal",
                    urlForimage="https://www.jobs.ie/job-talk/wp-content/uploads/PayPal-Header--720x480.jpg",
                    url="https://www.paypal.com/hk/home", indexID=5)
CTR3 = CustomerLogo(name="Google",
                    urlForimage="https://cdn.vox-cdn.com/thumbor/L1PZnV6wQVZGZJqQU0rxJGfAV1U=/0x0:2040x1360/1200x800/filters:focal(443x747:769x1073)/cdn.vox-cdn.com/uploads/chorus_image/image/59226439/jbareham_170504_1691_0004.0.0.jpg",
                    url="https://www.google.com", indexID=5)
CTR4 = CustomerLogo(name="facebook",
                    urlForimage="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Facebook_New_Logo_%282015%29.svg/2000px-Facebook_New_Logo_%282015%29.svg.png",
                    url="https://www.facebook.com", indexID=5)
CTR5 = CustomerLogo(name="twitter", urlForimage="https://www.cbronline.com/wp-content/uploads/2016/06/twitter2.png",
                    url="https://www.twitter.com", indexID=5)
CTR6 = CustomerLogo(name="ebay",
                    urlForimage="data:image/png;base64,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",
                    url="https://www.ebay.com", indexID=5)

db.session.add(M1)
db.session.add(M2)
db.session.add(M3)
db.session.add(M4)

db.session.add(My1)
db.session.add(My2)
db.session.add(My3)
db.session.add(My4)
db.session.add(My5)
db.session.add(My6)
db.session.add(My7)
db.session.add(My8)

db.session.add(Down1)
db.session.add(Down2)
db.session.add(Down3)
db.session.add(Down4)
db.session.add(Down5)
db.session.add(Down6)
db.session.add(Down7)

db.session.add(Doc1)
db.session.add(Doc2)
db.session.add(Doc3)
db.session.add(Doc4)
db.session.add(Doc5)
db.session.add(Doc6)
db.session.add(Doc7)

db.session.add(DZ1)
db.session.add(DZ2)
db.session.add(DZ3)
db.session.add(DZ4)
db.session.add(DZ5)
db.session.add(DZ6)
db.session.add(DZ7)

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

# ---------------------------MySQL---------------------------
db.session.add(IP1)
db.session.add(IP2)
db.session.add(IP3)
db.session.add(IP4)

db.session.add(PE1)
db.session.add(PE2)
db.session.add(PE3)
db.session.add(PE4)

db.session.add(SQLC1)
db.session.add(SQLC2)
db.session.add(SQLC3)

db.session.add(CGE1)
db.session.add(CGE2)
db.session.add(CGE3)
db.session.add(CGE4)

db.session.add(OEM1)
db.session.add(OEM2)
db.session.add(OEM3)

db.session.add(CTR1)
db.session.add(CTR2)
db.session.add(CTR3)
db.session.add(CTR4)
db.session.add(CTR5)
db.session.add(CTR6)
# ---------------------------MySQL---------------------------

# ---------------------------DeveloperZone---------------------------
ft1 = ForumsTopic(name="Announcements", description="MySQL related Product and Service announcements.",
                  url="forumstopic/Announcements", type="Forums")
ft2 = ForumsTopic(name="Perl", description="Forum for MySQL and Perl.", url="forumstopic/Perl", type="Languages")
ft3 = ForumsTopic(name="PHP", description="Forum for MySQL and PHP.", url="forumstopic/PHP", type="Languages")
ft4 = ForumsTopic(name="Ruby", description="Forum for MySQL and Ruby", url="forumstopic/Ruby", type="Languages")
ft5 = ForumsTopic(name="InnoDB", description="Forum for InnoDB Storage Engine.", url="forumstopic/InnoDB",
                  type="Storage Engines")
ft6 = ForumsTopic(name="MyISAM", description="Forum for MyISAM Storage Engine.", url="forumstopic/MyISAM",
                  type="Storage Engines")

db.session.add(ft1)
db.session.add(ft2)
db.session.add(ft3)
db.session.add(ft4)
db.session.add(ft5)
db.session.add(ft6)

fp11 = ForumsPost(subject="MySQL Enterprise Backup 3.12.4 has been released", url="/forumspost/1", topic_id="1", writer_id="1")
fp12 = ForumsPost(subject="MySQL Enterprise Backup 4.1.3 has been released", url="/forumspost/2", topic_id="1", writer_id="2")
fp13 = ForumsPost(subject="MySQL Enterprise Backup 8.0.15 has been released", url="/forumspost/3", topic_id="1", writer_id="3")

fp21 = ForumsPost(subject="MySQL and Perl: Articles, Blogs, Docs", url="/forumspost/4", topic_id="2", writer_id="4")
fp22 = ForumsPost(subject="DBIx::MyServer - Perl module that implements MySQL client/server protocol", url="/forumspost/5", topic_id="2", writer_id="5")
fp23 = ForumsPost(subject="Can't connect to mysql from MAMP Perl", url="/forumspost/6", topic_id="2", writer_id="6")

fp31 = ForumsPost(subject="MySQL 8.0: X DevAPI PHP Extension", url="/forumspost/7", topic_id="3", writer_id="3")
fp32 = ForumsPost(subject="MySQL Workbench: Plugins for PHP development", url="/forumspost/8", topic_id="3", writer_id="4")
fp33 = ForumsPost(subject="Upgrading from MyISAM to InnoDB", url="/forumspost/9", topic_id="3", writer_id="5")

fp41 = ForumsPost(subject="Ruby and MySQL: Articles, Blogs, FAQs", url="/forumspost/10", topic_id="4", writer_id="1")
fp42 = ForumsPost(subject="Permission denied", url="/forumspost/11", topic_id="4", writer_id="2")
fp43 = ForumsPost(subject="MySQL Evolution - From 5.6 to 8.0 -- plus Ruby on Rails", url="/forumspost/12", topic_id="4", writer_id="6")

fp51 = ForumsPost(subject="MySQL 8.0: InnoDB New Lock free, scalable WAL design", url="/forumspost/13", topic_id="5", writer_id="2")
fp52 = ForumsPost(subject="MySQL 8.0: Instant ADD COLUMN for InnoDB", url="/forumspost/14", topic_id="5", writer_id="3")
fp53 = ForumsPost(subject="MySQL HA: InnoDB clusters", url="/forumspost/15", topic_id="5", writer_id="4")

fp61 = ForumsPost(subject="Meltdown Fix: 40% performance regression for MyISAM; recommend switch to InnoDB", url="/forumspost/16", topic_id="6", writer_id="5")
fp62 = ForumsPost(subject="MySQL: InnoDB -vs- MyISAM", url="/forumspost/17", topic_id="6", writer_id="6")
fp63 = ForumsPost(subject="MySQL 5.6: InnoDB Read-only Performance", url="/forumspost/18", topic_id="6", writer_id="1")

fpc1 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup v3.12.4, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

A brief summary of the changes in MySQL Enterprise Backup (MEB) 
version 3.12.4 is given below. 

Changes in MySQL Enterprise Backup 3.12.4 (2019-02-15) 

* Functionality Added or Changed 

* Bugs Fixed 

Functionality Added or Changed 
""", post_id="1")
fpc2 = ForumsPostContect(contect="""Plx,
subscribe pewdiepie !!!
""", post_id="1")
fpc3 = ForumsPostContect(contect="""Dear MySQL users,

MySQL Enterprise Backup v4.1.3, a new version of the MySQL backup tool, is
now available for download from the My Oracle Support (MOS) website
as our latest GA release. This release will be available on eDelivery (OSDC)
after the next upload cycle. MySQL Enterprise Backup is a commercial
extension to the MySQL family of products.

MySQL Enterprise Backup 4.1.3 only supports MySQL 5.7.
MySQL Enterprise Backup 3.12.4 only supports MySQL 5.6 and earlier.
MySQL Enterprise Backup 8.0 only supports MySQL 8.0.""", post_id="2")
fpc4 = ForumsPostContect(contect="""i have been backup already ^.^""", post_id="2")
fpc5 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12. """, post_id="3")
fpc6 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12. """, post_id="4")
fpc7 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12. """, post_id="5")
fpc8 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="6")
fpc9 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="7")
fpc10 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="8")
fpc11 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="9")
fpc12 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="10")
fpc13 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="11")
fpc14 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="12")
fpc15 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="13")
fpc16 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="14")
fpc17 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="15")
fpc18 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="16")
fpc19 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="17")
fpc20 = ForumsPostContect(contect="""Dear MySQL users, 

MySQL Enterprise Backup 8.0.15, a new version of the online MySQL backup 
tool, is now available for download from the My Oracle Support (MOS) website 
as our latest GA release. This release will be available on eDelivery (OSDC) 
after the next upload cycle. MySQL Enterprise Backup is a commercial 
extension to the MySQL family of products. 

MySQL Enterprise Backup 8.0.15 supports only the MySQL Server 8.0.15. 
For earlier versions of MySQL 8.0, use the MySQL Enterprise Backup 
version with the same version number as the server. For MySQL server 
5.7, please use MySQL Enterprise Backup 4.1 and for MySQL Server 5.6 
and 5.5, please use MySQL Enterprise Backup 3.12.""", post_id="18")
fpc21 = ForumsPostContect(contect="""I am so rich!""", post_id="1")
fpc22 = ForumsPostContect(contect="""I am so poor""", post_id="2")

db.session.add(fp11)
db.session.add(fp12)
db.session.add(fp13)

db.session.add(fp21)
db.session.add(fp22)
db.session.add(fp23)

db.session.add(fp31)
db.session.add(fp32)
db.session.add(fp33)

db.session.add(fp41)
db.session.add(fp42)
db.session.add(fp43)

db.session.add(fp51)
db.session.add(fp52)
db.session.add(fp53)

db.session.add(fp61)
db.session.add(fp62)
db.session.add(fp63)

db.session.add(fpc1)
db.session.add(fpc2)
db.session.add(fpc3)
db.session.add(fpc4)
db.session.add(fpc5)

db.session.add(fpc6)
db.session.add(fpc7)
db.session.add(fpc8)
db.session.add(fpc9)
db.session.add(fpc10)

db.session.add(fpc11)
db.session.add(fpc12)
db.session.add(fpc13)
db.session.add(fpc14)
db.session.add(fpc15)

db.session.add(fpc16)
db.session.add(fpc17)
db.session.add(fpc18)
db.session.add(fpc19)
db.session.add(fpc20)

db.session.add(fpc21)
db.session.add(fpc22)
# ---------------------------DeveloperZone---------------------------


db.session.commit()
