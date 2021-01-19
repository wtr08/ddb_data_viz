import pandas as pd
import numpy as np
import os

class DataLoader(object):

    def __init__(self, base_folder):
        self.base_folder = base_folder

    def load_data(self):
        #import Data
        df = pd.read_csv(self.base_folder)
        
class CBSdataloader(object):

    def __init__(self, cbs_postcode, cbs_gemeentenaam, cbs_verkoop, cbs_voorraad_woningen):
        self.cbs_postcode = cbs_postcode
        self.cbs_gemeentenaam = cbs_gemeentenaam
        self.cbs_verkoop = cbs_verkoop
        self.cbs_voorraad_woningen = cbs_voorraad_woningen


    def load_cbs(self, cbs_postcode, cbs_gemeentenaam, cbs_verkoop, cbs_voorraad_woningen):

        postcode = pd.read_csv(self.cbs_postcode, sep = ';')
        gemeentenaam = pd.read_csv(self.cbs_gemeentenaam, sep = ';')
        verkoop = pd.read_csv(self.cbs_verkoop, sep = ';')
        voorraad_woningen = pd.read_csv(self.cbs_voorraad_woningen, sep = ';')


        return postcode, gemeentenaam, verkoop, voorraad_woningen