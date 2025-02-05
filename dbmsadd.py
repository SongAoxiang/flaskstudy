from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化 Flask
app = Flask(__name__)

# 配置 MySQL 连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db = SQLAlchemy(app)

# 定义电影模型
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 电影ID
    title = db.Column(db.String(100), nullable=False)  # 电影标题
    year = db.Column(db.String(4), nullable=False)  # 上映年份

#定义用户模型
class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    password = db.Column(db.String(25))

# 电影数据
movies = [
    {'title': '钢铁侠', 'year': '2008'},
    {'title': '无敌浩克', 'year': '2008'},
    {'title': '钢铁侠2', 'year': '2010'},
    {'title': '雷神', 'year': '2011'},
    {'title': '美国队长', 'year': '2011'},
    {'title': '复仇者联盟', 'year': '2012'},
    {'title': '钢铁侠3', 'year': '2013'},
    {'title': '雷神2：黑暗世界', 'year': '2013'},
    {'title': '美国队长2：冬日战士', 'year': '2014'},
    {'title': '银河护卫队', 'year': '2014'},
    {'title': '复仇者联盟2：奥创纪元', 'year': '2015'},
    {'title': '蚁人', 'year': '2015'},
    {'title': '美国队长3：内战', 'year': '2016'},
    {'title': '奇异博士', 'year': '2016'},
    {'title': '银河护卫队2', 'year': '2017'},
    {'title': '蜘蛛侠：英雄归来', 'year': '2017'},
    {'title': '雷神3：诸神黄昏', 'year': '2017'},
    {'title': '黑豹', 'year': '2018'},
    {'title': '复仇者联盟3：无限战争', 'year': '2018'},
    {'title': '蚁人2：黄蜂女现身', 'year': '2018'},
    {'title': '惊奇队长', 'year': '2019'},
    {'title': '复仇者联盟4：终局之战', 'year': '2019'},
    {'title': '蜘蛛侠：英雄远征', 'year': '2019'},
    {'title': '黑寡妇', 'year': '2021'},
    {'title': '尚气与十环传奇', 'year': '2021'},
    {'title': '永恒族', 'year': '2021'},
    {'title': '蜘蛛侠：英雄无归', 'year': '2021'},
    {'title': '奇异博士2：疯狂多元宇宙', 'year': '2022'},
    {'title': '雷神4：爱与雷霆', 'year': '2022'},
    {'title': '黑豹2：瓦坎达万岁', 'year': '2022'},
    {'title': '蚁人3：量子狂热', 'year': '2023'},
    {'title': '银河护卫队3', 'year': '2023'},
    {'title': '惊奇队长2', 'year': '2023'},
    {'title': '死侍与金刚狼', 'year': '2024'},
    {'title': '毒液', 'year': '2018'},
    {'title': '毒液2：屠杀开始', 'year': '2021'},
    {'title': '莫比亚斯', 'year': '2022'},
    {'title': '猎人克莱文', 'year': '2023'},
    {'title': '蜘蛛夫人', 'year': '2023'},
    {'title': 'X战警', 'year': '2000'},
    {'title': 'X战警2', 'year': '2003'},
    {'title': 'X战警3：背水一战', 'year': '2006'},
    {'title': '金刚狼', 'year': '2009'},
    {'title': 'X战警：第一战', 'year': '2011'},
    {'title': '金刚狼2', 'year': '2013'},
    {'title': 'X战警：逆转未来', 'year': '2014'},
    {'title': '死侍', 'year': '2016'},
    {'title': 'X战警：天启', 'year': '2016'},
    {'title': '金刚狼3：殊死一战', 'year': '2017'},
    {'title': '死侍2', 'year': '2018'},
    {'title': 'X战警：黑凤凰', 'year': '2019'},
    {'title': '新变种人', 'year': '2020'}
]

# 插入数据
def insert_movies():
    with app.app_context():  # 确保在 Flask 上下文中执行
        db.create_all()  # 创建表（如果不存在）
        db.session.add(User(name="Song Aoxiang",password="123456"))
        db.session.commit()
        # 检查是否已存在数据，避免重复插入
        if Movie.query.first() is None:
            for movie in movies:
                db.session.add(Movie(title=movie['title'], year=movie['year']))
            db.session.commit()
            print("✅ 电影数据已成功插入数据库！")
        else:
            print("⚠️ 数据库已存在电影数据，未进行重复插入！")

if __name__ == '__main__':
    insert_movies()
    
