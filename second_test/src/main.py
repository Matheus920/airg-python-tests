import argparse

from src.csv import generate_csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for creating a csv with random data.')
    parser.add_argument('-f', '--filename', help='A csv filename for the output (.csv required in filename)', type=str)
    parser.add_argument('-r', '--rows', help='Number of rows to fill the .csv', type=int)
    args = parser.parse_args()
    generate_csv(filename=args.filename, number_of_rows=args.rows)
