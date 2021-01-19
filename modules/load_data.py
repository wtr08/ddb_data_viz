import pandas as pd
import numpy as np
import os

class DataLoaderHood(object):

     def __init__(self, woningvoorraad):
         #self.base_folder = base_folder
         self.woningvoorraad = woningvoorraad

     def load_data_woning(self):
         #import Data
         #df = pd.read_csv(self.base_folder)
         woningvoorraad = pd.read_csv(self.woningvoorraad, sep = ';')
         return {
            "woningvoorraad" : woningvoorraad
            }
    
        
class DataLoaderMun(object):

    def __init__(self, cbs_postcode, cbs_gemeentenaam, cbs_verkoop, cbs_voorraad_woningen, cbs_gemeente_flow):
        self.cbs_postcode = cbs_postcode
        self.cbs_gemeentenaam = cbs_gemeentenaam
        self.cbs_verkoop = cbs_verkoop
        self.cbs_voorraad_woningen = cbs_voorraad_woningen
        self.cbs_gemeente_flow = cbs_gemeente_flow


    def load_cbs(self):

        postcode = pd.read_csv(self.cbs_postcode, sep = ';')
        gemeentenaam = pd.read_csv(self.cbs_gemeentenaam, sep = ';')
        verkoop = pd.read_csv(self.cbs_verkoop, sep = ';')
        voorraad_woningen = pd.read_csv(self.cbs_voorraad_woningen, sep = ';')
        cbs_gemeente_flow = pd.read_csv(self.cbs_gemeente_flow, sep = ';')
        
        return {
            "postcode" : postcode, 
            "gemeentenaam" : gemeentenaam,
            "verkoop" : verkoop,
            "voorraad_woningen" : voorraad_woningen,
            "gemeente_flow" : cbs_gemeente_flow
            }