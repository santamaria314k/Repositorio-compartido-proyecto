
Hay que mejorar algunos detalles si  a lgo usted las une  las monta a un repositorio y 
vamos trabajando asincronicamente en el proyecto ,si llega aver clase para el bicho ese 
tocaba enviar un correo con los __name__ y eso a el teacher de proyecto.

crear las tablas:


usuario
roles
valoracion

crear    la primera relacion:
 ALTER TABLE `usuarios` ADD CONSTRAINT `usuarios_fk0` FOREIGN KEY (`id_rol`) REFERENCES `Roles`(`id_rol`);


en el archivo config  hay una coneccion detallada se bdebe dejr igual 

todos los archivos de coneccion y roles esta en loginMenus -> routes.py 

para que la conexion funcione los objetos de la carpeta app => __init__ndeben estar importados 
(flask migrate flask mysql  flask bootstrap)