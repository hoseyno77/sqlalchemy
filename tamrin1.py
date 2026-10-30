from sqlalchemy import create_engine,Column,INTEGER,String,Float
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine('sqlite:///students1.db' , echo = False)
engine.connect()

Base = declarative_base()

class Student(Base):
    __tablename__ = "Students"

    id = Column(INTEGER,primary_key=True)
    name = Column(String,nullable=False)
    score = Column(Float)
    
Base.metadata.create_all(engine)

#########################Create######################

Session = sessionmaker(bind=engine)
SessionLocal =Session()

f1 = Student(name ="sina shahi",score = 15)                              
f2 = Student(name ="bahar nab",score = 18)                              
f3 = Student(name ="lena ghasemi",score = 20)                              
f4 = Student(name ="saman sarfaraz",score = 12)                              

# SessionLocal.add_all([f1,f2,f3,f4])
# SessionLocal.commit()

#################Read#########################
 
all_students= SessionLocal.query(Student).all()
print(all_students)

for item in all_students:  
    print(item.name)
    print(item.score)
    print('--'*30)
 

# f_list = SessionLocal.query(Student).filter_by(id=1).all()
# print(f1.name)
  
# for item in f_list:   
  
    # print(item.name)
    # print(item.score)
    # print('--'*30)  
                                                                                                                                                     
######################update############################

f1= SessionLocal.query(Student).filter_by(score=18).first()

f1.score = 13.75
SessionLocal.commit()

 
#####################delete###########################

# f2= SessionLocal.query(Student).filter_by(id=4).first()

# SessionLocal.delete(f2)
# SessionLocal.commit()  