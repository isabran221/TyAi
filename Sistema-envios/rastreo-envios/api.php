<?php
header('Content-Type: application/json');
$conexion = new mysqli("localhost", "root", "", "rastreo_envios");

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['codigo'])) {
    $codigo = $conexion->real_escape_string($_GET['codigo']);
    $sql = "SELECT * FROM paquetes WHERE codigo = '$codigo'";
    $resultado = $conexion->query($sql);
    if ($resultado->num_rows > 0) {
        echo json_encode($resultado->fetch_assoc());
    } else {
        echo json_encode(['mensaje' => 'Paquete no encontrado']);
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $datos = json_decode(file_get_contents('php://input'), true);
    $codigo = $conexion->real_escape_string($datos['codigo']);
    $cliente = $conexion->real_escape_string($datos['cliente']);
    $direccion = $conexion->real_escape_string($datos['direccion']);
    $estado = $conexion->real_escape_string($datos['estado']);

    $sql = "INSERT INTO paquetes (codigo, cliente, direccion, estado)
            VALUES ('$codigo', '$cliente', '$direccion', '$estado')";

    if ($conexion->query($sql)) {
        echo json_encode(['mensaje' => 'Paquete registrado']);
    } else {
        echo json_encode(['mensaje' => 'Error al registrar']);
    }
}

$conexion->close();
?>
