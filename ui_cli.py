# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

from d_base import DataBase

# --------------------------------------------------------------------------------------------------
# CLASS DECLARATION 
# --------------------------------------------------------------------------------------------------


class UiCli:
    """
    \nClass user interface command line 
    \nit is used to create all the attributes and methods 
    \nfor interaction with the user through the command line.
    """

    #Class attributes
    COMMANDS = ["CB", "CT", "ST", "DT", "IR", "DR", "UR", "CR", "EXIT"]
    COMMANDS_LIST = [
        {"code": "CB", "description": "Create connection and data base"}, 
        {"code": "CT", "description": "Create table"},
        {"code": "ST", "description": "Show table"},
        {"code": "DT", "description": "Delete table"},
        {"code": "IR", "description": "Insert record"},
        {"code": "DR", "description": "Delete record"},
        {"code": "UR", "description": "Update record"},
        {"code": "CR", "description": "Consult record"},
        {"code": "EXIT", "description": "Exit program"}]
    
    #Class method to receive commands
    def receive_command(self):
        self.command = input("\nInsert a command: ").upper()
        while self.command not in UiCli.COMMANDS:
            self.command = input("\nInvalid command. Please enter a valid command: ").upper()

        return self.command

    #Constructor method
    def __init__(self):
        #d_base module instance
        self.db = DataBase()

    def initialize_program(self):
        """
        \nThis method is used for print in command line the information about the app
        \nand the valid commands with their description,
        \nalso is used for receive and accept the commands 
        \nand thus be able to work with class methods of DataBase.
        """
        print("\nCreate data base with python from command line using Sqlite3")
        print("\nValid commands")
        for command in UiCli.COMMANDS_LIST:
            print(f'  {command["code"]}: {command["description"]}')

        command = UiCli.receive_command(self)
        while command != "EXIT":
            if command == "CB":
                self.db.connect_db()      
            elif command == "CT": 
                self.db.create_table()
            elif command == "ST": 
                self.db.show_table() 
            elif command == "DT": 
                self.db.delete_table()           
            elif command == "IR": 
                self.db.insert_records()  
            elif command == "DR": 
                self.db.delete_records()
            elif command == "UR": 
                self.db.update_records()
            elif command == "CR": 
                self.db.consult_records()   
            command = UiCli.receive_command(self)    

        print("\nFinished program")
        



