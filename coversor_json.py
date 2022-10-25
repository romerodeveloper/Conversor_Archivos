from cursor import CursorDelPool
import json
from logger_base import log

class ConversorJson:

    _INSERTAR = 'INSERT INTO catalogo(common, botanical, zone, light, price, availability) VALUES(%s,%s,%s,%s,%s,%s)'
  
    @classmethod
    def insertar(cls, planta):
        with CursorDelPool() as cursor:
            valores = (planta['COMMON'], planta['BOTANICAL'], planta['ZONE'], planta['LIGHT'], planta['PRICE'], planta['AVAILABILITY'] )
            cursor.execute(cls._INSERTAR, valores)
            log.info('Registro exitoso')
            return cursor.rowcount

    @classmethod
    def LeerJson(cls, archivo):
        try:
            # Abrir el archivo ordenes.json
            with open(archivo) as archivo:
                # Cargar su contenido y crear un diccionario
                datos = json.load(archivo)
                datos_generales = datos['CATALOG']['PLANT'] 
                for registro in datos_generales:
                    cls.insertar(registro)
                    log.info('Fin de la lectura')
        except NameError as e:
            log.debug(f'Error: {e}')
        except Exception as e:
            log.debug(f'Error de tipo: {e}')
        

if __name__ == '__main__':
    ruta_archivo = input('Ingrese la ruta del archivo: ')
    datos = ConversorJson.LeerJson(ruta_archivo)
