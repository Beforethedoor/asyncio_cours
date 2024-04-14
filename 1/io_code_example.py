import requests
import time


def get_example_data(url: str) -> str:
    response = requests.get(url)
    items = response.headers.items()
    headers = [f'{key}: {header}' for key, header in items]
    format_headers = '\n'.join(headers)
    return format_headers


start = time.time()

get_example_data('https://www.example.com')

end = time.time()

print(end - start)
