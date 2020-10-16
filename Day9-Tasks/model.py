# Patient Model Class

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger, Text

base = declarative_base()

class Patient(base):

    __tablename__ = 'p_details'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(Text)
    state = Column(String)
    country = Column(String)
    phoneNumber = Column(BigInteger)
    report = Column(Text)

    def __init__(self, id, name, address, state, country, phoneNumber, report):
        self.id = id
        self.name = name
        self.address = address
        self.state = state
        self.country = country
        self.phoneNumber = phoneNumber
        self.report = report
    
    def __repr__(self):
        return f"Patient Id : {self.id}, Name : {self.name}, Address : {self.address}, State : {self.state}, Country : {self.country}, Phone Number : {self.phoneNumber}, Report : {self.report}"
    
