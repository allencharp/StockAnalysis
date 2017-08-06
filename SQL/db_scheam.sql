DROP TABLE IF EXISTS analysis;
CREATE TABLE analysis
(
	item INT auto_increment PRIMARY KEY,
	stock_code VARCHAR(10),
    stock_name NVARCHAR(10),
    target_price VARCHAR(10),
    rating VARCHAR(10),
    organization VARCHAR(100),
    analyst VARCHAR(100),
    market VARCHAR(20),
    date_time VARCHAR(20)
)