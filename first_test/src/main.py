import requests
from dotenv import load_dotenv
import os
from typing import List

class EndOfPagesError(Exception):
    pass

def get_api_host() -> str:
    load_dotenv()
    return os.getenv('API_HOST')

def make_api_request(page: int = 1) -> requests.Response:
    API_HOST = get_api_host()
    vehicles_api_response = requests.get(API_HOST + f'/?page={page}')
    return vehicles_api_response

def parse_api_response(api_response: requests.Response) -> dict:
    if api_response.status_code == 404:
        raise EndOfPagesError
    response_content = api_response.json()
    return response_content.get('results')

def get_distinct_manufacturers(api_pagination: int) -> List[str]:
    vehicles = parse_api_response(make_api_request(api_pagination))
    manufacturers = [vehicle.get('manufacturer') for vehicle in vehicles]
    distinct_manufacturers = list(dict.fromkeys(manufacturers))
    return distinct_manufacturers

def get_manufacturers_names(manufacturers_length: int = 5) -> List[str]:
    number_of_requests = 0
    distinct_manufacturers = list()

    while len(distinct_manufacturers) < manufacturers_length:
        try:
            distinct_manufacturers = distinct_manufacturers + get_distinct_manufacturers(number_of_requests + 1)
            number_of_requests = number_of_requests + 1
        except EndOfPagesError:
            break
    
    manufacturers_subset = distinct_manufacturers[0:manufacturers_length]

    return manufacturers_subset


if __name__ == '__main__':
    print(get_manufacturers_names())
