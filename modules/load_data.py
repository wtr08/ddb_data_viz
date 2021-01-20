import pandas as pd
import numpy as np
import os

class DataLoaderHood(object):

     def __init__(self, base_folder, woningvoorraad, cbs_postcode, cbs_gemeentenaam, cbs_buurtnaam):
         self.base_folder = base_folder
         self.woningvoorraad = woningvoorraad
         self.cbs_postcode = cbs_postcode
         self.cbs_gemeentenaam = cbs_gemeentenaam
         self.cbs_buurtnaam = cbs_buurtnaam
         

     def load_data_woning(self):
         df = pd.read_csv(self.base_folder, sep = ',', encoding = 'utf-8')
         woningvoorraad = pd.read_csv(self.woningvoorraad, sep = ';')
         postcode = pd.read_csv(self.cbs_postcode, sep = ';', encoding = 'utf-8')
         gemeentenaam = pd.read_csv(self.cbs_gemeentenaam, sep = ';')
         buurtnaam = pd.read_csv(self.cbs_buurtnaam, sep = ';')
         


         return {
            "df" : df,
            "woningvoorraad" : woningvoorraad,
            "postcode" : postcode,
            "gemeentenaam" : gemeentenaam,
            "buurtnaam" : buurtnaam
            }
    
        
class DataLoaderMun(object):

    def __init__(self, cbs_postcode, cbs_gemeentenaam, cbs_verkoop, cbs_voorraad_woningen, cbs_gemeente_flow, cbs_wijkenbuurten):
        self.cbs_postcode = cbs_postcode
        self.cbs_gemeentenaam = cbs_gemeentenaam
        self.cbs_verkoop = cbs_verkoop
        self.cbs_voorraad_woningen = cbs_voorraad_woningen
        self.cbs_gemeente_flow = cbs_gemeente_flow
        self.cbs_wijkenbuurten = cbs_wijkenbuurten 


    def load_cbs(self):

        postcode = pd.read_csv(self.cbs_postcode, sep = ';')
        gemeentenaam = pd.read_csv(self.cbs_gemeentenaam, sep = ';')
        verkoop = pd.read_csv(self.cbs_verkoop, sep = ';')
        voorraad_woningen = pd.read_csv(self.cbs_voorraad_woningen, sep = ';')
        cbs_gemeente_flow = pd.read_csv(self.cbs_gemeente_flow, sep = ';')
        wijken = pd.read_csv(self.cbs_wijkenbuurten, sep = ';')

        return {
            "postcode" : postcode, 
            "gemeentenaam" : gemeentenaam,
            "verkoop" : verkoop,
            "voorraad_woningen" : voorraad_woningen,
            "gemeente_flow" : cbs_gemeente_flow,
            "wijken" : wijken
            }