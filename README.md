<img style="max-height:120px;" src="./docs/assets/logo.png"><br><br>

# Restbot: Test Restful JSON API's using YAML files
## Features
- Write test script in YAML.
- GET, POST, PUT, DELETE requests supported.
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
cd restbot/restbot
sudo pip3 install -r requirements.txt
```

## Usage
```
usage: restbot.py [-h] [--headers-script HEADERS_SCRIPT] [--sample SAMPLE]
                  [--sample-header SAMPLE_HEADER] [-i] [-e]
                  test_script

positional arguments:
  test_script           Test script (.yaml)

optional arguments:
  -h, --help            show this help message and exit
  --headers-script HEADERS_SCRIPT
                        Headers script, using name,value format (.yaml)
  --sample SAMPLE       Show sample of tests YAML file
  --sample-header SAMPLE_HEADER
                        Show sample of headers YAML file
  -i, --insecure        Do not verify SSL certificates (insecure)
  -e, --errors          Show only errors
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
```

Example usage restbot:
```
$ python restbot/restbot.py ./github.yaml
Test: GitHub is online
Result: OK

Test: GitHub contains 'Built for developers'
Result: OK
```

## How to write a test file?
A test file needs the following:

| | |
|-|-|
| **url**   | url of API endpoint       |
| **tests** | list of specified tests   |

### Tests
The following parameters need to be used in a test:

| | |
|-|-|
| **name** | name of the test |
| **request** | type of request (GET,POST,PUT,DELETE) |
| **path** | path to endpoint |
| **expected_status** (optional) | expected status code |
| **expected_content** (optional) | expected value in response (case-insensitive) |
| **expected_value** (optional) | expected exact value |
| **sleep** (optional) | sleep specified seconds after test |
| **headers** (optional) | list of specified headers |

#### Headers (optional)
The following format is used to define headers in a test:

| | |
|-|-|
| **name** | name of the header |
| **value** | value of the header |


## Extra's
### Header file (--headers-script)
Specify a file to load headers from. The format Headers (see Headers) is used to define headers that are used in each test.

### Sample test script (--sample-script)
Use--sample-script to show a sample of a working test script.

### Sample header script (--sample-header-script)
Use --sample-header-script to show a sample of a working header script.

## License
Licensed under AGPL3.
