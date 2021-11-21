create table event_coach(
	id_event int,
	id_coach int,
	primary key(id_event,id_coach));
	
create table event_team(
	id_event int,
	id_team int,
	primary key(id_event,id_team));
	
copy event_coach(id_event,id_coach)
from '/Volumes/ESD-USB/proyecto_cami/event_coach.csv' 
delimiter ';'
csv header;

copy event_team(id_event,id_team)
from '/Volumes/ESD-USB/proyecto_cami/event_team.csv' 
delimiter ';'
csv header;