---
arch: etl
---
main_api:: ["create","read","update","delete"]
           ["extract","transform","load"]

## [[extract]]

main_link:: https://www.sec.gov/Archives/edgar/full-index/

### tasks
1. open Enter link
2. Year
3. for every query
4. parse_info
5. pass to [[transform]]

## [[transform]]

## [[load]]


- [ ] : Daily index - (everyday add new perot slinks in spec file) https://www.sec.gov/Archives/edgar/daily-index/2023/QTR2/
