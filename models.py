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



class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean)

    
    #relationship wit Role; Each audition is related to one role
    role = relationship('Role', back_populates='auditions')
