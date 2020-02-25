CREATE TABLE IF NOT EXISTS workers (
id int,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
position VARCHAR(30) NOT NULL,
salary int not null
);

INSERT INTO workers values
(1,'Борщева', 'Дарья', 'юрист', 50000),
(2,'Иванов', 'Иван', 'программист', 25000),
(3,'Петров', 'Петр', 'дизайнер',35000);

select * from workers where salary<30000;
select * from workers where position='программист' and salary<30000;


alter table workers add id_local_chef int ;
select * from workers;
update workers set id_local_chef=2 where id=3;
INSERT INTO workers values
(3,'Петров', 'Петр', 'дизайнер', 35000,1);
INSERT INTO workers values
(4,'Стрелецкий', 'Артем', 'психолог', 35000,1);
update workers set id_local_chef=1 where id=2;
create or replace function task3 (int)
returns table(first_name VARCHAR(30), last_name VARCHAR(30))
as
$$
declare
rec record;
chef int;
begin
for rec in(select workers.id, id_local_chef from workers) loop
if rec.id_local_chef= $1
then chef =rec.id;
end if;
return query select distinct workers.last_name,workers.first_name from workers where workers.id = chef;
end loop;
if (chef is null) then raise exception 'Нет подчиненных';
end if;

end
$$ language plpgsql;

select * from task3(1);


