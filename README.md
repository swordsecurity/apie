<div align="center">
  <img src="./docs/assets/logo.png"><br><br>
</div>

# Restbot: Test Restful JSON API's using YAML files

## Features
- Write test script in YAML.
- GET, POST, PUT, DELETE requests.
- Supports JWT Authentication.
- Assert with status, content (includes, case-insensitive) or value (exact match)

## Prerequisites
To run Restbot, you will need the following:
- git
- python3
- pip3

## Installation
Install dependencies from requirements.txt
```
git clone [this repository]
pip3 install -r requirements.txt
```

## Usage
```
usage: apie.py [-h] [--header_file HEADER_FILE]
               [--example_test_file EXAMPLE_TEST_FILE]
               [--example_header_file EXAMPLE_HEADER_FILE]
               file

positional arguments:
  file                  Tests YAML file

optional arguments:
  -h, --help            show this help message and exit
  --header_file HEADER_FILE
                        Headers YAML file
  --example_test_file EXAMPLE_TEST_FILE
                        Show example tests YAML file
  --example_header_file EXAMPLE_HEADER_FILE
                        Show example headers YAML file
```

## Examples
Example test script (github.yaml):
```
url: "https://github.com"
tests:
    - name: "GitHub is online"
      request: 'GET'
      path: '/'
      expected_status: 200
    - name: "GitHub contains 'Built for developers'"
      request: 'GET'
      path: '/'
      expected_content: "Built for developers"

$ restbot.py github.yaml
OK GitHub is online
OK GitHub contains 'Built for developers'
```
