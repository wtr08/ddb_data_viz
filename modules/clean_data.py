import pandas as pd
import numpy as np

class DataMerge(object):

    def __init__(self):
        pass

    def merge(self, postcode, gemeentenaam, verkoop, voorraad_woningen):

        #1. postcode dataset merge with gemeente dataset -> postcode_gemeente
        postcode_gemeente = pd.merge(postcode, gemeentenaam, how='left', left_on='Gemeente2018', right_on='Gemcode')
        del postcode_gemeente['Gemeente2018']
        postcode_gemeente = postcode_gemeente.drop_duplicates(subset=["Gemeentenaam"], keep="first")
        #2 add verkoop price with gemeente
        postcode_gemeente = pd.merge(postcode_gemeente, verkoop, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')
        postcode_gemeente = postcode_gemeente.drop(['Buurt2018', 'Wijk2018', 'Gemcode'], axis = 1)
        #3 add housing and office stock information
        gemeente_years_price_stock = pd.merge(postcode_gemeente, voorraad_woningen, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')

        return gemeente_years_price_stock