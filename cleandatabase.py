from models import engine, db_session, Base, Hospitalward, Patient

# Delete all tables if exist!
#
Hospitalward.__table__.drop(engine)
Patient.__table__.drop(engine)

Base.metadata.create_all(bind=engine)

db_session.commit()
