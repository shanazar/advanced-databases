-- Index for store_sales table
CREATE INDEX idx_store_sales_sold_date_sk ON store_sales (ss_sold_date_sk);
CREATE INDEX idx_store_sales_item_sk ON store_sales (ss_item_sk);
CREATE INDEX idx_store_sales_store_sk ON store_sales (ss_store_sk);
CREATE INDEX idx_store_sales_customer_sk ON store_sales (ss_customer_sk);
CREATE INDEX idx_store_sales_ticket_number ON store_sales (ss_ticket_number);

-- Index for store_returns table
CREATE INDEX idx_store_returns_customer_sk ON store_returns (sr_customer_sk);
CREATE INDEX idx_store_returns_item_sk ON store_returns (sr_item_sk);
CREATE INDEX idx_store_returns_ticket_number ON store_returns (sr_ticket_number);
CREATE INDEX idx_store_returns_returned_date_sk ON store_returns (sr_returned_date_sk);

-- Index for catalog_sales table
CREATE INDEX idx_catalog_sales_bill_customer_sk ON catalog_sales (cs_bill_customer_sk);
CREATE INDEX idx_catalog_sales_item_sk ON catalog_sales (cs_item_sk);
CREATE INDEX idx_catalog_sales_sold_date_sk ON catalog_sales (cs_sold_date_sk);

-- Index for date_dim table
DROP INDEX idx_date_dim_date_sk on date_dim;
CREATE INDEX idx_date_dim_date_sk ON date_dim (d_date_sk);

select
     i_item_id
     ,i_item_desc
     ,s_store_id
     ,s_store_name
     ,max(ss_net_profit) as store_sales_profit
     ,max(sr_net_loss) as store_returns_loss
     ,max(cs_net_profit) as catalog_sales_profit
 from
     store_sales
     ,store_returns
     ,catalog_sales
     ,date_dim d1
     ,date_dim d2
     ,date_dim d3
     ,store
     ,item
 where
     d1.d_moy = 4
     and d1.d_year = 1999
     and d1.d_date_sk = ss_sold_date_sk
     and i_item_sk = ss_item_sk
     and s_store_sk = ss_store_sk
     and ss_customer_sk = sr_customer_sk
     and ss_item_sk = sr_item_sk
     and ss_ticket_number = sr_ticket_number
     and sr_returned_date_sk = d2.d_date_sk
     and d2.d_moy               between 4 and  10
     and d2.d_year              = 1999
     and sr_customer_sk = cs_bill_customer_sk
     and sr_item_sk = cs_item_sk
     and cs_sold_date_sk = d3.d_date_sk
     and d3.d_moy               between 4 and  10
     and d3.d_year              = 1999
     group by
     i_item_id
     ,i_item_desc
     ,s_store_id
     ,s_store_name
 order by
 i_item_id
 ,i_item_desc
 ,s_store_id
 ,s_store_name
 limit 100;