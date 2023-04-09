# Hangman

![Screenshot from 2023-04-09 11-52-03](https://user-images.githubusercontent.com/71731579/230766856-ea4aef6e-a640-4a37-8b28-3afaf207493a.png)

Object-Oriented console version of the classic Hangman game. The user is handled a word and has 'N' number
of attempts to guess the word.



## How to run

### Prerequisites
- postgresql installed and configured
- postgresql table with the following credentials:


    ``` CREATE TABLE IF NOT EXISTS public.words
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 742 CACHE 1 ),
        word character varying(64) COLLATE pg_catalog."default",
        CONSTRAINT words_pkey PRIMARY KEY (id)
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.words
        OWNER to postgres;
    ```
  
  ![Screenshot from 2023-04-09 12-41-07](https://user-images.githubusercontent.com/71731579/230767008-7f9e89fe-fa61-435a-bf47-af00a8e9b423.png)
  


- psycopg installed 
    ```
    pip install psycopg2
    ```



### Starting the app
1. Clone the repository

```
    git clone https://github.com/BorisDundakov/Hangman.git
```

2. Start the game!

```
    /bin/python main.py
```


## Current Version - Hangman 2.1
- Implementation of OOP principles
- Visual features and game rules depending on difficulty selected (displaying the word and the hanging man)
- Hard difficulty implements a timer [fix soon]
- Random word is selected from a PostgreSQL Database

## Additional Information
- Database source --> https://github.com/Xethron/Hangman/blob/master/words.txt
- Previous version of the project was set up with a .txt file as a database
