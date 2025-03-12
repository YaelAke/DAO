from database import obtener_db

class UsuarioDAO:
    def __init__(self):
        self.db = obtener_db()
        self.coleccion = self.db["usuarios"]

    def crear_usuario(self, usuario):
        return self.coleccion.insert_one(usuario).inserted_id

    def obtener_usuarios(self):
        return list(self.coleccion.find({}, {"_id": 0}))

    def obtener_usuario_por_nombre(self, nombre):
        return self.coleccion.find_one({"nombre": nombre}, {"_id": 0})

    def actualizar_usuario(self, nombre, nuevos_datos):
        resultado = self.coleccion.update_one({"nombre": nombre}, {"$set": nuevos_datos})
        return resultado.modified_count > 0

    def eliminar_usuario(self, nombre):
        return self.coleccion.delete_one({"nombre": nombre}).deleted_count
