<?php
if($_POST["name"]&&$_POST["email"]!="") {
$de=$_POST["name"];
$destino="labs.chih@gmail.com";
$asunto="Beta Tester";
$mensaje.="\n";
$mensaje.="NOMBRE: ".utf8_decode($_POST["name"])."\n";
$mensaje.="\n";
$mensaje.="EMAIL: ".utf8_decode($_POST["email"])."\n";
$emailheader="Beta Tester aplicacion >\r\n";
mail($destino,$asunto,$mensaje,$emailheader) or die("Lo sentimos, el mail no ha sido enviado <br/>Intentelo de nuevo.");
echo utf8_decode(utf8_encode('Se ha enviado tu mensaje, gracias'));
} else {
if($_POST["nombre"]=="") {
echo utf8_encode('Por favor, indica tu nombre.');
exit ;
}
if($_POST["email"]=="") {
echo utf8_encode('Por favor, indica un email de contacto.');
exit ;
}
}
?>