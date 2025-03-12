# Patrón DAO con Conexión a Base de Datos en MongoDB

Este proyecto implementa el **Patrón de Diseño Data Access Object (DAO)** para gestionar usuarios en una base de datos MongoDB. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los usuarios, asegurando una separación clara entre la lógica de acceso a datos y la lógica de negocio.

## Características Principales
- **Patrón DAO:** Separa la lógica de acceso a datos de la lógica de negocio, mejorando la mantenibilidad y reutilización del código.
- **MongoDB como Base de Datos:** Almacena los datos de los usuarios en una colección eficiente.
- **Arquitectura en Capas:** División clara entre **Rutas (Flask), DAO (Acceso a Datos) y Conexión a la Base de Datos**.
- **Interfaz Web Simple:** Permite gestionar usuarios desde el navegador con un diseño responsivo.
- **Flask como Framework Backend:** Sencillo y eficiente para la gestión de APIs RESTful.

## Tecnologías Utilizadas
- **Python y Flask** para el desarrollo del backend.
- **MongoDB** como base de datos NoSQL.
- **Pymongo** como driver para interactuar con MongoDB.
- **HTML, CSS y JavaScript** para la interfaz de usuario.
- **Fetch API** para consumir los endpoints de la API desde el frontend.

---

## **¿Qué es el Patrón de Diseño DAO?**
El **Patrón Data Access Object (DAO)** es una estrategia que abstrae la interacción con la base de datos, proporcionando una interfaz sencilla para acceder y manipular los datos.

### **Características del Patrón DAO**
- **Encapsulamiento del acceso a datos:** Se aísla la lógica de base de datos en una capa separada.
- **Mantenimiento simplificado:** Permite modificar la implementación de acceso a datos sin afectar la lógica de negocio.
- **Desacoplamiento:** El código de Flask no interactúa directamente con MongoDB, sino a través del DAO.
- **Reutilización:** Se pueden usar los métodos del DAO en diferentes partes de la aplicación sin redundancia de código.
- **Seguridad y organización:** Reduce el riesgo de errores al manejar directamente la base de datos en la capa de presentación.

---

### **Diagrama UML del Patrón DAO**
![Diagrama UML](https://drive.google.com/uc?export=view&id=1owYg3id3CFguL0qICn4PG3YoHz0TFuhS)

