SELECT COUNT(*)
FROM report_liks;

SELECT DISTINCT(tickers_table.ticker),title, report_liks.cik
FROM tickers_table
INNER JOIN report_liks
	ON report_liks.cik = tickers_table.cik

ORDER BY ticker;

SELECT tickers_table.ticker, title,tickers_table.cik, url_report
FROM tickers_table
INNER JOIN report_liks
	ON report_liks.cik = tickers_table.cik
WHERE ticker ='AAL';

SELECT DISTINCT(tickers_table.ticker),title, report_liks.cik,url_report
FROM tickers_table
FULL OUTER JOIN report_liks
	ON report_liks.cik = tickers_table.cik
WHERE report_liks.url_report is NULL or report_liks.cik is NULL
ORDER BY ticker;

SELECT tickers_table.ticker, title,tickers_table.cik, url_report
FROM tickers_table
INNER JOIN report_liks
	ON report_liks.cik = tickers_table.cik
WHERE ticker ='ZG';

SELECT tickers_table.ticker, title,tickers_table.cik, url_report
FROM tickers_table
FULL OUTER JOIN report_liks
	ON report_liks.cik = tickers_table.cik
WHERE report_liks.cik ='0001617640';

SELECT DISTINCT(url_report)
FROM tickers_table
FULL OUTER JOIN report_liks
	ON report_liks.cik = tickers_table.cik
WHERE report_liks.cik ='0001617640';

select DISTINCT(report_liks.cik),report_liks.url_report,title,date_publication,ticker
FROM tickers_table
FULL OUTER JOIN report_liks
	ON report_liks.cik = tickers_table.cik
Where tickers_table.title='Janux Therapeutics, Inc.'
ORDER BY date_publication
