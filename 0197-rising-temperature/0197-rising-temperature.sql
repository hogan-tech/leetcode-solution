select
	Weather.id
from
	Weather
		Join Weather as subWeather
		On subWeather.recordDate = SUBDATE(Weather.recordDate, 1)
where
	Weather.temperature > subWeather.temperature