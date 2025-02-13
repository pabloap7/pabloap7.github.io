from data.modelo.director import Director

class DaoDirectores:
    
    def get_all(self,db) -> list[Director]:
        cursor = db.cursor()  
        cursor.execute("SELECT * FROM directores")
        equipos_en_db = cursor.fetchall()
        equipos : list[Director]= list()
        for equipo in equipos_en_db:
            director = Director(equipo[0], equipo[1])
            equipos.append(director)
        cursor.close()     
        return equipos
    
    def add_director(self, db, nombre: str):
        cursor = db.cursor()
        
        # Calcular el id
        cursor.execute("SELECT MAX(id) FROM directores")
        last_id = cursor.fetchone()[0]
        next_id = last_id + 1 if last_id is not None else 1
        
        # Insertar el nuevo director con el id calculado
        sql = "INSERT INTO directores (id, nombre) VALUES (%s, %s)"
        data = (next_id, nombre)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()


    def delete_director(self, db, id: int):
        cursor = db.cursor()
        sql = "DELETE FROM directores WHERE id = %s"
        data = (id,)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()