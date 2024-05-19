import pandas as pd



def sec_response_to_df(sec_response):
    df = pd.DataFrame.from_dict(sec_response.json(),
                              orient='index')
    return df




def main(cik_str):

