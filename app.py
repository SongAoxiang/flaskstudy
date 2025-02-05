from flask import Flask,url_for,render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# 配置 MySQL 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy
db = SQLAlchemy(app)
migrate=Migrate


#定义用户模型
class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    password = db.Column(db.String(25))


# 定义电影模型
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 电影ID
    title = db.Column(db.String(100), nullable=False)  # 电影标题
    year = db.Column(db.String(4), nullable=False)  # 上映年份

# 创建数据库表
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    name=User.query.first().name
    movies=Movie.query.all()
    #return 'Welcome to My Watchlist!'
    return render_template('index.html',name=name,movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return f'User :{escape(name)}\'s website'

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'
#url_for() 是一个 自动生成 URL 的函数，
#它会根据 视图函数（即 Flask 里的路由处理函数）的名字 生成对应的 URL。
# name = '漫威电影宇宙'
# movies = [
#     {'title': '钢铁侠', 'year': '2008'},
#     {'title': '无敌浩克', 'year': '2008'},
#     {'title': '钢铁侠2', 'year': '2010'},
#     {'title': '雷神', 'year': '2011'},
#     {'title': '美国队长', 'year': '2011'},
#     {'title': '复仇者联盟', 'year': '2012'},
#     {'title': '钢铁侠3', 'year': '2013'},
#     {'title': '雷神2：黑暗世界', 'year': '2013'},
#     {'title': '美国队长2：冬日战士', 'year': '2014'},
#     {'title': '银河护卫队', 'year': '2014'},
#     {'title': '复仇者联盟2：奥创纪元', 'year': '2015'},
#     {'title': '蚁人', 'year': '2015'},
#     {'title': '美国队长3：内战', 'year': '2016'},
#     {'title': '奇异博士', 'year': '2016'},
#     {'title': '银河护卫队2', 'year': '2017'},
#     {'title': '蜘蛛侠：英雄归来', 'year': '2017'},
#     {'title': '雷神3：诸神黄昏', 'year': '2017'},
#     {'title': '黑豹', 'year': '2018'},
#     {'title': '复仇者联盟3：无限战争', 'year': '2018'},
#     {'title': '蚁人2：黄蜂女现身', 'year': '2018'},
#     {'title': '惊奇队长', 'year': '2019'},
#     {'title': '复仇者联盟4：终局之战', 'year': '2019'},
#     {'title': '蜘蛛侠：英雄远征', 'year': '2019'},
#     {'title': '黑寡妇', 'year': '2021'},
#     {'title': '尚气与十环传奇', 'year': '2021'},
#     {'title': '永恒族', 'year': '2021'},
#     {'title': '蜘蛛侠：英雄无归', 'year': '2021'},
#     {'title': '奇异博士2：疯狂多元宇宙', 'year': '2022'},
#     {'title': '雷神4：爱与雷霆', 'year': '2022'},
#     {'title': '黑豹2：瓦坎达万岁', 'year': '2022'},
#     {'title': '蚁人3：量子狂热', 'year': '2023'},
#     {'title': '银河护卫队3', 'year': '2023'},
#     {'title': '惊奇队长2', 'year': '2023'},
#     {'title': '死侍与金刚狼', 'year': '2024'},

#     # 索尼漫威角色宇宙
#     {'title': '毒液', 'year': '2018'},
#     {'title': '毒液2：屠杀开始', 'year': '2021'},
#     {'title': '莫比亚斯', 'year': '2022'},
#     {'title': '猎人克莱文', 'year': '2023'},
#     {'title': '蜘蛛夫人', 'year': '2023'},

#     # X战警电影宇宙（福克斯）
#     {'title': 'X战警', 'year': '2000'},
#     {'title': 'X战警2', 'year': '2003'},
#     {'title': 'X战警3：背水一战', 'year': '2006'},
#     {'title': '金刚狼', 'year': '2009'},
#     {'title': 'X战警：第一战', 'year': '2011'},
#     {'title': '金刚狼2', 'year': '2013'},
#     {'title': 'X战警：逆转未来', 'year': '2014'},
#     {'title': '死侍', 'year': '2016'},
#     {'title': 'X战警：天启', 'year': '2016'},
#     {'title': '金刚狼3：殊死一战', 'year': '2017'},
#     {'title': '死侍2', 'year': '2018'},
#     {'title': 'X战警：黑凤凰', 'year': '2019'},
#     {'title': '新变种人', 'year': '2020'}
# ]



# import click


# @app.cli.command()
# def forge():
#     """Generate fake data."""
#     db.create_all()

#     # 全局的两个变量移动到这个函数内
#     name = 'Grey Li'
#     movies = [
#         {'title': 'My Neighbor Totoro', 'year': '1988'},
#         {'title': 'Dead Poets Society', 'year': '1989'},
#         {'title': 'A Perfect World', 'year': '1993'},
#         {'title': 'Leon', 'year': '1994'},
#         {'title': 'Mahjong', 'year': '1996'},
#         {'title': 'Swallowtail Butterfly', 'year': '1996'},
#         {'title': 'King of Comedy', 'year': '1999'},
#         {'title': 'Devils on the Doorstep', 'year': '1999'},
#         {'title': 'WALL-E', 'year': '2008'},
#         {'title': 'The Pork of Music', 'year': '2012'},
#     ]

#     user = User(name=name)
#     db.session.add(user)
#     for m in movies:
#         movie = Movie(title=m['title'], year=m['year'])
#         db.session.add(movie)

#     db.session.commit()
#     click.echo('Done.')
@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    # user = User.query.first()
    return render_template('404.html')
    # return render_template('404.html', user=user), 404  # 返回模板和状态码
@app.context_processor#让模板里面都可以用user
def inject_user():  # 函数名可以随意修改
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于 return {'user': user}

