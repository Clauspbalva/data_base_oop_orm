# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

from ui_cli import *
import observer


# --------------------------------------------------------------------------------------------------
# CLASS DECLARATION 
# --------------------------------------------------------------------------------------------------

class Controller:
    """
    This is the main class
    """

    #Metodo constructor
    def __init__(self):
        self.controller = UiCli()
        self.observer = observer.ConcreteObserverA(self.controller.object_db)
        self.object_view = UiCli.initialize_program(self.controller)
        

# --------------------------------------------------------------------------------------------------
# MAIN PROCEDURE
# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    application = Controller()
    
    
    