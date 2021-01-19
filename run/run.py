import json
from modules.gemeente import Gemeente
from modules.load_data import DataLoader, CBSdataloader
from modules.clean_data import DataMerge   

# important: for the above import to work, the package needs to be
# installed in the conda environment using e.g. pip install -e .
# from the package root, or python setup.py develop.
# See https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# for a good guide to this

def main():
    # here goes the pipeline code
    with open(r'C:\Users\Fedde\OneDrive\Documenten\GitHub\ddb_data_viz\run\conf.json', 'r') as f:
        conf = json.load(f)
    
    #gemeente = Gemeente.clean_data()
    #print(gemeente)


    #Load housing data

    base_folder=conf['base_folder']
    housing_dataloader = DataLoader(base_folder)
    housing_data = housing_dataloader.load_data()

    #Load CBS data
    cbs_postcode=conf['cbs_postcode']
    cbs_gemeentenaam=conf['cbs_gemeentenaam']
    cbs_verkoop=conf['cbs_verkoop']
    cbs_voorraad_woningen=conf['cbs_voorraad_woningen']
    cbs_dataloader = CBSdataloader(cbs_postcode, cbs_gemeentenaam, cbs_verkoop, cbs_voorraad_woningen)
    cbs_data = cbs_dataloader.load_cbs(cbs_postcode, cbs_gemeentenaam, cbs_verkoop, cbs_voorraad_woningen)

    #merge datA
    merge_price_stock = DataMerge().merge(cbs_data[0], cbs_data[1], cbs_data[2], cbs_data[3])


    return print(merge_price_stock)

if __name__ == "__main__":
    # the main function above is called when the script is
    # called from command line
    main()