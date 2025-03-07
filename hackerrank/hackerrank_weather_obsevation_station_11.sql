-- select CITY from STATION where CITY regexp '^[^aeiouAEIOU]$'
-- ~ no response on stdout ~
-- select CITY from STATION where CITY regexp '^[^aeiouAEIOU][^aeiouAEIOU]$'
-- ~ no response on stdout ~
select distinct CITY from STATION
where CITY regexp '^[^aeiouAEIOU]'
or CITY regexp '[^aeiouAEIOU]$'
