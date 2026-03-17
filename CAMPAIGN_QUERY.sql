use msdb

create table campaign 
(Date varchar(40) ,Channel varchar(200),
Impressions int,Clicks int,
Conversions int,Spend int);

--inserting bulk data
bulk insert campaign
from 'C:\Users\kuche\OneDrive\Desktop\aARATI\CAMPAIGN_DATA.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001', -- This specifies UTF-8 encoding
    TABLOCK
);

select * from campaign;

----KPI CALCULATIONS
select Channel,
       sum(Impressions) as total_impressions,
	   sum (Clicks) as total_clicks,
	   sum(Conversions) as total_conversions,
	   sum(Spend) as total_spend,
	   sum (Clicks)*1.0/sum(Impressions) as CTR,
	   sum(Conversions) * 1.0/sum (Clicks) as CVR,
	   sum(Spend) * 1.0/sum(Conversions) as CPC,
	   sum(Conversions) * 100/sum(Spend) as ROAS
from campaign 
group by Channel;


--FUNNEL VIEW
SELECT Channel ,SUM(Impressions) as total_impressions,
       sum(Clicks) as total_clicks,
	   sum(Conversions) as total_conversions
from campaign
group by Channel


---DAILY TRENDS 
SELECT Date,SUM(Impressions) as total_impressions,
       sum(Clicks) as total_clicks,
	   sum(Conversions) as total_conversions
 from  campaign
group by Date
order by Date
       