from sqlalchemy import create_engine, Column, INTEGER, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///Social_Media.db')
engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'usersInfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    username = Column(String)

    posts = relationship('Post', back_populates='owner' )

class Post(Base):
    __tablename__ = 'postsInfo'

    id = Column(INTEGER, primary_key=True)
    title = Column(String)

    user_id = Column(INTEGER, ForeignKey('usersInfo.id'))

    owner = relationship('User', back_populates='posts')

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
sessionLocal = Session()

# user1 = User(name='Nima Asadi', username='Nima123')
# user2 = User(name='Reza Amini', username='Reza123')
# sessionLocal.add_all([user1, user2])
# sessionLocal.commit()

# post1 = Post(title='Subject 1', user_id=1)
# post2 = Post(title='Subject 2', user_id=1)
# sessionLocal.add_all([post1, post2])
# sessionLocal.commit()
 
# temp = sessionLocal.query(User).filter_by(id=1).first()
# print(temp.name)
# print(temp.posts)
# 
# for post in temp.posts:
    # print(post.title)
