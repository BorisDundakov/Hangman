import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='133'
)


# 

def insert_data(data):
    """ insert all words into the words table  """

    cur = conn.cursor()
    # cur.executemany(insert_statement, data)
    for word in data:
        cur.execute("INSERT INTO words (word) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM words WHERE word = %s)", (word, word))
        conn.commit()


def random_word():
    """ select a random word from the words table  """

    cur = conn.cursor()
    cur.execute("SELECT word FROM words ORDER BY random() LIMIT 1")
    word_as_tuple = cur.fetchone()
    word = word_as_tuple[0]
    cur.close()
    conn.close()
    return word
