SELECT countries.name as name, languages.language as language, languages.percentage as percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name as name, COUNT(cities.name) as cities
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY cities DESC;

select * from cities 
where country_id = 136 and population >= 500000 
order by population desc;

select * from languages 
join countries on countries.id = country_id 
where percentage > 89 
order by percentage desc;

select countries.name as name, countries.surface_area as surface_area, countries.population as population from countries
where surface_area < 501 and population > 100000;

SELECT countries.government_form as government_form, countries.capital as capital, countries.life_expectancy as life_expectancy FROM countries
WHERE countries.government_form = "Constitutional Monarchy" and countries.capital > 200 and countries.life_expectancy > 75;

SELECT * FROM cities
WHERE cities.country_id = 9 and cities.district = "Buenos Aires" and cities.population > 500000;


