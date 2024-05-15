create database tpcds_06;

# Fact tables
# 1. Catalog sales
create table tpcds_06.catalog_sales as select * from tpcds.catalog_sales LIMIT 684600; # 1,441k rows total
create table tpcds_06.catalog_returns as
    select cr.* from tpcds.catalog_returns as cr
         left join tpcds_06.catalog_sales as cs on
             (cs.cs_order_number=cr.cr_order_number AND cs.cs_item_sk=cr.cr_item_sk)
        where cs.cs_order_number is not null;

# 2. Store sales
create table tpcds_06.store_sales as select * from tpcds.store_sales LIMIT 1728000; # 2,880k rows total
create table tpcds_06.store_returns as
    select sr.* from tpcds.store_returns as sr
         left join tpcds_06.store_sales as sts on
             (sts.ss_ticket_number = sr.sr_ticket_number and sts.ss_item_sk = sr.sr_item_sk)
        where sts.ss_ticket_number is not null;

# 3. Web sales
create table tpcds_06.web_sales as select * from tpcds.web_sales LIMIT 432000; # 720k rows total
create table tpcds_06.web_returns as
    select wr.* from tpcds.web_returns as wr
         left join tpcds_06.web_sales as ws on
             (ws.ws_order_number=wr.wr_order_number and ws.ws_item_sk=wr.wr_item_sk)
        where ws.ws_order_number is not null;

# 4. Inventory
create table tpcds_06.inventory as select * from tpcds.inventory LIMIT 7047000; # 11,745k rows total
# Dim tables
create table tpcds_06.call_center as select * from tpcds.call_center; # 6 rows total
create table tpcds_06.catalog_page as select * from tpcds.catalog_page; #11.7k rows total
create table tpcds_06.customer as select * from tpcds.customer; #100k rows total
create table tpcds_06.customer_address as select * from tpcds.customer_address; #50k rows total
create table tpcds_06.customer_demographics as select * from tpcds.customer_demographics; #1920k rows total
create table tpcds_06.date_dim as select * from tpcds.date_dim; #73k rows total
create table tpcds_06.dbgen_version as select * from tpcds.dbgen_version; #1 row
create table tpcds_06.household_demographics as select * from tpcds.household_demographics; #7.2k rows total
create table tpcds_06.income_band as select * from tpcds.income_band; #20 rows total
create table tpcds_06.item as select * from tpcds.item; #18k rows total
create table tpcds_06.promotion as select * from tpcds.promotion; #300 rows total
create table tpcds_06.reason as select * from tpcds.reason; #35 rows total
create table tpcds_06.ship_mode as select * from tpcds.ship_mode; #20 rows total
create table tpcds_06.store as select * from tpcds.store; #12 rows total
create table tpcds_06.time_dim as select * from tpcds.time_dim; #86.4k rows total
create table tpcds_06.warehouse as select * from tpcds.warehouse; #5 rows total
create table tpcds_06.web_page as select * from tpcds.web_page; #50 rows total
create table tpcds_06.web_site as select * from tpcds.web_site; #30 rows total