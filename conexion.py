from psycopg2 import pool
from logger_base import log
import sys

class Conexion:

    _HOST = '127.0.0.1'
    _DATABASE = 'pruebas'
    _PORT = '5432'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _MAX_CON = 5
    _MIN_CON = 1
    _pool = None

    @classmethod
    def ObtenerPool(cls):
        if not cls._pool:
            try: 
                cls._pool = pool.SimpleConnectionPool(cls._MAX_CON, cls._MIN_CON,
                                                    host = cls._HOST,
                                                    port = cls._PORT,
                                                    database = cls._DATABASE,
                                                    user = cls._USERNAME,
                                                    password = cls._PASSWORD)
                log.debug(f'Se creo la conexion del pool: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Se ha producido un error en el pool de tipo {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def ObtenerConexion(cls):
        conexion = cls.ObtenerPool().getconn()
        log.debug(f'Se ha creado la conexion: {conexion} de manera satisfactoria ')
        return conexion

    @classmethod
    def LiberarConexion(cls, conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debug(f'Se ha liberado la conexion: {conexion} de manera satisfactoria ')

