import csv
import os
from pathlib import Path
from typing import List, Tuple
from dotenv import load_dotenv
import multiprocessing

from src.random import generate_data_row

class IllegalFileError(Exception):
    pass

def get_output_directory() -> str:
    load_dotenv()
    return os.getenv('OUTPUT_DIRECTORY')

def generate_csv_content(number_of_rows: int) -> List[Tuple[str, str]]:
    with multiprocessing.Pool() as pool:
        content = pool.starmap(generate_data_row, [(4, 12) for _ in range(number_of_rows)])
    return content

def generate_csv(filename: str, number_of_rows: int) -> None:
    output_directory = get_output_directory()

    if Path(filename).suffix != '.csv':
        raise IllegalFileError

    with open(f'{output_directory}/{filename}', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(generate_csv_content(number_of_rows))