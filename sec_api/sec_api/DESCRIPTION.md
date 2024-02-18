## SRC
- [ ]:: "https://www.sec.gov/files/company_tickers.json"            :: companyData
- [ ]:: 'https://data.sec.gov/submissions/CIK{cik}.json'            :: allForms     :: only limited (2013 INTEL)
- [ ]:: 'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'  :: companyFacts

##
arg_name:: companyData
columns::
    cik_str	
    ticker	
    title