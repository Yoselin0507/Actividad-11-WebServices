/*Se crea la base de datos con el nombre ria_iniciales*/
create database ferreteria_yor;

/*Se usa la base de datos creada*/
use ferreteria_yor;

/* Se crea la tabla clientes*/
create table clientes(
    id_cliente integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_c varchar(30) not null,
    apepat_c varchar(20) not null,
    apemat_c varchar(20) not null,
    telefono_c varchar(10) not null,
    email varchar(50) not null
    )ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Se insertan registros en la tabla clientes */
insert into clientes (nombre_c, apepat_c, apemat_c, telefono_c, email) values 
('Yoselin', 'Ortiz', 'Romero', '7751012307', 'ortiz99093@gmail.com'),
('Valentin', 'Gonzalez', 'Miranda', '7757592009', 'vale@gmail.com'),
('Gonzalo', 'Garcia', 'Soto', '7751855159', 'gonza@gmail.com');

/*Se muestran las tablas creadas en la base de datos ferreteria_g_c*/
show tables;

/*Se muestra todos los resgistros que tiene la tabla clientes */
select * from clientes;

/*Muestra los parametros de la tabla creada*/
describe clientes;

/*Conexion a la base de datos creada*/
create user 'yoss'@'localhost' identified by 'yoss.2019';
grant all privileges on ferreteria_g_c.* to 'yoss'@'localhost';
flush privileges; 