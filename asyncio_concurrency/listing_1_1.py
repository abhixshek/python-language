import requests


response = requests.get("https://www.google.com") # I/O bound web request

items = response.headers.items()

headers = [f'{key}: {header}' for key, header in items] # CPU-bound response processing

formatted_headers = "\n".join(headers) # CPU-bound string concatenation

with open('headers.txt', 'w') as file:
    file.write(formatted_headers) # I/O bound write to disk. # NOTE, both opening a file and writing to it are I/O bound operations


