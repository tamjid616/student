from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/student_table"
DATABASE_URL = "postgresql+psycopg2://student_s3so_user:if0TQw3AGnW5ezgHx8SclyXICx0LuB3C@dpg-dbct6kuq1p3s73d832eg-a.oregon-postgres.render.com/student_s3so"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()