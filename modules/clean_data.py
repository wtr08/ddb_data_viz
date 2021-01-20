import pandas as pd
import numpy as np

class DataMergeHood(object):
    def __init__(self):
        pass

    def mergehood(self, df, woningvoorraad, postcode, gemeentenaam, buurtnaam):



        #1. postcode dataset merge with gemeente dataset -> postcode_gemeente
        postcode_gemeente = pd.merge(postcode, gemeentenaam, how='left', left_on='Gemeente2018', right_on='Gemcode')
        del postcode_gemeente['Gemeente2018']
        #2. postcode dataset merge with buurtnaam dataset -> postcode_buurt
        postcode_buurt = pd.merge(postcode, buurtnaam, how='left', left_on='Buurt2018', right_on='Buurtcode')
        del postcode_buurt['Buurt2018']
        # postcode_buurt merge with postcode_gemeente
        postcode_gemeente_buurt = pd.merge(postcode_buurt, postcode_gemeente, how='left', left_on='PC6', right_on='PC6')
        postcode_gemeente_buurt = postcode_gemeente_buurt.drop(['Wijk2018_x', 'Gemeente2018', 'Buurt2018', 'Wijk2018_y', 'Gemcode'], axis=1)
        postcode_gemeente_buurt = pd.merge(df, postcode_gemeente_buurt, how='left', left_on='postcode', right_on='PC6')
        postcode_gemeente_buurt = postcode_gemeente_buurt[postcode_gemeente_buurt['Gemeentenaam'].notna()]
        postcode_gemeente_buurt = postcode_gemeente_buurt.drop(['postcode'], axis=1)
        postcode_gemeente_buurt_oppervlakte = postcode_gemeente_buurt.groupby(['Buurtnaam', 'Gemeentenaam', 'Buurtcode'])['oppervlakte'].mean().reset_index()

        woningvoorraad = woningvoorraad.drop(['Afstand_tot_school_km', 'Afstand_tot_kinderdagverblijf_km', 'Afstand_tot_grote_supermarkt_km', 'Afstand_tot_huisartsenpraktijk_km', 'Geweld', 'Vernieling', 'Diefstal_uit_woning', 'Soort_regio', 'Wijken_en_buurten'], axis=1)        
        postcode_gemeente_buurt = pd.merge(postcode_gemeente_buurt_oppervlakte, woningvoorraad, how='left', left_on='Buurtcode', right_on='codering')
        postcode_gemeente_buurt = postcode_gemeente_buurt.drop(['Gemeentenaam_y', 'codering'], axis=1)

        postcode_gemeente_buurt = pd.merge(postcode_gemeente_buurt, postcode, how='left', left_on='Buurtcode', right_on='Buurt2018')
        postcode_gemeente_buurt = postcode_gemeente_buurt.drop(['Buurt2018', 'Wijk2018', 'Gemeente2018'], axis=1)

        return postcode_gemeente_buurt




class DataMergeMun(object):

    def __init__(self):
        pass

    def merge(self, postcode, gemeentenaam, verkoop, voorraad_woningen, gemeente_flow, wijken):

        #1. postcode dataset merge with gemeente dataset -> postcode_gemeente
        postcode_gemeente = pd.merge(postcode, gemeentenaam, how='left', left_on='Gemeente2018', right_on='Gemcode')
        del postcode_gemeente['Gemeente2018']
        postcode_gemeente = postcode_gemeente.drop_duplicates(subset=["Gemeentenaam"], keep="first")
        #2 add verkoop price with gemeente
        postcode_gemeente = pd.merge(postcode_gemeente, verkoop, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')
        postcode_gemeente = postcode_gemeente.drop(['Buurt2018', 'Wijk2018'], axis = 1)
        #3 add housing and office stock information
        gemeente_years_price_stock = pd.merge(postcode_gemeente, voorraad_woningen, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')
        gemeente_flow = gemeente_flow.drop(["Verhuismobiliteit","Gemiddeld_aantal_inwoners"], axis=1)
        gemeente_years_price_stock = pd.merge(gemeente_years_price_stock, gemeente_flow, how='left', left_on='Gemeentenaam', right_on='Gemeentenaam')
        pd.set_option('display.max_columns', 132)

        wijken = wijken.drop(['Wijken_en_buurten', 'Gemeentenaam', 'Soort_regio', 'Mannen', 'Vrouwen', '0tot15', '15tot25', '25tot45', '45tot65', '65jaarofouder', 'Gemiddeld_inkomen_per_inwoner'], axis=1)
        merge = pd.merge(gemeente_years_price_stock, wijken, how='left', left_on='Gemcode', right_on='Codering')
        del merge['Codering']
        return merge
