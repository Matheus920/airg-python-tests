from first_test.src.main import get_api_host, get_distinct_manufacturers, get_manufacturers_names, make_api_request, parse_api_response


def test_api_host_exists():
    assert get_api_host() is not None

def test_api_response_returns_ok():
    assert make_api_request().status_code == 200

def test_api_response_returns_not_found():
    assert make_api_request(-1).status_code == 404

def test_api_parsing_returns_data():
    assert len(parse_api_response(make_api_request(1))) > 0

def test_manufacturers_are_distinct():
    assert len(set(get_distinct_manufacturers(1))) == len(get_distinct_manufacturers(1))

def tests_expected_number_of_manufacturers():
    assert len(get_manufacturers_names(5)) == 5