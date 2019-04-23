from datetime import datetime, timedelta
from flask import render_template, flash, redirect, url_for, request, make_response
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, \
    ResetPasswordRequestForm, ResetPasswordForm, ForumsPostReplyForm
from app.models import User, ProductMysqlServer, ProductXDevAPI, ProductMySQLNDBCluster, EnterpriseDownload, \
    ClusterDownload, MySQLCommunity, TopicGeneral, TopicAdministrator_Guides, TopicHA_Scalability, Windows, ForumsTopic, \
    ForumsPost, ForumsPostContect, Mainbar, MySQLBar, DownloadBar, DocumentBar, DZBar, index_product, \
    Product_Enterprise, \
    Product_Cluster, ProductForOME, Product_SqlClound, CustomerLogo

from app.email import send_password_reset_email


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/', methods=['GET'])
def index():
    MysqlOptions = index_product.query.filter_by(id=1)
    MysqlOptions2 = index_product.query.filter_by(id=2)
    MysqlOptions3 = index_product.query.filter_by(id=3)
    MysqlOptions4 = index_product.query.filter_by(id=4)
    customer = CustomerLogo.query.all()
    mainbarquery = Mainbar.query.all()
    mysqlquery = MySQLBar.query.all()
    return render_template('MYSQLCOM/index.html', title='Home', MysqlOptions=MysqlOptions, MysqlOptions2=MysqlOptions2,
                           MysqlOptions3=MysqlOptions3, MysqlOptions4=MysqlOptions4, customer=customer,
                           mainbarquery=mainbarquery, mysqlquery=mysqlquery)


@app.route('/index', methods=['GET'])
def indexs():
    mainbarquery = Mainbar.query.all()
    mysqlquery = MySQLBar.query.all()
    return render_template('MYSQLCOM/index.html', title='Home', mainbarquery=mainbarquery, mysqlquery=mysqlquery)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    mainbarquery = Mainbar.query.all()
    return render_template('Login/login.html', title='Sign In', form=form, mainbarquery=mainbarquery)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    mainbarquery = Mainbar.query.all()
    return render_template('Login/register.html', title='Register', form=form, mainbarquery=mainbarquery)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    mainbarquery = Mainbar.query.all()
    return render_template('Login/reset_password_request.html',
                           title='Reset Password', form=form, mainbarquery=mainbarquery)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    mainbarquery = Mainbar.query.all()
    return render_template('Login/reset_password.html', form=form, mainbarquery=mainbarquery)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    mainbarquery = Mainbar.query.all()
    return render_template('user.html', user=user, mainbarquery=mainbarquery)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    mainbarquery = Mainbar.query.all()
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form, mainbarquery=mainbarquery)


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    mainbarquery = Mainbar.query.all()
    return redirect(url_for('user', username=username), mainbarquery=mainbarquery)


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    mainbarquery = Mainbar.query.all()
    return redirect(url_for('user', username=username), mainbarquery=mainbarquery)


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['username']
    resp = make_response(render_template('readcookie.html'))
    expire = datetime.now()
    expire = expire + timedelta(seconds=60000)
    resp.set_cookie('userID', user, expires=expire)
    resp.set_cookie('secureUserID', user, expires=expire, secure=True)
    resp.set_cookie('httpOnlyUserID', user, expires=expire, httponly=True)
    return resp


@app.route('/getcookie')
def getcookie():
    userID = request.cookies.get('userID') or ''
    secureUserID = request.cookies.get('secureUserID') or ''
    httpOnlyUserID = request.cookies.get('httpOnlyUserID') or ''
    return f"""
<h1>userID: {userID} </h1>
<h1>secureUserID: {secureUserID} </h1>
<h1>httpOnlyUserID: {httpOnlyUserID} </h1>   
"""


@app.route('/documentation')
def documentation():
    docquery = DocumentBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template('Documentation/documentation.html', title="documentation", docquery=docquery,
                           mainbarquery=mainbarquery)


@app.route('/documentation/product')
def product():
    server = ProductMysqlServer.query.all()
    api = ProductXDevAPI.query.all()
    pc = ProductMySQLNDBCluster.query.all()
    docquery = DocumentBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template('Documentation/product 2.html', title="Product", server=server, api=api, pc=pc,
                           docquery=docquery, mainbarquery=mainbarquery)


@app.route('/documentation/topic')
def topic():
    general = TopicGeneral.query.all()
    admin = TopicAdministrator_Guides.query.all()
    ha = TopicHA_Scalability.query.all()
    docquery = DocumentBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template('Documentation/topic.html', title="Topic", general=general, admin=admin, ha=ha,
                           docquery=docquery, mainbarquery=mainbarquery)


@app.route('/Download')
def enterprise():
    enterquery = EnterpriseDownload.query.all()
    clusterquery = ClusterDownload.query.all()
    downquery = DownloadBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template('Download/enterprise.html', title="Enterprise", enterquery=enterquery,
                           clusterquery=clusterquery, downquery=downquery, mainbarquery=mainbarquery)


@app.route('/Download/community')
def community():
    comquery = MySQLCommunity.query.all()
    downquery = DownloadBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template('Download/community.html', title="Community", comquery=comquery, downquery=downquery,
                           mainbarquery=mainbarquery)


@app.route('/Download/windows')
def windows():
    winquery = Windows.query.all()
    mainbarquery = Mainbar.query.all()
    downquery = DownloadBar.query.all()
    return render_template('Download/windows.html', title="Windows", winquery=winquery, downquery=downquery,
                           mainbarquery=mainbarquery)


@app.route('/MySQLCOM/Enterprise')
def MysqlProduct():
    EnterpriseDropDown = Product_Enterprise.query.all()
    ClusterDropDown = Product_Cluster.query.all()
    OEMDropDown = ProductForOME.query.all()
    mainbarquery = Mainbar.query.all()
    mysqlquery = MySQLBar.query.all()
    return render_template('MySQLCOM/MySQL_Enterprise.html', title='Enterprise', EnterpriseDropDown=EnterpriseDropDown,
                           OEMDropDown=OEMDropDown, ClusterDropDown=ClusterDropDown, mysqlquery=mysqlquery,
                           mainbarquery=mainbarquery)


@app.route('/MySQLCOM/Cloud')
def MysqlCloud():
    EnterpriseDropDown = Product_Enterprise.query.all()
    ClusterDropDown = Product_Cluster.query.all()
    OEMDropDown = ProductForOME.query.all()
    cloudbutton = Product_SqlClound.query.filter_by(id=2)
    cloudbutton2 = Product_SqlClound.query.filter_by(id=3)
    mysqlquery = MySQLBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template('MySQLCOM/MySQL_Cloud.html', title='Cloud', EnterpriseDropDown=EnterpriseDropDown,
                           OEMDropDown=OEMDropDown, ClusterDropDown=ClusterDropDown, cloudbutton=cloudbutton,
                           cloudbutton2=cloudbutton2, mysqlquery=mysqlquery, mainbarquery=mainbarquery)


@app.route('/developerzone')
def developerzone():
    dzquery = DZBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template("DeveloperZone/developerzone.html", title="developerzone", dzquery=dzquery,
                           mainbarquery=mainbarquery)


@app.route('/forums')
def forums():
    typeforums = ForumsTopic.query.filter_by(type='Forums').all()
    typelanguages = ForumsTopic.query.filter_by(type='Languages').all()
    typestorage = ForumsTopic.query.filter_by(type='Storage Engines').all()
    dzquery = DZBar.query.all()
    mainbarquery = Mainbar.query.all()
    return render_template("DeveloperZone/forums.html", title="forums", forums=typeforums, languages=typelanguages,
                           storages=typestorage, dzquery=dzquery, mainbarquery=mainbarquery)


@app.route('/forumstopic/<topictype>')
def forumstopic(topictype):
    if current_user.is_authenticated:
        supertopic = ForumsTopic.query.filter_by(name=f'{topictype}').first()
        if supertopic is None:
            flash("What are u doing? We don't have this TOPIC!!!!!  GOOD BYE")
            return redirect(url_for('index'))
        idd = supertopic.id
        data = ForumsPost.query.filter_by(topic_id=f'{str(idd)}').all()
        writerlist = []
        for dada in data:
            writerquery = User.query.filter_by(id=f'{dada.writer_id}').first()
            writerlist.append(writerquery.username)
        superdata = zip(data, writerlist)
        dzquery = DZBar.query.all()
        mainbarquery = Mainbar.query.all()
        return render_template('DeveloperZone/supertopic.html', dzquery=dzquery, mainbarquery=mainbarquery, \
                               superdata=superdata, topictype=topictype)
    elif not current_user.is_authenticated:
        supertopic = ForumsTopic.query.filter_by(name=f'{topictype}').first()
        if supertopic is None:
            flash("What are u doing? We don't have this TOPIC!!!!!  GOOD BYE")
            return redirect(url_for('index'))
        idd = supertopic.id
        data = ForumsPost.query.filter_by(topic_id=f'{str(idd)}').all()
        writerlist = []
        for dada in data:
            writerquery = User.query.filter_by(id=f'{dada.writer_id}').first()
            writerlist.append(writerquery.username)
        superdata = zip(data, writerlist)
        dzquery = DZBar.query.all()
        mainbarquery = Mainbar.query.all()
        return render_template('DeveloperZone/supertopic.html', dzquery=dzquery, mainbarquery=mainbarquery, \
                               superdata=superdata, topictype=topictype)


@app.route('/forumspost/<postid>', methods=['GET', 'POST'])
def forumspost(postid):
    if current_user.is_authenticated:
        postdata = ForumsPost.query.filter_by(id=f'{str(postid)}').first()
        if postdata is None:
            flash("What are u doing? We don't have this POST!!!!!  GOOD BYE")
            return redirect(url_for('index'))
        topicdata = ForumsTopic.query.filter_by(id=f'{str(postdata.topic_id)}').first()
        writer = User.query.filter_by(id=f'{postdata.writer_id}').first()
        postcontect = ForumsPostContect.query.filter_by(post_id=f'{str(postid)}').all()
        writerlist = []
        for dada in postcontect:
            writerquery = User.query.filter_by(id=f'{dada.writer_id}').first()
            writerlist.append(writerquery.username)
        superpostcontect = zip(postcontect, writerlist)
        form = ForumsPostReplyForm()
        if form.validate_on_submit():
            post = ForumsPostContect(contect=form.postcontect.data, post_id=postid, postcontectauthor=current_user)
            db.session.add(post)
            db.session.commit()
            flash('You were replied!')
            return redirect(url_for('forumspost', postid=postid))
        dzquery = DZBar.query.all()
        mainbarquery = Mainbar.query.all()
        return render_template('DeveloperZone/forumspost.html', dzquery=dzquery, mainbarquery=mainbarquery, \
                               topicdata=topicdata, postdata=postdata, writer=writer, superpostcontect=superpostcontect \
                               , form=form)
    elif not current_user.is_authenticated:
        postdata = ForumsPost.query.filter_by(id=f'{str(postid)}').first()
        if postdata is None:
            flash("What are u doing? We don't have this POST!!!!!  GOOD BYE")
            return redirect(url_for('index'))
        topicdata = ForumsTopic.query.filter_by(id=f'{str(postdata.topic_id)}').first()
        writer = User.query.filter_by(id=f'{postdata.writer_id}').first()
        postcontect = ForumsPostContect.query.filter_by(post_id=f'{str(postid)}').all()
        writerlist = []
        for dada in postcontect:
            writerquery = User.query.filter_by(id=f'{dada.writer_id}').first()
            writerlist.append(writerquery.username)
        superpostcontect = zip(postcontect, writerlist)
        dzquery = DZBar.query.all()
        mainbarquery = Mainbar.query.all()
        return render_template('DeveloperZone/forumspost.html', dzquery=dzquery, mainbarquery=mainbarquery, \
                               topicdata=topicdata, postdata=postdata, writer=writer, superpostcontect=superpostcontect)
