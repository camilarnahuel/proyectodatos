copy country(name, gold, silver, bronze, total)
from 'C:\Users\shoyo\Desktop\Proyecto/country.csv' 
delimiter ';'
csv header;

copy country(name, gold, silver, bronze, total)
from '/Volumes/ESD-USB/proyecto_cami/country1.csv' 
delimiter ';'
csv header;

copy event(name)
from 'C:\Users\shoyo\Desktop\Proyecto/event.csv' 
delimiter ';'
csv header;

copy discipline(name, female, male, total)
from 'C:\Users\shoyo\Desktop\Proyecto/discipline.csv' 
delimiter ';'
csv header;

--/////////////ATHLETE/////////////////////
alter table athlete
add column name_country varchar(45)

alter table athlete
add column name_discipline varchar(45)

copy athlete(name, name_country, name_discipline)
from 'C:\Users\shoyo\Desktop\Proyecto/athletes.csv' 
delimiter ';'
csv header;
--/////////////COACH/////////////////////
alter table coach
add column name_country varchar(45);

alter table coach
add column name_discipline varchar(45)

alter table coach
add column name_event varchar(45)

copy coach(name, name_country, name_discipline, name_event)
from 'C:\Users\shoyo\Desktop\Proyecto/coach.csv' 
delimiter ';'
csv header;
--/////////////////////////TEAM///////////////////
alter table team
add column name_country varchar(45);

alter table team
add column name_discipline varchar(45);

alter table team
add column name_event varchar(45)

copy team(name, name_discipline, name_country, name_event)
from 'C:\Users\shoyo\Desktop\Proyecto/team.csv' 
delimiter ';'
csv header;

--////////////////////EVENT_TEAM////////////////
copy event_team(id_event,id_team)
from '/Volumes/ESD-USB/proyecto_cami/event_team.csv' 
delimiter ';'
csv header;

--////////////////////EVENT_COACH////////////////
copy event_coach(id_event,id_coach)
from '/Volumes/ESD-USB/proyecto_cami/event_coach.csv' 
delimiter ';'
csv header;




