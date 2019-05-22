import pandas as pd
import glob
import argparse

def merge_csvs_in_dir(dir_path, result_csv_name):
    all_files = glob.glob(dir_path + "/*.csv")
    merge_csvs(all_files, result_csv_name)


def merge_csvs(csv_paths, save_to_path):
    df = pd.concat((pd.read_csv(f) for f in csv_paths))
    pd.DataFrame.to_csv(df, save_to_path, index=False)

# TODO: Add argparser
# parser = argparse.ArgumentParser()
# parser.add_argument('-dir', help='location of the directory that contains all the csv\'s to merge')
# args = parser.parse_args()

# TODO: Delete this
dir = "H:\#Masterarbeit\Datasets\Inner_Wear"
target = "H:\#Masterarbeit\Datasets\Inner_Wear\#inner_wear.csv"
merge_csvs_in_dir(dir, target)
