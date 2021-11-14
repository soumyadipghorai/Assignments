create table customer ( customer_id integer constraint cid primary key, 
phone_number number(10) constraint pnum unique, email_id varchar(100), 
address varchar(100), first_name varchar(20) constraint fname not null,
last_name varchar(20) constraint lname not null);

create table restaurant ( restaurant_id integer constraint rid primary key, 
restaurant_name varchar(20) constraint rname not null,
price number(10) constraint price not null , rating number(2) constraint rating check (rating between 1 and 10), 
address varchar(100), customer_id integer, 
foreign key (customer_id) references customer(customer_id));

create table bill (transaction_id integer constraint tid primary key, 
payment_method varchar(20), date_time date, discount_coupon number, amount integer, 
customer_id integer, restaurant_id integer, foreign key (customer_id) references customer(customer_id), 
foreign key (restaurant_id) references restaurant(restaurant_id));


-- Inserting values : 

insert into customer values(101, 7872817970, 'ghorai.soumyadip33@gmail.com', 
'kolkata', 'abcd1', 'efgh');
insert into customer values(102, 7872827970, 'ghorai.soumyadip33@gmail.com', 
'bangalore', 'abcd2', 'efgh');
insert into customer values(103, 7872867970, 'ghorai.soumyadip33@gmail.com', 
'delhi', 'abcd3', 'efgh');
insert into customer values(104, 7872813970, 'ghorai.soumyadip33@gmail.com', 
'mumbai', 'abcd4', 'efgh');
insert into customer values(105, 7872717970, 'ghorai.soumyadip33@gmail.com', 
'Pune', 'abcd5', 'efgh');
insert into customer values(106, 7871813970, 'ghorai.soumyadip33@gmail.com', 
'contai', 'abcd6', 'efgh');
insert into customer values(107, 7871317970, 'ghorai.soumyadip33@gmail.com', 
'vizag', 'abcd7', 'efgh');
insert into customer values(108, 9871317970, 'ghorai.soumyadip33@gmail.com', 
'vizag', 'abcd8', 'efgh');


insert into restaurant values(1001, 'xyz', 100, 8, 'kolkata', 101);
insert into restaurant values(1002, 'xyz1', 200, 7, 'bangalore', 106);
insert into restaurant values(1003, 'xyz2', 300, 9, 'pune', 107);
insert into restaurant values(1004, 'xyz3', 400, 10, 'contai', 103);
insert into restaurant values(1005, 'xyz4', 500, 5, 'kerala', 104);
insert into restaurant values(1006, 'xyz5', 600, 6, 'delhi', 102);

insert into bill values(101, 'netbanking', date'2021-10-11', 12, 1000, 101, 1001);
insert into bill values(102, 'cash', date'2021-11-12', 12.5, 10200, 102, 1003);
insert into bill values(103, 'card', date'2021-09-10', 12.45, 1200, 104, 1004);
insert into bill values(104, 'credit card', date'2021-10-10', 12.1312, 4000, 105, 1005);
insert into bill values(105, 'EMI', date'2021-11-09', 15.5, 5000, 103, 1006);
insert into bill values(106, 'GPAY', date'2021-03-02', 11.13, 6000, 107, 1001);

-- inner join 
select customer.first_name,customer.last_name, restaurant.restaurant_name 
from restaurant inner join customer on restaurant.customer_id = customer.customer_id;

-- left outer join
select customer.first_name,customer.last_name, restaurant.restaurant_name 
from customer left join restaurant on restaurant.customer_id = customer.customer_id;

-- right outer join
select restaurant.restaurant_name, customer.first_name, customer.last_name from restaurant right join customer on customer.customer_id = restaurant.customer_id;

-- cross join 
select restaurant.restaurant_name, customer.first_name, customer.last_name from restaurant, customer, bill where customer.customer_id = restaurant.customer_id and restaurant.restaurant_id = bill.restaurant_id;

-- self join 
select A.first_name, A.last_name, A.address from customer A, customer B 
where A.customer_id <> B.customer_id and A.address = B.address order by A.address;

-- full outer join  
select restaurant.restaurant_name, customer.first_name, customer.last_name from restaurant full outer join customer on customer.customer_id = restaurant.customer_id
full outer join bill on restaurant.restaurant_id = bill.restaurant_id;



create table bill (transaction_id integer constraint tid primary key, 
payment_method varchar(20), date_time date, discount_coupon number, amount integer);

insert into bill values(101, 'netbanking', date'2021-10-11', 12, 1000);
insert into bill values(102, 'cash', date'2021-11-12', 12.5, 10200);
insert into bill values(103, 'card', date'2021-09-10', 12.45, 1200);
insert into bill values(104, 'credit card', date'2021-10-10', 12.1312, 4000);
insert into bill values(105, 'EMI', date'2021-11-09', 15.5, 5000);
insert into bill values(106, 'GPAY', date'2021-03-02', 11.13, 6000);

-- numeric functions 
select payment_method, abs(discount_coupon) from bill;

select payment_method, ceil(discount_coupon) from bill;

select payment_method, floor(discount_coupon) from bill;

select payment_method, trunc(discount_coupon, 1) from bill;

select payment_method, round(discount_coupon, 2) from bill;

-- character function 
select lower(payment_method) from bill;

select upper(payment_method) from bill;

select initcap(payment_method) from bill;

select length(payment_method) from bill;

select lpad(payment_method, 10) from bill;

-- date function
select add_months(date_time,1) from bill;

select months_between(date_time, date '2021-10-11') from bill;

select last_day(date_time) from bill;

select sysdate, payment_method from bill;
