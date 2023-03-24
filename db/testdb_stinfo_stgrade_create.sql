use testdb;
show tables;

create table st_info(ST_ID int, NAME varchar(20), DEPT varchar(25)) default charset=utf8;
show tables;

create table st_grade(ST_ID int, Linux int, DB int);
show tables;

explain st_info;
explain st_grade;

alter table st_info add constraint pk_stinfo primary key (ST_ID);
alter table st_grade add constraint pk_stgrade primary key (ST_ID);

explain st_info;
explain st_grade;

insert INTO st_info values(202301, "Kazuha",'Game');
insert INTO st_info values(202302, "Karina",'Computer');
insert INTO st_info values(202303, "Jieun",'Game');

insert INTO st_grade values(202301, 80, 70);
insert INTO st_grade values(202302, 90, 75);
insert INTO st_grade values(202303, 95, 85);