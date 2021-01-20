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
    
    
    #Load data
    base_folder=conf['base_folder']
    woningvoorraad=conf['woningvoorraad']
    postcode = conf["cbs_postcode"]
    gemeentenaam = conf["cbs_gemeentenaam"]
    buurtnaam = conf["buurtnaam"]
    


    datahood = DataLoaderHood(base_folder, woningvoorraad, postcode, gemeentenaam, buurtnaam).load_data_woning()

    housing_data = datahood["df"]
    woningvoorraad = datahood["woningvoorraad"]
    postcode = datahood["postcode"]
    gemeentenaam = datahood["gemeentenaam"]
    buurtnaam = datahood["buurtnaam"]
    

    #clean woningvoorraad
    #cleanwoningvoorraad = DataMergeHood().mergehood(woningvoorraad)
    merged_dataset = DataMergeHood().mergehood(datahood["df"], datahood["woningvoorraad"], datahood["postcode"], datahood["gemeentenaam"], datahood["buurtnaam"])

    merged_dataset.to_csv("/Users/Fedde/OneDrive/Documenten/GitHub/ddb_data_viz/data/datahood_data.csv", sep=';' , decimal=",")

    return merged_dataset.head

if __name__ == "__main__":
    # the main function above is called when the script is
    # called from command line
    main()