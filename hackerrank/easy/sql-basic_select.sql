/*https://www.hackerrank.com/challenges/revising-the-select-query*/

select * from city where countrycode = 'USA' and population > 100000;

/*https://www.hackerrank.com/challenges/revising-the-select-query-2*/

select name from city where countrycode = 'USA' and population > 120000;

/*https://www.hackerrank.com/challenges/select-all-sql*/

select * from city;

/*https://www.hackerrank.com/challenges/select-by-id*/

select * from city where id = 1661;

/*https://www.hackerrank.com/challenges/japanese-cities-detail*/

select * from city where countrycode = 'JPN';

/*https://www.hackerrank.com/challenges/weather-observation-station-5*/

/*Can do it better!!!*/
select city, length(city) from station order by length(city) asc limit 1; 
select city, length(city) from station order by length(city) desc limit 1; 
