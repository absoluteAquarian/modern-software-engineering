# Assignment 3 - PIP PIP Hooray
## Purpose of the Script


## Steps Followed
The steps mentioned below are in line with the instructions for this assignment:
1. Installation of required packages based on the source for `globe.py`
    ```commandline
    pip install geopandas pandas numpy requests plotly
    ```
2. Generation of the full `all_requirements.txt` file
    ```commandline
    pip freeze > all_requirements.txt
    ```
3. Installation of `pipdeptree`
    ```commandline
    pip install pipdeptree
    ```
4. Generation of the reduced requirements list `dependency_tree.txt`
    ```commandline
    pipdeptree > dependency_tree.txt
    ```
5. Generation of the final `requirements.txt` file
   ```commandline
   pipreqs . --force --ignore ".venv"
   ```
6. Checking that the packages in `requirements.txt` satisfies the requirements for running `globe.py`
   ```commandline
   pip uninstall -y -r all_requirements.txt
   pip list
   pip install requirements.txt
   ```
7. TODO

## Output of `pipdeptree`
```
geopandas==1.0.1
  - numpy [required: >=1.22, installed: 2.2.3]
  - packaging [required: Any, installed: 24.2]
  - pandas [required: >=1.4.0, installed: 2.2.3]
    - numpy [required: >=1.26.0, installed: 2.2.3]
    - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
      - six [required: >=1.5, installed: 1.17.0]
    - pytz [required: >=2020.1, installed: 2025.1]
    - tzdata [required: >=2022.7, installed: 2025.1]
  - pyogrio [required: >=0.7.2, installed: 0.10.0]
    - certifi [required: Any, installed: 2025.1.31]
    - numpy [required: Any, installed: 2.2.3]
    - packaging [required: Any, installed: 24.2]
  - pyproj [required: >=3.3.0, installed: 3.7.1]
    - certifi [required: Any, installed: 2025.1.31]
  - shapely [required: >=2.0.0, installed: 2.0.7]
    - numpy [required: >=1.14,<3, installed: 2.2.3]
pipdeptree==2.25.0
  - packaging [required: >=24.1, installed: 24.2]
  - pip [required: >=24.2, installed: 25.0.1]
plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.27.1]
  - packaging [required: Any, installed: 24.2]
requests==2.32.3
  - certifi [required: >=2017.4.17, installed: 2025.1.31]
  - charset-normalizer [required: >=2,<4, installed: 3.4.1]
  - idna [required: >=2.5,<4, installed: 3.10]
  - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]
```

## Observations or Issues
1. The provided instructions for the assignment specified to run `pipreqs . --force` to generate the requirements.  
   However, after some brief digging, I discovered that the `.venv\` folder was being checked as well, which caused problems since at least one file was not using UTF-8 encoding.   
   This was fixed by ignoring the directory via an `--ignore ".venv"` option when running `pipreqs`.
2. Step 6 mentions the usage of `pip list`.  More specifically, the instructions for this assignment mentioned that only `pip` should appear in the printed list.  
   However, this did not end up being the case.  I ended up deciding to ignore this since checking for `requirements.txt` being sufficient was more important.