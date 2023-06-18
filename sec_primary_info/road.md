sec_primary:
    > data_bases:

    > sec_archive:
        __init__.py  |
        logg_file : data_processor 
        extract
        transform
        launch |
            extract    : extracter_archive()
                - [ ] - Not Implemented error

            push in db : load_to_db(zip_archive)
            
            packages:
                logg
                sql
            TROUBLES:
                - [x] Dublicates rows : sec_tickers/data_bases.py[Table {column} unique=True]
                - [ ] some data not check
                - [ ] - data started since 2009 year
            FEATURES NEED:
                - [ ] Daily index - (everyday add new perot slinks in spec file) 
                    -  https://www.sec.gov/Archives/edgar/daily-index/2023/QTR2/ (2. Написать   получение отчетов из ежедневного индекса)
    > sec_tickers:
        __init__.py 
        extract
        transform
        launch  

