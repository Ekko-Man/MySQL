from app import app, db
from app.models import User, Post, ForumsTopic, ForumsPost, ForumsPostContect,\
    Product, Topic, ProductMysqlServer, ProductXDevAPI, ProductMySQLNDBCluster,\
    TopicGeneral, TopicAdministrator_Guides, TopicHA_Scalability,\
    Mainbar, MySQLBar, DownloadBar, DocumentBar, DZBar,\
    Newdownload,EnterpriseDownload,ClusterDownload,\
    MySQLCommunity, Windows, Language,\
    index_product, Product_Enterprise, Product_SqlClound, Product_Cluster, ProductForOME,\
    CustomerLogo



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,\
            'ForumsTopic': ForumsTopic, 'ForumsPost': ForumsPost, 'ForumsPostContect': ForumsPostContect\
            'Product': Product, 'Topic':Topic , \
            'ProductMysqlServer': ProductMysqlServer, 'ProductXDevAPI': ProductXDevAPI, 'ProductMySQLNDBCluster': ProductMySQLNDBCluster,\
            'TopicGeneral': TopicGeneral, 'TopicAdministrator_Guides': TopicAdministrator_Guides, 'TopicHA_Scalability': TopicHA_Scalability,\
            'Mainbar': Mainbar, 'MySQLBar': MySQLBar, 'DownloadBar': DownloadBar,\
            'DocumentBar': DocumentBar, 'DZBar': DZBar, \
            'Newdownload':Newdownload, 'EnterpriseDownload': EnterpriseDownload, 'ClusterDownload': ClusterDownload,\
            'MySQLCommunity': MySQLCommunity, 'Windows':Windows, 'Language': Language,\
            'index_product': index_product, 'Product_Enterprise': Product_Enterprise,\
            'Product_SqlClound': Product_SqlClound, 'Product_Cluster': Product_Cluster,\
            'ProductForOME': ProductForOME,'CustomerLogo': CustomerLogo}
