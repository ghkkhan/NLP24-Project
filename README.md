Repository for working on the Movie Database project with Trey and Huzaifa

## HOW TO RUN 

1) Create virtual environment:
`python -m venv myenv`

2) Activate 
`source myenv/bin/activate #on linux/macos` 
`# or`
`myenv/Scripts/activate #on windows` 

3) Install Dependencies 
`pip install -r requirements.txt` 

4) Download spacy en_core_web_sm model 
`python -m spacy download en_core_web_sm`

5) Set environment variable TMDB_AUTH to your TMDB API key
+ This can be done through https://www.themoviedb.org/?language=en-US
`export TMDB_AUTH={YOUR KEY HERE} # on linux/macos for temporary use`

5) Run
`python spacy_test.py`

## Requirements to run spacy_test.py
set environment variable tmdb_api_key to the api key 