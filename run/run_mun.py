import json
from modules.load_data import DataLoaderMun
from modules.clean_data import DataMergeMun   

# important: for the above import to work, the package needs to be
# installed in the conda environment using e.g. pip install -e .
# from the package root, or python setup.py develop.
# See https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# for a good guide to this

def main():
    # here goes the pipeline code
    with open(r'./conf.json', 'r') as f:
        conf = json.load(f)
    
    
    #Load CBS data
    cbs_postcode=conf['cbs_postcode']
    cbs_gemeentenaam=conf['cbs_gemeentenaam']
    cbs_verkoop=conf['cbs_verkoop']
    cbs_voorraad_woningen=conf['cbs_voorraad_woningen']
    cbs_gemeente_flow = conf["gemeente_flow"]
    wijken = conf["wijkenbuurten"]
    
    Data = DataLoaderMun(cbs_postcode, cbs_gemeentenaam, cbs_verkoop, cbs_voorraad_woningen, cbs_gemeente_flow, wijken).load_cbs()

    postcode = Data["postcode"]
    gemeentenaam = Data["gemeentenaam"]
    verkoop = Data["verkoop"]
    voorraad_woningen = Data["voorraad_woningen"]
    gemeente_flow = Data["gemeente_flow"]
    wijken = Data["wijken"]

    #merge data
    merged_dataset = DataMergeMun().merge(Data["postcode"], Data["gemeentenaam"], Data["verkoop"], Data["voorraad_woningen"], Data["gemeente_flow"], Data["wijken"])

    merged_dataset.to_csv("/Users/Fedde/OneDrive/Documenten/GitHub/ddb_data_viz/data/datamunicipality_data.csv", sep=';' , decimal=",")

    return merged_dataset

if __name__ == "__main__":
    # the main function above is called when the script is
    # called from command line
    main()