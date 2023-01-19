import csv
import os
from typing import List, Tuple
from dotenv import load_dotenv

load_dotenv()

def get_input_file() -> str:
    return os.getenv('INPUT_FILE')

def get_output_file() -> str:
    return os.getenv('OUTPUT_FILE')

def read_input_csv(delimiter, quote_character) -> List[List[str]]:
    csv_data = list()
    with open(get_input_file(), 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=delimiter, quotechar=quote_character)
        for row in csv_reader:
            csv_data.append(row)

    return csv_data

def generate_new_csv(old_delimiter: str = '|',  quote_character: str = '"', new_delimiter: str = ',') -> None:
    csv_data = read_input_csv(old_delimiter, quote_character)
    
    with open(get_output_file(), 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=new_delimiter, quotechar=quote_character)
        csv_writer.writerows(csv_data)

def guess_csv_format() -> Tuple[str, str]:
    with open(get_input_file(), 'r', newline='') as input_csv:
        dialect = csv.Sniffer().sniff(input_csv.read())
        return dialect.delimiter, dialect.quotechar

        
