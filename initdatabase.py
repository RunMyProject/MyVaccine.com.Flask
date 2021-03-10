from models import engine, db_session, Base, Hospitalward, Patient

Base.metadata.create_all(bind=engine)

# Fill the table Hospitalward with some data
#
vaccinations = Hospitalward(name='Vaccinations', address="Spring Street 7", city="Milan")
db_session.add(vaccinations)

swabs = Hospitalward(name='Swabs', address="Summer Street 4", city="Milan")
db_session.add(swabs)

# Fill the table Patient with some data
#
edoardo = Patient(name='Edoardo', email='edoardo.sabatini@myemail.it', password="123", hospitalward=vaccinations)
db_session.add(edoardo)

admin = Patient(name='Admin', email='admin@myemail.it', password="123", hospitalward=vaccinations)
db_session.add(admin)

Tester = Patient(name='Tester', email='tester@myemail.it', password="123", hospitalward=swabs)
db_session.add(Tester)

db_session.commit()
