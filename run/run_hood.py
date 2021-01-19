import json
import pandas as pd 
from modules.load_data import DataLoaderHood
from modules.clean_data import DataMergeHood   

# important: for the above import to work, the package needs to be
# installed in the conda environment using e.g. pip install -e .
# from the package root, or python setup.py develop.
# See https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# for a good guide to this

def main():
    # here goes the pipeline code
    with open('conf.json', 'r') as f:
        conf = json.load(f)
    
    
    #Load housing data

    #base_folder=conf['base_folder']
    #housing_dataloader = DataLoader(base_folder)
    #housing_data = housing_dataloader.load_data()

    #load woningvoorraad
    woningvoorraad=conf['woningvoorraad']
    woningvoorraad_dataloader = DataLoaderHood(woningvoorraad)
    woningvoorraad = woningvoorraad_dataloader.load_data_woning()

    #clean woningvoorraad
    cleanwoningvoorraad = DataMergeHood().mergehood(woningvoorraad)


    return print(cleanwoningvoorraad)

if __name__ == "__main__":
    # the main function above is called when the script is
    # called from command line
    main()