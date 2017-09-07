DROP TABLE IF EXISTS analysis;
CREATE TABLE analysis
(
	item INT auto_increment PRIMARY KEY,
	stock_code VARCHAR(10),
    stock_name NVARCHAR(10),
    target_price VARCHAR(10),
    rating NVARCHAR(10),
    organization NVARCHAR(100),
    analyst NVARCHAR(100),
    market NVARCHAR(20),
    date_time VARCHAR(20)
);

alter table analysis
add column score_after_10 int NULL