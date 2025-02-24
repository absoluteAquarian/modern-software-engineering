# Assignment 3 - PIP PIP Hooray
## Purpose of the Script
The `globe.py` script does the following:
1. Define the paths for the URL to download the data from and the local file directory destination
2. If the data has already been downloaded and extracted, skip the next step
3. Otherwise, attempt to download the compressed `.zip` of the data
   1. If the download was successful, write the `.zip` to disk, extract the files from it and also write them to disk
   2. Otherwise, report that something went wrong
4. Load the population data from the files, then transform the values to population density
   1. If a country is missing population data, assume a population density of zero
5. Convert the population densities to a logarithmic scale to allow for smoother color differences on the globe
6. Create a 3D sphere, map each country to the sphere and finally color them based on the logarithmic population densities
7. Display the sphere, as well as a color index for the logarithmic population densities

## Steps Followed
The steps mentioned below are in line with the instructions for this assignment:
1. Installing required packages based on the source for `globe.py`
    ```commandline
    pip install geopandas pandas numpy requests plotly
    ```
2. Generating the full `all_requirements.txt` file
    ```commandline
    pip freeze > all_requirements.txt
    ```
3. Installing `pipdeptree`
    ```commandline
    pip install pipdeptree
    ```
4. Generating the reduced requirements list `dependency_tree.txt`
    ```commandline
    pipdeptree > dependency_tree.txt
    ```
5. Generating the final `requirements.txt` file
   ```commandline
   pip install pipreqs
   pipreqs . --force --ignore ".venv"
   ```
6. Checking that the packages in `requirements.txt` satisfies the requirements for running `globe.py`
   ```commandline
   pip uninstall -y -r all_requirements.txt
   pip list
   pip install requirements.txt
   ```
7. Verifying that the script works as intended
   ```commandline
   > python globe.py
   Dataset not found. Downloading...
   Download complete.
   Extracting dataset...
   Extraction complete.
   
   Process finished with exit code 0
   ```
8. Re-generating the dependencies via `pipdeptree`
   ```commandline
   pipdeptree > dependency_tree.txt
   ```

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
pipreqs==0.5.0
  - docopt [required: ==0.6.2, installed: 0.6.2]
  - ipython [required: ==8.12.3, installed: 8.12.3]
    - backcall [required: Any, installed: 0.2.0]
    - colorama [required: Any, installed: 0.4.6]
    - decorator [required: Any, installed: 5.2.0]
    - jedi [required: >=0.16, installed: 0.19.2]
      - parso [required: >=0.8.4,<0.9.0, installed: 0.8.4]
    - matplotlib-inline [required: Any, installed: 0.1.7]
      - traitlets [required: Any, installed: 5.14.3]
    - pickleshare [required: Any, installed: 0.7.5]
    - prompt_toolkit [required: >=3.0.30,<3.1.0,!=3.0.37, installed: 3.0.50]
      - wcwidth [required: Any, installed: 0.2.13]
    - Pygments [required: >=2.4.0, installed: 2.19.1]
    - stack-data [required: Any, installed: 0.6.3]
      - asttokens [required: >=2.1.0, installed: 3.0.0]
      - executing [required: >=1.2.0, installed: 2.2.0]
      - pure_eval [required: Any, installed: 0.2.3]
    - traitlets [required: >=5, installed: 5.14.3]
  - nbconvert [required: >=7.11.0,<8.0.0, installed: 7.16.6]
    - beautifulsoup4 [required: Any, installed: 4.13.3]
      - soupsieve [required: >1.2, installed: 2.6]
      - typing_extensions [required: >=4.0.0, installed: 4.12.2]
    - bleach [required: !=5.0.0, installed: 6.2.0]
      - webencodings [required: Any, installed: 0.5.1]
    - defusedxml [required: Any, installed: 0.7.1]
    - Jinja2 [required: >=3.0, installed: 3.1.5]
      - MarkupSafe [required: >=2.0, installed: 3.0.2]
    - jupyter_core [required: >=4.7, installed: 5.7.2]
      - platformdirs [required: >=2.5, installed: 4.3.6]
      - pywin32 [required: >=300, installed: 308]
      - traitlets [required: >=5.3, installed: 5.14.3]
    - jupyterlab_pygments [required: Any, installed: 0.3.0]
    - MarkupSafe [required: >=2.0, installed: 3.0.2]
    - mistune [required: >=2.0.3,<4, installed: 3.1.2]
    - nbclient [required: >=0.5.0, installed: 0.10.2]
      - jupyter_client [required: >=6.1.12, installed: 8.6.3]
        - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
          - platformdirs [required: >=2.5, installed: 4.3.6]
          - pywin32 [required: >=300, installed: 308]
          - traitlets [required: >=5.3, installed: 5.14.3]
        - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
          - six [required: >=1.5, installed: 1.17.0]
        - pyzmq [required: >=23.0, installed: 26.2.1]
        - tornado [required: >=6.2, installed: 6.4.2]
        - traitlets [required: >=5.3, installed: 5.14.3]
      - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
        - platformdirs [required: >=2.5, installed: 4.3.6]
        - pywin32 [required: >=300, installed: 308]
        - traitlets [required: >=5.3, installed: 5.14.3]
      - nbformat [required: >=5.1, installed: 5.10.4]
        - fastjsonschema [required: >=2.15, installed: 2.21.1]
        - jsonschema [required: >=2.6, installed: 4.23.0]
          - attrs [required: >=22.2.0, installed: 25.1.0]
          - jsonschema-specifications [required: >=2023.03.6, installed: 2024.10.1]
            - referencing [required: >=0.31.0, installed: 0.36.2]
              - attrs [required: >=22.2.0, installed: 25.1.0]
              - rpds-py [required: >=0.7.0, installed: 0.23.1]
              - typing_extensions [required: >=4.4.0, installed: 4.12.2]
          - referencing [required: >=0.28.4, installed: 0.36.2]
            - attrs [required: >=22.2.0, installed: 25.1.0]
            - rpds-py [required: >=0.7.0, installed: 0.23.1]
            - typing_extensions [required: >=4.4.0, installed: 4.12.2]
          - rpds-py [required: >=0.7.1, installed: 0.23.1]
        - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
          - platformdirs [required: >=2.5, installed: 4.3.6]
          - pywin32 [required: >=300, installed: 308]
          - traitlets [required: >=5.3, installed: 5.14.3]
        - traitlets [required: >=5.1, installed: 5.14.3]
      - traitlets [required: >=5.4, installed: 5.14.3]
    - nbformat [required: >=5.7, installed: 5.10.4]
      - fastjsonschema [required: >=2.15, installed: 2.21.1]
      - jsonschema [required: >=2.6, installed: 4.23.0]
        - attrs [required: >=22.2.0, installed: 25.1.0]
        - jsonschema-specifications [required: >=2023.03.6, installed: 2024.10.1]
          - referencing [required: >=0.31.0, installed: 0.36.2]
            - attrs [required: >=22.2.0, installed: 25.1.0]
            - rpds-py [required: >=0.7.0, installed: 0.23.1]
            - typing_extensions [required: >=4.4.0, installed: 4.12.2]
        - referencing [required: >=0.28.4, installed: 0.36.2]
          - attrs [required: >=22.2.0, installed: 25.1.0]
          - rpds-py [required: >=0.7.0, installed: 0.23.1]
          - typing_extensions [required: >=4.4.0, installed: 4.12.2]
        - rpds-py [required: >=0.7.1, installed: 0.23.1]
      - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
        - platformdirs [required: >=2.5, installed: 4.3.6]
        - pywin32 [required: >=300, installed: 308]
        - traitlets [required: >=5.3, installed: 5.14.3]
      - traitlets [required: >=5.1, installed: 5.14.3]
    - packaging [required: Any, installed: 24.2]
    - pandocfilters [required: >=1.4.1, installed: 1.5.1]
    - Pygments [required: >=2.4.1, installed: 2.19.1]
    - traitlets [required: >=5.1, installed: 5.14.3]
  - yarg [required: ==0.1.9, installed: 0.1.9]
    - requests [required: Any, installed: 2.32.3]
      - certifi [required: >=2017.4.17, installed: 2025.1.31]
      - charset-normalizer [required: >=2,<4, installed: 3.4.1]
      - idna [required: >=2.5,<4, installed: 3.10]
      - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]
plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.27.1]
  - packaging [required: Any, installed: 24.2]
tinycss2==1.4.0
  - webencodings [required: >=0.4, installed: 0.5.1]
```

## Observations or Issues
1. The provided instructions for the assignment specified to run `pipreqs . --force` to generate the requirements.  
   However, after some brief digging, I discovered that the `.venv\` folder was being checked as well, which caused problems since at least one file was not using UTF-8 encoding.   
   This was fixed by ignoring the directory via an `--ignore ".venv"` option when running `pipreqs`.
2. Step 6 mentions the usage of `pip list`.  More specifically, the instructions for this assignment mentioned that only `pip` should appear in the printed list.  
   However, this did not end up being the case.  I ended up deciding to ignore this since checking for `requirements.txt` being sufficient was more important.
3. The provided instructions for the assignment mentioned that running the script would open the program in a standalone window.  
   However — when I ran it — a new Google Chrome tab was created, supposedly because I already had tabs open in a window.  I decided to just ignore this discrepancy.