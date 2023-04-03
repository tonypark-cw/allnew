use testdb;

select * from st_info where ST_ID=202301;

select * from st_info where DEPT ='Game';

select linux from st_grade where ST_ID =202301;

select st_info.name, st_grade.DB, st_grade.Linux, st_info.DEPT from st_info, st_grade where st_info.ST_ID = 202301 and st_grade.st_id=202301;  

update st_grade set linux=90 where st_id = 202301;
select * from st_info;

select st_info.name, st_grade.DB, st_grade.Linux, st_info.DEPT from st_info, st_grade where st_info.ST_ID = 202301 and st_grade.st_id=202301;

update st_info set dept="Computer" where ST_ID =202301;
select * from st_info;
