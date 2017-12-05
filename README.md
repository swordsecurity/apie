# Apie
Test Restful API's using YAML files

# Getting started
(optional) Setup virtualenv
```
mkdir .venv
virtualenv -p python3 .venv/
source .venv/bin/activate
```

Install dependencies from requirements.txt
```
pip3 install -r requirements.txt
```

# Usage
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

# Examples
## Testing GitHub status
```
$ cat github.yaml
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

$ apie.py github.yaml
OK GitHub is online
OK GitHub contains 'Built for developers'
```
