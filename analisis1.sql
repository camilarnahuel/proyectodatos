--Analizar la igualdad de género en términos de la cantidad de equipos masculinos 
--y femeninos inscritos por cada país en las respectivas disciplinas.

select distinct d.name as name_discipline, count(e.id) as number_of_events, e.name as name_event
from (discipline d join team t on (d.id=t.id_discipline)
	 			   join event_team et on (t.id=et.id_team)
	 			   join event e on (et.id_event=e.id))
group by d.name,e.name
order by d.name asc;

----------------------------------------------------------------------------------
--Estudiar la correlación existente entre la cantidad de medallas obtenidas por un
--país y los atletas inscritos por dicho país. Es de esperar que a mayor número de 
--atletas el país gane más medallas.

select c.name as name_country, c.total as medals_total, count(a.id) as number_of_athletes
from athlete a join country c on (a.id_country=c.id)
where c.total <> 0
group by c.name, c.total
order by count(a.id) desc;

----------------------------------------------------------------------------------
--Medir la correlación que existe entre la cantidad de entrenadores que tiene cada
--país y su cantidad respectiva de medallas obtenidas en los juegos. Es de esperar
--que un equipo con más entrenadores gane más medallas, esta hipótesis será estudiada.

select c.name as name_country, c.total as medals_total, count(co.id) as number_of_coaches
from coach co join country c on (co.id_country=c.id)
where c.total <> 0
group by c.name, c.total
order by count(co.id) desc;

----------------------------------------------------------------------------------
--Contrastar la cantidad de eventos para cada disciplina y generar una discusión
--sobre las disciplinas sobrevaloradas o infravaloradas por el comité olímpico.

select d.name as name_discipline, count(e.id) as number_of_events
from (discipline d join team t on (d.id=t.id_discipline)
	 			   join event_team et on (t.id=et.id_team)
	 			   join event e on (et.id_event=e.id))   
group by d.name
order by count(e.id) desc;