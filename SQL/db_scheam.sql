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

DROP TABLE IF EXISTS analysis_per_score;
CREATE TABLE analysis_per_score
(
	item INT(11) PRIMARY KEY AUTO_INCREMENT,
    organization NVARCHAR(100) NOT NULL,
    analyst NVARCHAR(100) NOT NULL,
    stock_code VARCHAR(10) NOT NULL,
    date_time VARCHAR(20) NOT NULL,
    tendays_value INT NULL
)
AS
SELECT organization, analyst, stock_code,date_time
FROM analysis GROUP BY organization, analyst,stock_code,date_time