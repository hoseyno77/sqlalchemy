from sqlalchemy import create_engine,Column,INTEGER,String,Float
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine('sqlite:///FruitShop.db' , echo = False)
engine.connect()

Base = declarative_base()

class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(INTEGER,primary_key=True)
    fruit_name = Column(String,nullable=False)
    price_unit = Column(Float)
    quantity =Column(INTEGER)

Base.metadata.create_all(engine)

class Customer(Base):
    __tablename__ ="Customers"

    id = Column(INTEGER,primary_key=True)
    fullname = Column(String,nullable=False)
    address =Column(String)
    Phone = Column(String)
    

Base.metadata.create_all(engine)
#######createایجاد کردن  عملیات####################################
Session = sessionmaker(bind=engine)
SessionLocal =Session()
########################################### 
#f1 = Fruit(fruit_name ="apple",price_unit = 10, quantity =200)                              
#f2 = Fruit(fruit_name ="orange",price_unit = 15, quantity =300)
#f3 = Fruit(fruit_name ="bnnana",price_unit = 19, quantity =600) 
#f1 = Fruit(fruit_name ="watermelon",price_unit = 10, quantity =200)                              
#f2= Fruit(fruit_name ="cherry",price_unit = 10, quantity =200)                              

#SessionLocal.add(f1)
#SessionLocal.add(f2)
#SessionLocal.add(f3)
#SessionLocal.add_all([f1,f2])

#SessionLocal.commit()


##########به جای عملیاتreab by select####################################
#all_friuts= SessionLocal.query(Fruit).all()
#print(all_friuts)


#for item in all_friuts:
    
    #print(item.fruit_name)
    #print(item.price_unit)
    #print(item.quantity)
    #print('--'*30)


################# selecteکه شرط د filter by وfilterبا متد###########################

#f_list = SessionLocal.query(Fruit).filter_by(id=1).all()
#print(f.fruit_name)
                           
                           
#for item in f_list:   
                           
    #print(item.fruit_name)
    #print(item.price_unit)
    #print(item.quantity)  
    #print('--'*30)  

#####################################      
#f_list = SessionLocal.query(Fruit).filter_by(price_unit=15,quantity=300).all()
#print(f.fruit_name)                                     
                                                         
                                                         
#for item in f_list:                                     
                                                         
    #print(item.fruit_name)                              
    #print(item.price_unit)                              
    #print(item.quantity)                                
    #print('--'*30)                                      
####################################################
f1 = SessionLocal.query(Fruit).filter(Fruit.fruit_name.like('wa%')).first()
#print(f1.fruit_name)
#print(f1.price_unit)
#update#######################
# f1.price_unit = 50.0
#SessionLocal.commit()
##delete##################
#SessionLocal.delete(f1)
#SessionLocal.commit()
###########################################
f2= SessionLocal.query(Fruit).filter_by(quantity=600).first()
print(f2.fruit_name)

SessionLocal.delete(f2)
SessionLocal.commit()  