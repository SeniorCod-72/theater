from sqlalchemy import Column, Integer, String,Boolean, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker




Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    #Relationship with Audition; one role can have many auditions
    auditions = relationship('Audition', back_populates='role')

    #method to return list of actor name for this role
    def actors(self):
        return[audition.actor for audition in self.auditions]
    
    #method to return list of auditon locations for this role
    def locations(self):
        return[audition.location for audition in self.auditions]
    
    #returning the first actor who was hired for the role or a message if none
    def lead(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if hired_auditions:
            return hired_auditions[0].actor
        return "No actor has been hired for understudy for this role"

    #returning the second hired actor
    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) > 1:
            return hired_auditions[1].actor
        return "No actor has been hired for understudy for this role"


class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean)
    role_id = Column(Integer,ForeignKey('roles.id'))


    #relationship wit Role; Each audition is related to one role
    role = relationship('Role', back_populates='auditions')

    #updating the hired status to true when an actor is hired for a Role
    def call_back(self):
        self.hired = True

engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)