# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

from peewee import *
import re
from decorators import *
from observer import Subject
from tabulate import tabulate


# --------------------------------------------------------------------------------------------------
# CLASS DECLARATION 
# --------------------------------------------------------------------------------------------------

# The db object will be used to manage the connections to the Sqlite database
db = SqliteDatabase("base.db")

class BaseModel(Model):
    class Meta:
        database = db

class ClimbingSchools(BaseModel):
    """
    \nThis class defines the
    \ndatabase attributes.
    """
    name = CharField(unique = True)
    country = TextField()
    town = TextField()
    rock_type = TextField()

    #Method str of python
    def __str__(self):
        return "The name of the park is: " + self.name

class DataBase(Subject):
    """
    \nThis class is used to define all methods
    \nthat work with the database.
    """

    #Constructor method
    def __init__(self):
        db.connect()
        db.create_tables([ClimbingSchools])
        db.close()

    #Method to create connection and database        
    def connect_db(self):
        try:
            self.connection = db.connect
            print("\nSuccessful connection")
            return self.connection
        except:
            print("Connection not available")

    #Method to create table
    def create_table(self):
        try:
            self.create_table = db.create_tables(ClimbingSchools)
            print("\nTable created successfully")
            return self.create_table
        except:
            print("Table can not be created. Please create connection")

    #Method to show all records on table
    def show_table(self):
        headers = ["Id", "Name", "Country", "Town", "Rock_type", "Str method"] 
        values = []  

        try:
            for record in ClimbingSchools.select():  
                col1 = record.id 
                col2 = record.name 
                col3 = record.country 
                col4 = record.town 
                col5 = record.rock_type
                col6 = record   # This call the str method of Python
                column = col1, col2, col3, col4, col5, col6 
                values.append(column)    
            print(tabulate(values, headers, tablefmt="github"))  
            print("\nNumber of records: ", ClimbingSchools.select().count())
        except:
            print("Table does not exists. Please create a table")

    #Method to insert records
    @decorator_log
    def insert_records(self, r1):
        table = ClimbingSchools()
        text_1 = "Validated string: {}"
        text_2 = "Invalid string: {}"
        r1 = input("\nInsert name:").capitalize()
        r2 = input("Insert country:").capitalize()
        r3 = input("Insert town:").capitalize()
        r4 = input("Insert rock type:").capitalize()
        patron = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"

        try:
            if(re.match(patron, r1)):
                print("-" * 100)
                print("\n", text_1.format(r1))
                table.name = r1
                table.country = r2
                table.town = r3
                table.rock_type = r4
                table.save()
                self.notify(r1) #This is the observer
                print("\nNumber of records entered: ", table.save())   
            else:
                print("\n", text_2.format(r1))
                print("\nThe record could not be entered. Please try again")
        except:
            print("Table not available. Please create table")
    
    #Method to delete records
    @decorator_log
    def delete_records(self, r0):
        table = ClimbingSchools()
        text_1 = "Validated id: {}"
        text_2 = "Invalid id: {}"
        r0 = input("\nInsert id number:")
        pattern = "[0-9]"

        try:
            if(re.match(pattern, r0)):
                print("-" * 100)
                print("\n", text_1.format(r0))
                table = ClimbingSchools.get(ClimbingSchools.id == r0)
                table.delete_instance()   
                print("\nThe record has been deleted")
            else:
                print(text_2.format(r0))
                print("\nThe record could not be deleted. Please try again")
        except:
            print("Table not available. Please create table")

    #Method to update records
    @decorator_log
    def update_records(self, r0):
        text_1 = "Validated string: {}"
        text_2 = "Invalid string: {}"
        r0 = input("\nInsert id number:")
        r1 = input("\nInsert update name:").capitalize()
        r2 = input("Insert update country:").capitalize()
        r3 = input("Insert update town:").capitalize()
        r4 = input("Insert update rock type:").capitalize()
        pattern = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"

        try:
            if(re.match(pattern, r1)):
                print("-" * 100)
                print("\n", text_1.format(r1))
                update = ClimbingSchools.update(
                    name = r1, 
                    country = r2,
                    town = r3,
                    rock_type = r4 
                    ).where(ClimbingSchools.id == r0)
                update.execute()
                print("\nRecord has been updated") 
            else:
                print(text_2.format(r1))
                print("\nThe record could not be updated. Please try again")
        except:
            print("Table not available. Please create table")
        
    #Method to show an specific record
    def consult_records(self):  
        text_1 = "Validated id: {}"
        text_2 = "Invalid id: {}"
        r0 = input("\nInsert id number:")
        pattern = "[0-9]"
        headers = ["Name", "Country", "Town", "Rock_type"]
        try:
            if(re.match(pattern, r0)):
                print("-" * 100)
                print("\n", text_1.format(r0), "\n")
                for record in ClimbingSchools.select().where(ClimbingSchools.id == r0):
                    records = [
                        [record.name,
                        record.country, record. town,
                        record.rock_type]
                    ]
                    print(tabulate(records, headers, tablefmt="github")) 
            else:
                print(text_2.format(r0))
        except:
            print("Table not available. Please create table")

    def close_db(self):
        try:
            self.close = db.close()
            print("\nSuccessful disconnection")
            return self.close
        except:
            print("Connection not available")

    
    

