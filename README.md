<div align="center">
  <img src="./docs/assets/logo.png"><br><br>
</div>

# Restbot: Test Restful JSON API's using YAML files
## Features
- Write test script in YAML.
- GET, POST, PUT, DELETE requests.
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
usage: restbot.py [-h] [--header_file HEADER_FILE]
                  [--example_script EXAMPLE_SCRIPT]
                  [--example_header_file EXAMPLE_HEADER_FILE]
                  filename
```

## Test file
A test file needs the following:
| key | value |
|-|-|-|
| **url** (required)   | url of API endpoint       |
| **tests** (required) | list of specified tests   |

### Tests
The following parameters need to be used in a test:
--- | ---
| **name** | name of the test |
| **request** | type of request (GET,POST,PUT,DELETE) |
| **path** | path to endpoint |
| **expected_status** (optional) | expected status code |
| **expected_content** (optional) | expected value in response (case-insensitive) |
| **expected_value** (optional) | expected exact value |
| **headers** (optional) | list of specified headers |

#### Headers
The following format is used to define headers in a test:
--- | ---
| **name** | name of the header |
| **value** | value of the header |

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
$ restbot.py ~/Downloads/github-it/github.yaml
Test: GitHub is online
Result: OK

Test: GitHub contains 'Built for developers'
Result: OK
```
