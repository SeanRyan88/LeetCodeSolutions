-- Challenge 1
select product_id 
from Products
where low_fats = 'Y' and recyclable = 'Y'

-- Challenge 2
select name 
from Customer
where referee_id != 2 or referee_id is null

-- Challenge 3
select name, population, area 
from World
where area >= 3000000 or population >= 25000000

-- Challenge 4
select distinct author_id as id 
from Views
where author_id = viewer_id
order by id 

-- Challenge 5
select tweet_id 
from Tweets
where length(content) >15