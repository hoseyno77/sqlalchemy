from sqlalchemy import create_engine , Column, INTEGER, String , Float
from sqlalchemy.orm import declarative_base , sessionmaker

engine = create_engine('sqlite:///FruitShop.db', echo=False)
engine.connect()

Base = declarative_base()

class Fruit(Base):
    tablename = 'fruits'

    id = Column(INTEGER, primary_key=True)
    friut_name = Column(String, nullable=False)
    price_unit = Column(Float)
    quantity = Column(INTEGER)


class Customer(Base):
    tablename  = 'customers'

    id = Column(INTEGER, primary_key=True)
    fullname = Column(String, nullable=False)
    address = Column(String)
    mobile_number = Column(String)
    discount = Column(Float)

Base.metadata.create_all(engine)

################################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()

###################################################
# f1 = Fruit(friut_name='watermelon', price_unit=10, quantity=200 )
# f2 = Fruit(friut_name='cherry', price_unit=15, quantity=300 )
# # f3 = Fruit(friut_name='bnnana', price_unit=19, quantity=800 )

# # sessionLocal.add(f1)
# # sessionLocal.add(f2)
# # sessionLocal.add(f3)
# sessionLocal.add_all([f1, f2])
# sessionLocal.commit()

# all_friuts = sessionLocal.query(Fruit).all()
# # print(all_friuts)

# for item in all_friuts:
#     print(item.friut_name)
#     print(item.price_unit)
#     print(item.quantity)
#     print('--'*30)

# f = sessionLocal.query(Fruit).filter_by(quantity = 300).first() # output is Fruit object
# print(f.friut_name)

# print('--'*30)
# f_list = sessionLocal.query(Fruit).filter_by(price_unit = 15 , quantity= 300).all() #output is Fruit Object list
# for item in f_list:
#     print(item.friut_name)
#     print(item.price_unit)
#     print(item.quantity)
#     print('--'*30)

f = sessionLocal.query(Fruit).filter(Fruit.price_unit > 10.0).first()
print(f.friut_name)
print(f.price_unit)

f1 = sessionLocal.query(Fruit).filter(Fruit.friut_name.like('wa%')).first()
print(f1.friut_name)
print(f1.price_unit)

#update
# f1.price_unit = 50.0
# sessionLocal.commit()

#delete
sessionLocal.delete(f1)
sessionLocal.commit()