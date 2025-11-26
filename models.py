from sqlalchemy import ForeignKey,Column,Integer,String,Date,Time,select 
from database import Base
from sqlalchemy.orm import relationship

class Artist(Base):
    __tablename__='Artists'

    artist_id=Column(String(10),primary_key=True,index=True)
    artist_name=Column(String(100),unique=True)
    artist_gender=Column(String(10))
    no_of_songs=Column(Integer)
    phone=Column(Integer)
    artist_age=Column(Integer)

    song=relationship("Song",back_populates="artist",cascade='all,delete-orphan')
    play=relationship("PlaybackSinger",back_populates="a_var1",single_parent=True,cascade='all, delete-orphan')
    location=relationship("Location",back_populates="a_var2",cascade='all,delete-orphan')
    band=relationship("InstrumentalBand",back_populates="a_var3",cascade='all,delete-orphan')

class PlaybackSinger(Base):
    __tablename__="PlaybackSingers"

    artist_id=Column(String(10),ForeignKey("Artists.artist_id"))
    playbks_id=Column(String(10),primary_key=True)
    playbks_name=Column(String(100))
    playbks_gender=Column(String(10))
    playbks_age=Column(Integer)
    
    a_var1=relationship("Artist",back_populates="play")

class Location(Base):
    __tablename__="Locations"

    artist_id=Column(String(10),ForeignKey("Artists.artist_id"))
    location_id=Column(String(10),primary_key=True)
    location_name=Column(String(100))
    accomodation=Column(Integer)
    date=Column(Date)#datatype 
    time=Column(Time)#datatype to be given

    a_var2=relationship("Artist",back_populates="location")
    ticket=relationship("Ticket",back_populates="l_var")

class Ticket(Base):
    __tablename__="Tickets"

    ticket_type=Column(String(10),primary_key=True)
    location_id=Column(String(10),ForeignKey("Locations.location_id"))
    ticket_name=Column(String(100))
    available_tickets=Column(Integer)
    price=Column(Integer)

    l_var=relationship("Location",back_populates="ticket")
    book=relationship("Booking",back_populates="t_var1")

class Genre(Base):
    __tablename__='Genres'

    genre_id=Column(String(10),primary_key=True)
    genre_name=Column(String(100))
    
    s_var=relationship("Song",back_populates="genre")

class Song(Base):
    __tablename__='Songs'

    artist_id=Column(String(10),ForeignKey("Artists.artist_id"))
    genre_id=Column(String(10),ForeignKey("Genres.genre_id"))
    song_id=Column(String(10),primary_key=True)
    song_name=Column(String(200))

    artist=relationship("Artist",back_populates="song")
    genre=relationship("Genre",back_populates="s_var")

class InstrumentalBand(Base):
    __tablename__="InstrumentalBands"

    band_id=Column(String(10),primary_key=True)
    artist_id=Column(String(10),ForeignKey("Artists.artist_id"))
    band_name=Column(String(100))
    instrumentplayer_name=Column(String(100))
    instrumentname=Column(String(100))
    instrumentplayer_age=Column(Integer)

    a_var3=relationship("Artist",back_populates="band")

class Booking(Base):
    __tablename__="Bookings"

    book_id=Column(String(10),primary_key=True)
    ticket_type=Column(String(10),ForeignKey("Tickets.ticket_type"))
    no_of_tickets=Column(Integer)
    fan_name=Column(String(100))
    art_name=Column(String(100))
    loc_name=Column(String(100))
    
    t_var1=relationship("Ticket",back_populates="book")

#query1=select_from(Artists).join(PlaybackSingers,Artists.a_id=PlaybackSingers.a_id)
