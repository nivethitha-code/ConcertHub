from pydantic import BaseModel
from datetime import date,time

#pydantic model is used to verify the datatype given 
class ArtistBase(BaseModel):
    artist_id:str
    artist_name:str
    artist_gender:str
    no_of_songs:int
    phone:int
    artist_age:int

class PlaybackSingerBase(BaseModel):
    artist_id:str
    playbks_id:str
    playbks_name:str
    playbks_gender:str
    playbks_age:int

class LocationBase(BaseModel):
    artist_id:str
    location_id:str
    location_name:str
    accomodation:int
    date:date
    time:time

class TicketBase(BaseModel):
    location_id:str
    ticket_type:str
    ticket_name:str
    available_tickets:int
    price:int

class GenreBase(BaseModel):
    genre_id:str
    genre_name:str

class SongBase(BaseModel):
    artist_id:str
    genre_id:str
    song_id:str
    song_name:str

class BandBase(BaseModel):
    artist_id:str
    band_id:str
    band_name:str
    instrumentplayer_name:str
    instrumentname:str
    instrumentplayer_age:int

class BookingBase(BaseModel):
    book_id:str
    ticket_type:str
    no_of_tickets:int
    fan_name:str
    art_name:str
    loc_name:str

#new pydantic model for join query
class ArtistSong(BaseModel):
    artist_id:str
    artist_name:str
    artist_gender:str
    no_of_songs:int
    phone:int
    artist_age:int
    genre_id:str
    song_id:str
    song_name:str