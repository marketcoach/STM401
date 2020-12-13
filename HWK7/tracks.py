# Musical Track Database
# This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

# CREATE TABLE Artist (
    # id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    # name    TEXT UNIQUE
# );

# CREATE TABLE Genre (
    # id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    # name    TEXT UNIQUE
# );

# CREATE TABLE Album (
    # id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    # artist_id  INTEGER,
    # title   TEXT UNIQUE
# );

# CREATE TABLE Track (
    # id  INTEGER NOT NULL PRIMARY KEY 
        # AUTOINCREMENT UNIQUE,
    # title TEXT  UNIQUE,
    # album_id  INTEGER,
    # genre_id  INTEGER,
    # len INTEGER, rating INTEGER, count INTEGER
# );
# If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file to be used for this assignment. You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

# SELECT Track.title, Artist.name, Album.title, Genre.name 
    # FROM Track JOIN Genre JOIN Album JOIN Artist 
    # ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        # AND Album.artist_id = Artist.id
    # ORDER BY Artist.name LIMIT 3
# The expected result of the modified query on your database is:
# Select Language​▼
# Track	Artist	Album	Genre
# Chase the Ace	AC/DC	Who Made Who	Rock
# D.T.	AC/DC	Who Made Who	Rock
# For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock

import sqlite3
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
        
    #Get file
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'
uh = open(fname)

    #Open database connection
conn = sqlite3.connect('iTunesLibrary.sqlite')
cur = conn.cursor()

    #Create tables or delete their content
cur.executescript('CREATE TABLE IF NOT EXISTS Artist (
                        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name    TEXT UNIQUE);
                                
                    CREATE TABLE IF NOT EXISTS Genre (
                        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name    TEXT UNIQUE);
                                
                    CREATE TABLE IF NOT EXISTS Album (
                        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        artist_id  INTEGER,
                        title   TEXT UNIQUE);
                                
                    CREATE TABLE IF NOT EXISTS Track (
                        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        title TEXT  UNIQUE,
                        album_id  INTEGER,
                        genre_id  INTEGER,
                        len INTEGER, 
                        rating INTEGER, 
                        count INTEGER);
                                
                    DELETE FROM Artist;
                    DELETE FROM Genre;
                    DELETE FROM Album;
                    DELETE FROM Track
    ') 


    #Function that reconstruct the dictionaries in a standard format, from:
    # <key>Track ID</key><integer>369</integer>
    # <key>Name</key><string>Another One Bites The Dust</string>
    # <key>Artist</key><string>Queen</string>
    # to ("Track ID" : 369) , ("Name" : "Another One Bites The Dust") , ("Artist" : "Queen")
    def lookup(d, key):
        found = False
        for child in d:
            if found : return child.text
            if child.tag == 'key' and child.text == key :
                found = True
        return None

         #Parsing xml
    stuff = ET.parse(fname)
    #Finding all dict (3rd levels)
    all = stuff.findall('dict/dict/dict')
    print('Dict count:', len(all))

    #For each dict (track) insert values in the database
    for entry in all:

        #Cleaning up some incomplete records
        if ( lookup(entry, 'Track ID') is None ) : continue
        if ( lookup(entry, 'Genre') is None ) : continue
        
        #Collecting all fields from the track
        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')
        genre = lookup(entry, 'Genre')

        if name is None or artist is None or album is None : continue

        # print(name, artist, album, count, rating, length, genre)

        #Insert or ignore if already exist this record in Artist
        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', ( artist, ) )
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        #Insert or ignore if already exist this record in Album
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        #Insert or ignore if already exist this record in Genre
        cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ? )''', (genre, ) )
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]
        
        #Insert or update values in Track
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, len, rating, count, genre_id) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', 
            ( name, album_id, length, rating, count, genre_id ) )

            
    conn.commit()

    #Result query
    table = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
                FROM Track JOIN Genre JOIN Album JOIN Artist 
                ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
                AND Album.artist_id = Artist.id
                ORDER BY Artist.name LIMIT 3'''
    for line in cur.execute(table): 
        print(str(line[0]), "|", str(line[1]),"|", str(line[2]),"|", str(line[3]))

    conn.close()

    