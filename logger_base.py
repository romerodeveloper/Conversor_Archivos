import logging as log

log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                     log.FileHandler('C:/Users/NICOLAS/Desktop/Cursos/PYTHON_POSTGRESQL/APRENDIZAJE/capa_de_datos/capa_datos_persona/capa_datos.log'),
                     log.StreamHandler()
                        ])

#%(asctime)s agrega fecha y hora al mensaje de log
#%(levelname)s esto muestra el nivel del mensaje que se esta mostrando
#%(filename)s agrega el nombre del archivo al mensaje log
# %(lineno)s agrega el numero de la linea que mando el error
#%(message)s muestra el mensaje que hemos agregado al log

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')