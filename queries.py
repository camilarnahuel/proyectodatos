# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:09:13 2021

@author: anaka
"""

def getMedalsby():
    return """
    select c.name as name_country, c.total as medals_total, count(a.id) as number_of_athletes
from athlete a join country c on (a.id_country=c.id)
where c.total <> 0
group by c.name, c.total
order by count(a.id) desc;
    """  

   

def getbyGender():
    
    return """ select distinct d.name as name_discipline, count(e.id) as number_of_events, e.name as name_event
from (discipline d join team t on (d.id=t.id_discipline)
	 			   join event_team et on (t.id=et.id_team)
	 			   join event e on (et.id_event=e.id))
group by d.name,e.name
order by d.name asc;
"""

def getCoachesandMedals():
    return """select c.name as name_country, c.total as medals_total, count(co.id) as number_of_coaches
from coach co join country c on (co.id_country=c.id)
where c.total <> 0
group by c.name, c.total
order by count(co.id) desc;"""

def getEventsbyDis():
    return """select d.name as name_discipline, count(e.id) as number_of_events
from (discipline d join team t on (d.id=t.id_discipline)
	 			   join event_team et on (t.id=et.id_team)
	 			   join event e on (et.id_event=e.id))   
group by d.name
order by count(e.id) desc; """


