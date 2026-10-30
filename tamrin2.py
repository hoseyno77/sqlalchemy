from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine("sqlite:///School.db", echo=True)


Base = declarative_base()



class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)#نوع داده_ کلید اصلی_ افزایش خودکار
    name = Column(String, nullable=False)

    courses = relationship(
        "Course",
        back_populates="student",
        cascade="all, delete-orphan"
    )#اگه یه دانش اموز حذف شه درس های مربوط به ان هم حذف میشه



class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )#تعریف کلید خارجی

    student = relationship("Student", back_populates="courses")


#Base.metadata.create_all(engine)




Session = sessionmaker(bind=engine)
session = Session()



student1 = Student(name="ahmad")
student2 = Student(name="nahid")


course1 = Course(title="Python")
course2 = Course(title="Database")
course3 = Course(title="Streamlit")
course4 = Course(title="Mediapipe")

student1.courses.append(course1)
student1.courses.append(course2)
student2.courses.append(course3)
student2.courses.append(course4)



# session.add(student1)
# session.commit()
# session.add(student2)
# session.commit()



students = session.query(Student).all()

for student in students:
    print("Student ID:", student.id)
    print("Student Name:", student.name)

    for course in student.courses:
        print("Course ID:", course.id)
        print("Course Title:", course.title)
        print(30 * '--')
  




