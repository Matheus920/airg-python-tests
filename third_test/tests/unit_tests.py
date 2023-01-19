from pathlib import Path

from third_test.src.csv import generate_new_csv, get_input_file, get_output_file


def test_input_file_exists():
    assert Path(get_input_file()).is_file()

def test_input_file_is_csv():
    assert Path(get_input_file()).suffix == '.csv'

def test_output_file_exists():
    generate_new_csv()
    assert Path(get_output_file()).is_file()

def test_output_file_is_csv():
    generate_new_csv()
    assert Path(get_input_file()).suffix == '.csv'