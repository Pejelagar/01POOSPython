import sqlite3
from sqlite3 import Connection, Cursor

class Database:

    _instance = None
    _db_path = "clínica.db"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_connection(self) -> Connection:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:

        conn = self.get_connection()
        try:
            cursor: Cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS departamento (
                id_dep INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                piso INTEGER NOT NULL
                )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS paciente (
                rut TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                prevision TEXT NOT NULL,
                id_dep INTEGER,
                FOREIGN KEY(id_dep) REFERENCES departamento(id_dep) ON DELETE SET NULL
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    db = Database()
    db.init_db()
    print("Base de datos inicializada correctamento")