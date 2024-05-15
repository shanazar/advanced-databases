-- Index for store_sales table
CREATE INDEX idx_store_sales ON store_sales (ss_sold_date_sk, ss_item_sk, ss_cdemo_sk, ss_promo_sk, ss_quantity, ss_list_price, ss_coupon_amt, ss_sales_price);

-- Index for customer_demographics table
CREATE INDEX idx_customer_demographics ON customer_demographics (cd_demo_sk, cd_gender, cd_marital_status, cd_education_status);

-- Index for date_dim table
CREATE INDEX idx_date_dim ON date_dim (d_date_sk, d_year);

-- Index for item table
CREATE INDEX idx_item ON item (i_item_sk, i_item_id);

-- Index for promotion table
CREATE INDEX idx_promotion ON promotion (p_promo_sk, p_channel_email, p_channel_event);

select  i_item_id,
        avg(ss_quantity) agg1,
        avg(ss_list_price) agg2,
        avg(ss_coupon_amt) agg3,
        avg(ss_sales_price) agg4
 from store_sales, customer_demographics, date_dim, item, promotion
 where ss_sold_date_sk = d_date_sk and
       ss_item_sk = i_item_sk and
       ss_cdemo_sk = cd_demo_sk and
       ss_promo_sk = p_promo_sk and
       cd_gender = 'F' and
       cd_marital_status = 'W' and
       cd_education_status = 'College' and
       (p_channel_email = 'N' or p_channel_event = 'N') and
       d_year = 2001
 group by i_item_id
 order by i_item_id
 limit 100;