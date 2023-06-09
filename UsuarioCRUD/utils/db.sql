-- Crear la base de datos `usuariosdb_schema`

CREATE DATABASE IF NOT EXISTS usuariosdb_schema;

-- Utilizar la base de datos `usuariosdb_schema`
USE usuariosdb_schema;

-- Crear la tabla `usuarios`
CREATE TABLE IF NOT EXISTS usuarios (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    correo_electronico VARCHAR(45) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY (correo_electronico)
);

-- Insertar datos de prueba en la tabla `usuarios`
INSERT INTO usuarios (nombre, apellido, correo_electronico) 
VALUES  
    ('Juan', 'Perez', 'juan@perez.com'),
    ('Maria', 'Gomez', 'maria@gomez.com'),
    ('Pedro', 'Gonzalez', 'pedro@gonzalez.com'),
    ('Luis', 'Rodriguez', 'luis@rodriguez.com'),
    ('Ana', 'Hernandez', 'ana@hernandez.com');

-- Seleccionar todos los registros de la tabla `usuarios`
SELECT * FROM usuarios;
