import json
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
    
    
    #Load housing data

    base_folder=conf['base_folder']
    housing_dataloader = DataLoader(base_folder)
    housing_data = housing_dataloader.load_data()

    return print(housing_data)

if __name__ == "__main__":
    # the main function above is called when the script is
    # called from command line
    main()