import uuid
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func



db = SQLAlchemy()

class Authentication(db.Model):
    AuthenticationId = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    Username = db.Column(db.String(45), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(45), nullable=False)
    user_type = db.Column(db.String(20), nullable=True)
    timestamp = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    

class DepartmentAdministrator(db.Model):
    DepartmentAdminID = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    FirstName = db.Column(db.String(45), nullable=False)
    LastName = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), nullable=False)
    Password = db.Column(db.String(45), nullable=False)
    timestamp = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    internship_requests = db.relationship(
        "InternshipRequest", back_populates="department_administrator"
    )
    department = db.relationship(
        "Department", back_populates="department_administrator"
    )

class HRAdministrator(db.Model):
    AdminId = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    FirstName = db.Column(db.String(45), nullable=False)
    LastName = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), nullable=False)
    Password = db.Column(db.String(45), nullable=False)
    application_status = db.Column(db.Boolean, default=True)
    user_type = db.Column(db.String(20), nullable=True, default='admin')  

    timestamp = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    


class InternshipRequest(db.Model):
    RequestId = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    RequestDate = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Notes = db.Column(db.Text, nullable=True)
    VacantSpaces = db.Column(db.Integer, nullable=False)

    DepartmentAdminID = db.Column(
        db.CHAR(36), db.ForeignKey("department_administrator.DepartmentAdminID")
    )
    department_administrator = db.relationship(
        "DepartmentAdministrator", back_populates="internship_requests"
    )

class InternFeedback(db.Model):
    FeedbackId = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    Question1Rating = db.Column(db.Integer, nullable=False)
    Question2Rating = db.Column(db.Integer, nullable=False)
    Question3Rating = db.Column(db.Integer, nullable=False)
    Question4Rating = db.Column(db.Integer, nullable=False)
    Question5Rating = db.Column(db.Integer, nullable=False)
    Comment = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    StudentId = db.Column(db.CHAR(36), db.ForeignKey('student.StudentId'), nullable=False)
    student = db.relationship('Student', backref='feedbacks')



class Department(db.Model):
    DepartmentId = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    DepartmentName = db.Column(db.String(45))
    DepartmentLocation = db.Column(db.String(45))
    application_status = db.Column(db.Boolean, default=True)
    timestamp = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    department_administrator_id = db.Column(
        db.CHAR(36), db.ForeignKey("department_administrator.DepartmentAdminID")
    )
    department_administrator = db.relationship(
        "DepartmentAdministrator", back_populates="department"
    )

class Student(db.Model):
    StudentId = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    FirstName = db.Column(db.String(45), nullable=False)
    LastName = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), nullable=False)
    Residence = db.Column(db.String(45), nullable=False)
    institution = db.Column(db.String(255), nullable=False)
    Level = db.Column(db.String(45), nullable=False)
    inst_location = db.Column(db.String(45), nullable=False)
    IndexNumber = db.Column(db.String(10), nullable=False)
    Programme = db.Column(db.String(45), nullable=False)
    StartDate = db.Column(db.Date, nullable=False)
    EndDate = db.Column(db.Date, nullable=False)
    InternshipLetter = db.Column(db.String(255), nullable=False)
    ApplicationStatus = db.Column(db.String(45), nullable=False)   
    NationalId = db.Column(db.String(45), nullable=True)

    DateofBirth = db.Column(db.Date, nullable=True)
    authentication_id = db.Column(
        db.CHAR(36), db.ForeignKey("authentication.AuthenticationId"), nullable=False
    )
    authentication = db.relationship("Authentication", backref="students")
    DateAssigned = db.Column(db.Date, nullable=True)
    DepartmentId = db.Column(
        db.CHAR(36), db.ForeignKey("department.DepartmentId"), nullable=True
    )
    Department = db.relationship("Department", backref="students")

class Records(db.Model):
    RecordsId = db.Column(db.CHAR(36), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    StartDate = db.Column(db.Date, nullable=True)
    EndDate = db.Column(db.Date, nullable=True)
    AcceptanceLetter = db.Column(db.String(255), nullable=True)
    Indemnityform = db.Column(db.String(45), nullable=True)
    InternshipStatus = db.Column(db.String(45), nullable=False)
    Progress = db.Column(db.String(45), nullable=False)
    signed = db.Column(db.Boolean, default=False)
    email_sent=db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    student_id = db.Column(
        db.CHAR(36), db.ForeignKey("student.StudentId"), nullable=True
    )
    student = db.relationship("Student", backref="records")
    department_id = db.Column(db.CHAR(36), db.ForeignKey("department.DepartmentId"))
    department = db.relationship("Department", backref="records")


def create_tables(app):
    with app.app_context():
        db.create_all()