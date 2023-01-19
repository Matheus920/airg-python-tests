
import argparse
from src.csv import generate_new_csv, guess_csv_format


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='A program to transform a given CSV into a valid one')
    arg_parser.add_argument('-d', '--delimiter', help='The delimiter of the input file', required=False)
    arg_parser.add_argument('-q', '--quote', help='The quote character of the final file', required=False)
    parsed_args = arg_parser.parse_args()
    delimiter = parsed_args.delimiter
    quote = parsed_args.quote

    if not delimiter and not quote:
        delimiter, quote = guess_csv_format()
    elif not delimiter:
        delimiter = '|'
    elif not quote:
        quote = '"'

    generate_new_csv(old_delimiter=delimiter, quote_character=quote)