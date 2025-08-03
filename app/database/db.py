from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. URL de conexión
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/biblioteca"
# 2. Crear el motor
engine = create_engine(DATABASE_URL)
# 3. Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
