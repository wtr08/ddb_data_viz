import pandas as pd
import numpy as np

#class DataMergeHood(object):


class DataMergeMun(object):

    def __init__(self):
        pass

    def merge(self, postcode, gemeentenaam, verkoop, voorraad_woningen, gemeente_flow):

        #1. postcode dataset merge with gemeente dataset -> postcode_gemeente
        postcode_gemeente = pd.merge(postcode, gemeentenaam, how='left', left_on='Gemeente2018', right_on='Gemcode')
        del postcode_gemeente['Gemeente2018']
        postcode_gemeente = postcode_gemeente.drop_duplicates(subset=["Gemeentenaam"], keep="first")
        #2 add verkoop price with gemeente
        postcode_gemeente = pd.merge(postcode_gemeente, verkoop, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')
        postcode_gemeente = postcode_gemeente.drop(['Buurt2018', 'Wijk2018', 'Gemcode'], axis = 1)
        #3 add housing and office stock information
        gemeente_years_price_stock = pd.merge(postcode_gemeente, voorraad_woningen, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')
        gemeente_flow = gemeente_flow.drop(["Verhuismobiliteit","Gemiddeld_aantal_inwoners"], axis=1)
        gemeente_years_price_stock = pd.merge(gemeente_years_price_stock, gemeente_flow, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')
        gemeente_years_price_stock
        pd.set_option('display.max_columns', 132)

        

        return gemeente_years_price_stock