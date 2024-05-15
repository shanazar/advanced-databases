-- Index for store_sales table
CREATE INDEX idx_store_sales_sold_date_sk ON store_sales (ss_sold_date_sk);
CREATE INDEX idx_store_sales_customer_sk ON store_sales (ss_customer_sk);

-- Index for catalog_sales table
CREATE INDEX idx_catalog_sales_sold_date_sk ON catalog_sales (cs_sold_date_sk);
CREATE INDEX idx_catalog_sales_bill_customer_sk ON catalog_sales (cs_bill_customer_sk);

-- Index for web_sales table
CREATE INDEX idx_web_sales_sold_date_sk ON web_sales (ws_sold_date_sk);
CREATE INDEX idx_web_sales_bill_customer_sk ON web_sales (ws_bill_customer_sk);

-- Index for date_dim table
CREATE INDEX idx_date_dim_date_sk ON date_dim (d_date_sk);

-- Index for customer table
CREATE INDEX idx_customer_customer_sk ON customer (c_customer_sk);

select  count(*) from (
    select distinct c_last_name, c_first_name, d_date
    from store_sales, date_dim, customer
          where store_sales.ss_sold_date_sk = date_dim.d_date_sk
      and store_sales.ss_customer_sk = customer.c_customer_sk
      and d_month_seq between 1189 and 1189 + 11
  intersect
    select distinct c_last_name, c_first_name, d_date
    from catalog_sales, date_dim, customer
          where catalog_sales.cs_sold_date_sk = date_dim.d_date_sk
      and catalog_sales.cs_bill_customer_sk = customer.c_customer_sk
      and d_month_seq between 1189 and 1189 + 11
  intersect
    select distinct c_last_name, c_first_name, d_date
    from web_sales, date_dim, customer
          where web_sales.ws_sold_date_sk = date_dim.d_date_sk
      and web_sales.ws_bill_customer_sk = customer.c_customer_sk
      and d_month_seq between 1189 and 1189 + 11
) hot_cust
limit 100;