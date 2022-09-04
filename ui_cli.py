# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

from d_base import DataBase
from tabulate import tabulate


# --------------------------------------------------------------------------------------------------
# CLASS DECLARATION 
# --------------------------------------------------------------------------------------------------

class UiCli:
    """
    \nClass user interface command line 
    \nit is used to create all the attributes and methods 
    \nfor interaction with the user through the command line.
    """

    #Constructor method
    def __init__(self):
        #d_base module instance
        self.object_db = DataBase()

    #Class attributes
    COMMANDS = [
        "CB", "CT", "ST", 
        "DT", "IR", "DR", 
        "UR", "CR", "CC", "EXIT"
    ]
    COMMANDS_LIST = [
        {"code": "CB", "description": "Create connection and data base"}, 
        {"code": "CT", "description": "Create table"},
        {"code": "ST", "description": "Show table"},
        {"code": "IR", "description": "Insert record"},
        {"code": "DR", "description": "Delete record"},
        {"code": "UR", "description": "Update record"},
        {"code": "CR", "description": "Consult record"},
        {"code": "CC", "description": "Close connection"},
        {"code": "EXIT", "description": "Exit program"}
    ]
    
    #Class method to receive commands
    def receive_command(self):
        self.command = input("\nInsert a command: ").upper()
        while self.command not in UiCli.COMMANDS:
            self.command = input("\nInvalid command. Please enter a valid command: ").upper()

        return self.command  

    #Class method to initialize program
    def initialize_program(self):
        """
        \nThis method is used for print in command line the information about the app
        \nand the valid commands with their description,
        \nalso is used for receive and accept the commands 
        \nand thus be able to work with class methods of DataBase.
        """

        information = """
            Create data base with python from command line using an ORM
        """
        table = [[information]]
        print(tabulate(table, tablefmt='grid'))

        table1 = [["\nValid commands"]]
        print(tabulate(table1, tablefmt='grid'))
        for command in UiCli.COMMANDS_LIST:
            print(f'  {command["code"]}: {command["description"]}')

        print("-" * 100)
        command = UiCli.receive_command(self)
        while command != "EXIT":
            if command == "CB":
                self.object_db.connect_db()    
            elif command == "CT": 
                self.object_db.create_table()
            elif command == "ST": 
                self.object_db.show_table()           
            elif command == "IR": 
                self.object_db.insert_records(self)  
            elif command == "DR": 
                self.object_db.delete_records(self)
            elif command == "UR": 
                self.object_db.update_records(self)
            elif command == "CR": 
                self.object_db.consult_records() 
            elif command == "CC": 
                self.object_db.close_db() 
            print("-" * 100)      
            command = UiCli.receive_command(self)    

        print("\nFinished program")
        



