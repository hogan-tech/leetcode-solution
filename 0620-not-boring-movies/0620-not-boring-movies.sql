select
    Cinema.id,
    Cinema.movie,
    Cinema.description,
    Cinema.rating
from 
    Cinema
where
    Cinema.id % 2 = 1 and Cinema.description != "boring"
order by 
    Cinema.rating desc