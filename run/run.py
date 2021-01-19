import json
from modules.gemeente import Gemeente


# important: for the above import to work, the package needs to be
# installed in the conda environment using e.g. pip install -e .
# from the package root, or python setup.py develop.
# See https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# for a good guide to this

def main():
    # here goes the pipeline code
    with open('./conf.json', 'r') as f:
        conf = json.load(f)
    
    gemeente = Gemeente.clean_data()
    print(gemeente)


if __name__ == "__main__":
    # the main function above is called when the script is
    # called from command line
    main()