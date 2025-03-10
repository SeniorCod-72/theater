from sqlalchemy import Column, Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship




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
    





class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean)


    #relationship wit Role; Each audition is related to one role
    role = relationship('Role', back_populates='auditions')

    #updating the hired status to true when an actor is hired for a Role
    def call_back(self):
        self.hired = True
