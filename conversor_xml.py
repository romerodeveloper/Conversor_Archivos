from typing import final
from cursor import CursorDelPool
import xml.etree.ElementTree as ET
from logger_base import log
from catalogo import Catalogo

class Conversor:

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO catalogo(common, botanical, zone, light, price, availability) VALUES(%s,%s,%s,%s,%s,%s)'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    _xml_data = None


    @classmethod
    def insertar(cls, planta):
        with CursorDelPool() as cursor:
            valores = (planta.find("COMMON").text, planta.find("BOTANICAL").text, planta.find("ZONE").text, planta.find("LIGHT").text, planta.find("PRICE").text, planta.find("AVAILABILITY").text)
            #print(valores)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def leerxml(cls, xml_file):
        try:
            if xml_file.readable():
                cls._xml_data = ET.fromstring(xml_file.read())
                lista_plantas = cls._xml_data.findall('PLANT')
                for planta in lista_plantas:
                    cls.insertar(planta)
                log.debug('Datos insertados correctamente')
            else:
                log.debug(False)
        except Exception as e:
            log.debug(f'Se ha producido un error {e}')
        finally:
            xml_file.close()


if __name__ == '__main__':

    ruta = str(input('Ruta de archivo a ingresar: '))
    archivo = open(ruta)
    conversor = Conversor.leerxml(archivo)

