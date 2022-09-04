# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

import logging


# --------------------------------------------------------------------------------------------------
# CLASS DECLARATION 
# --------------------------------------------------------------------------------------------------

def decorator_log(funcion):

    def registro_log(*args, **kwargs):

        called = funcion.__name__.upper()

        logging.basicConfig(
            filename='log.txt', 
            format= '%(asctime)s %(message)s', 
            datefmt='%m/%d/%Y %I:%M:%S %p',
            encoding='utf-8', level=logging.INFO
        )   

        if called == "INSERT_RECORDS":
            logging.info(
                'Action: {0}'.format(
                called)
            )
        elif called == "DELETE_RECORDS":
            logging.info(
                'Action: {0}'.format(
                called)
            )
        elif called == "UPDATE_RECORDS":
            logging.info(
                'Acción: {0}'.format(
                called)
            )
        else:
            logging.info("No se ha realizado ninguna operación")

        return funcion(*args, **kwargs)

    return registro_log