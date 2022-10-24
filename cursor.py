from logger_base import log
from conexion import Conexion


class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_exception):
        if tipo_excepcion:
            self._conexion.rollback()
            log.debug(f'Se ha presentado un error de tipo {tipo_excepcion} con valor {valor_excepcion} detalles: {detalle_exception}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion') 
        self._cursor.close()
        Conexion.LiberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('Select * from catalogo')
        log.debug(cursor.fetchall())