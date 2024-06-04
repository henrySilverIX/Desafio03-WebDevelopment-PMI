show databases;
create database contatos;
use contatos;


create table informacoes(
	id int auto_increment primary key,
    nome_completo varchar(250) not null,
    email varchar(250) not null,
    telefone varchar(250) not null,
    comentario varchar(250) not null
);

SELECT * from informacoes;