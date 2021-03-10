import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from models import db_session, Hospitalward as HospitalwardModel, Patient as PatientModel

from graphene import String

class Hospitalward(SQLAlchemyObjectType):
    class Meta:
        model = HospitalwardModel
        interfaces = (relay.Node, )

class Patient(SQLAlchemyObjectType):
    class Meta:
        model = PatientModel
        filter_fields = ['name']
        interfaces = (relay.Node, )        

class Query(graphene.ObjectType):
    
    # Define a new node connection field for entire structure of patients and hospitalwards
    #
    node = relay.Node.Field()

    # Define a new patient GraphQL Query to resolve below in a def
    #
    patient = graphene.List(Patient, name=graphene.String())

    # Allows sorting over multiple columns, by default over the primary key
    #
    all_patients = SQLAlchemyConnectionField(Patient.connection)

    # Disable sorting over this field
    #
    all_hospitalwards = SQLAlchemyConnectionField(Hospitalward.connection, sort=None)

    def resolve_patient(self, info, **args):
        
        # Search query
        #
        name = args.get("name") 

        # Get queries
        #
        query = Patient.get_query(info)  # SQLAlchemy query

        # Query on all Patients by name
        #
        return query.filter(PatientModel.name.contains(name)).all()

schema = graphene.Schema(query=Query)


#
#
#
# #########################
# other techs and solutions
# 
#
#

"""
name = graphene.String(description='The name of the ship.')

@classmethod
def get_node(cls, info, id):
    return get_ship(id

# Queries with Object Types
#
patients = graphene.List(Patient)
patient_by_name = graphene.Field(Patient, name=graphene.String())

def resolve_patients(root, info, **kwargs):
    # Querying a list
    #
    return Question.objects.all()

def resolve_patient_by_name(root, info, name):
    # Querying a single patient
    #
    return f'Patient {name}!'
    # return Question.objects.get(name=name)
"""    

# class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
#    hello = String(name=String(default_value="stranger"))
#    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
#   def resolve_hello(root, info, name):
#        return f'Hello {name}!'

#   def resolve_goodbye(root, info):
#        return 'See ya!'

# schema = Schema(query=Query)

# we can query for our field (with the default argument)
# query_string = '{ hello }'
# result = schema.execute(query_string)
# print(result.data['hello'])
# "Hello stranger!"

# or passing the argument in the query
# query_with_argument = '{ hello(name: "GraphQL") }'
# result = schema.execute(query_with_argument)
# print(result.data['hello'])
# "Hello GraphQL!"
