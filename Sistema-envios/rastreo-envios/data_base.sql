CREATE DATABASE rastreo_envios;

USE rastreo_envios;

CREATE TABLE paquetes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    cliente VARCHAR(100) NOT NULL,
    direccion TEXT NOT NULL,
    estado VARCHAR(50) DEFAULT 'En proceso',
    ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
