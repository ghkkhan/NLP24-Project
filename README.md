Repository for working on the Movie Database project with Trey and Huzaifa

## HOW TO RUN 

1) Create virtual environment:
```
python -m venv myenv
```

2) Activate 
```
source myenv/bin/activate #on linux/macos
# or
myenv/Scripts/activate #on windows 
```

3) Install Dependencies 
```
pip install -r requirements.txt
```

4) Download spacy en_core_web_sm model 
```
python -m spacy download en_core_web_sm
```

5) Set environment variable TMDB_AUTH to your TMDB API key
+ This can be done through https://www.themoviedb.org/?language=en-US
```
export TMDB_AUTH={YOUR KEY HERE} # on linux/macos for temporary use
```

6) Obtain aclImdb folder and place in project root 
+ Download through https://ai.stanford.edu/~amaas/data/sentiment/

7) Run
```
python main.py {arg} # 0 for movie_reviews nltk corpus or 1 for IMDB random files

```

