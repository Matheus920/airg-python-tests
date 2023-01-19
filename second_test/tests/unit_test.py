import csv
import os
import pytest

from second_test.src.main import IllegalFileError, generate_csv, generate_data_row, generate_random_number, generate_random_word, get_output_directory

def test_output_directory_exists():
    assert os.path.isdir(get_output_directory())

def test_word_has_expected_letters():
    assert len(generate_random_word(10)) == 10

def test_number_has_expected_digits():
    assert len(generate_random_number(10)) == 10

def test_data_row_has_expected_letters_and_digits():
    row_data = generate_data_row(number_digits=10, word_length=10)
    assert len(row_data[0]) == 10 and len(row_data[1]) == 10

def test_generated_csv_has_expected_number_of_rows():
    generate_csv('unit_test_number_of_rows.csv', 1000)

    records_len = 0
    with open(get_output_directory() + '/unit_test_number_of_rows.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for _ in csv_reader:
            records_len = records_len + 1

    assert records_len == 1000

def test_invalid_csv_extension():
    with pytest.raises(IllegalFileError):
        generate_csv('unit_test_number_of_rows.pdf', 1000)