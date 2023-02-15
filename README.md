# Codeforces API

This is my attempt at some python web scraping. I will scrape the data from the Codeforces website and this can be accessed by making an API call to a REST endpoint I created using flask.

> The motive of this project is to aid a CP specific editor. I've been making some prototypes of it using PyQt6 on the [```orange/editor```](https://github.com/Abhijna-Raghavendra/CodeforcesAPI/tree/orange/editor) branch. Take a look at that if it interests you.

### Setup

- Clone the repository and access the project directory
  ```sh
    git clone https://github.com/Abhijna-Raghavendra/CodeforcesAPI.git
    cd CodeforcesAPI
  ```
- Create and activate your virtual environment
  > Make sure you have [python](https://www.python.org/downloads/) installed in your computer before proceeding
  ```sh
    python3 -m venv virtenv
  ```
  ```sh
    # In Windows cmd
    virtenv\Scripts\activate.bat
    # In Windows PowerShell
    virtenv\Scripts\Activate.ps1
    # In Linux or MacOS
    source virtenv/Scripts/activate
  ``` 
- Install required dependencies
  ```sh
  (virtenv)
    pip install -r requirements.txt
  ```
- Run the flask server
  ```sh
  (virtenv)
    python api.py
  ```

### Usage

Once the flask server is up and running on ```localhost:5000```, open a browser window and visit ```http://127.0.0.1:5000/scrape/{question}```

> The ```{question}``` must be valid and of the form "1729-A", where a "-" seperates the letter from the number.

Enjoy!! :heart: