import psycopg2
import webbrowser

ENDPOINT="database-3.cjxnchctpjfe.us-east-1.rds.amazonaws.com"
PORT="5432"
USER="postgres"
REGION="us-east-1b"
DBNAME="dbhw3"
PASSWORD = "carrie0622"
db = psycopg2.connect(
    database=DBNAME,
    user= USER,
    password= PASSWORD,
    host= ENDPOINT,
    port= PORT
)
con = db.cursor()
def db_random(emo):
    command = "select i.song, ar.artist, i.url " \
        "from song_info i, song_emo e, artist ar where e.emotion = \'"+emo+"\' "\
         "and e.song_id = i.song_id and i.artist_id = ar.artist_id ORDER BY RANDOM() LIMIT 1"
    con.execute(command)
    query_results = con.fetchall()
    return query_results[0][0],query_results[0][1],query_results[0][2]

def open_web(url):
    open = input("May I play the song for you? (y/n)")
    if(open=='y'or open=='Y'):
        webbrowser.open(url,new=1)
    elif(open=='n'or open=='N'):
        print("That's fine,maybe you need something new...")
    else:
        open_web(url)
