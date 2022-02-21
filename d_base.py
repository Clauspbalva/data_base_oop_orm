# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

import sqlite3
from sqlite3 import Error
import re
from tabulate import tabulate

# --------------------------------------------------------------------------------------------------
# CLASS DECLARATION 
# --------------------------------------------------------------------------------------------------


class DataBase():
    """
    \nThis class is used to define all methods
    \nthat work with Sqlite3.
    """

    #Method to create connection and database        
    def connect_db(self):
        try:
            self.connection = sqlite3.connect('base.db')
            print("\nSuccessful connection")
            return self.connection
        except:
            Error

    #Method to create table        
    def create_table(self):
        try:
            self.connection
            create_cursor = self.connection.cursor()
            create_cursor.execute(
                """CREATE TABLE IF NOT EXISTS parques_de_escalada 
                (Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                Name text unique NOT NULL, Country text NOT NULL, 
                Town text NOT NULL, Rock_type text NOT NULL)"""
            )
            self.connection.commit()
            print("\nTable created successfully")
        except:
            print("Table can not be created. Please create connection")

    #Method to show table's name
    def show_name(self):
        self.connection
        create_cursor = self.connection.cursor()
        create_cursor.execute(
            """SELECT name FROM sqlite_master 
            WHERE type = 'table' AND name = 'parques_de_escalada'"""
        )
        print("\n", create_cursor.fetchall())

    #Method to show all records on table
    def show_table(self):
        try:
            self.connection
            create_cursor = self.connection.cursor()
            create_cursor.execute("SELECT * FROM parques_de_escalada;")
            records = create_cursor.fetchall()
            DataBase.show_name(self)
            print(
                "\n", tabulate(
                    records, headers=["Id", "Name", "Country", "Town", "Rock type"])
            )   
            print("\nNumber of records: ", len(records))
        except:
            print("Table does not exists. Please create a table")

    #Method to delete tables
    def delete_table(self):
        try:
            self.connection
            create_cursor = self.connection.cursor()
            create_cursor.execute("DROP TABLE IF EXISTS parques_de_escalada")
            self.connection.commit()
            print("\nTable deleted")
        except:
            print("Table does not exists. Please create a table")

    #Method to insert records
    def insert_records(self):
        text_1 = "Validated string: {}"
        text_2 = "Invalid string: {}"
        r1 = input("\nInsert name:").capitalize()
        r2 = input("Insert country:").capitalize()
        r3 = input("Insert town:").capitalize()
        r4 = input("Insert rock type:").capitalize()
        patron = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"
        
        try:
            self.connection
            if(re.match(patron, r1)):
                print("\n", text_1.format(r1))
                sql = (
                    """INSERT INTO parques_de_escalada
                    (Name, Country, Town, Rock_type) VALUES(?, ?, ?, ?)"""
                )
                data = (r1, r2, r3, r4)
                create_cursor = self.connection.cursor()
                create_cursor.execute(sql, data)
                self.connection.commit()
                print("\nNumber of records entered: ", create_cursor.rowcount) 
            else:
                print("\n", text_2.format(r1))
                print("\nThe record could not be entered. Please try again")
        except:
            print("Table not available. Please create table")    

    #Method to delete records
    def delete_records(self):
        try:
            self.connection
            text_1 = "Validated id: {}"
            text_2 = "Invalid id: {}"
            r0 = input("\nInsert id number:")
            pattern = "[0-9]"

            if(re.match(pattern, r0)):
                print("\n", text_1.format(r0))
                sql = ("DELETE from parques_de_escalada where id = ?")
                data = (r0)
                create_cursor = self.connection.cursor()
                create_cursor.execute(sql, data)
                self.connection.commit()
                print("\nThe record has been deleted")
            else:
                print(text_2.format(r0))
                print("\nThe record could not be deleted. Please try again")
        except:
            print("Table not available. Please create table")

    #Method to update records
    def update_records(self):
        try:
            self.connection
            text_1 = "Validated string: {}"
            text_2 = "Invalid string: {}"
            r0 = input("\nInsert id number:")
            r1 = input("\nInsert name update:").capitalize()
            r2 = input("Insert country update:").capitalize()
            r3 = input("Insert town update:").capitalize()
            r4 = input("Insert rock type update:").capitalize()
            pattern = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"

            if(re.match(pattern, r1)):
                print("\n", text_1.format(r1))
                sql = (
                    """UPDATE parques_de_escalada SET 
                    Name = ?, Country = ?, Town = ?, Rock_type = ? where id = ?"""
                )
                data = (r1, r2, r3, r4, r0)
                create_cursor = self.connection.cursor()
                create_cursor.execute(sql, data)
                self.connection.commit()
                print("\nNumber of records updated: ", create_cursor.rowcount) 
            else:
                print(text_2.format(r1))
                print("\nThe record could not be updated. Please try again")
        except:
            print("Table not available. Please create table")
        
    #Method to show an specific record
    def consult_records(self):
        try:
            self.connection
            text_1 = "Validated id: {}"
            text_2 = "Invalid id: {}"
            r0 = input("\nInsert id number:")
            pattern = "[0-9]"

            if(re.match(pattern, r0)):
                print("\n", text_1.format(r0))
                sql = ("SELECT * FROM parques_de_escalada where id = ?")
                data = (r0)
                create_cursor = self.connection.cursor()
                create_cursor.execute(sql, data)
                records = create_cursor.fetchall()
                for row in records:
                    print("\nName:", row[1])
                    print("Country:", row[2])
                    print("Town:", row[3])
                    print("Rock type", row[4]) 
            else:
                print(text_2.format(r0))
        except:
            print("Table not available. Please create table")

    
    

