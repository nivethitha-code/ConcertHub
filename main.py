from fastapi import FastAPI,HTTPException,Depends,status,Request,Form
from fastapi.responses import HTMLResponse
from typing import Annotated#using this we do dependency injection
from database import engine,SessionLocal
from sqlalchemy.orm import Session
import models
from models import Artist,PlaybackSinger,Location,Ticket,Genre,Song,InstrumentalBand,Booking
import schemas
from schemas import ArtistBase,PlaybackSingerBase,LocationBase,TicketBase,GenreBase,SongBase,BandBase,BookingBase,ArtistSong
from fastapi.templating import Jinja2Templates #for the html page to be printed
from fastapi.staticfiles import StaticFiles #for the image to included in the html page
from datetime import date,time

app=FastAPI()
models.Base.metadata.create_all(bind=engine) #here we are connecting the Base with the engine to know for which database we are creating the class Base and from this query after connecing to the database using this query table will be created automatically

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]


templates=Jinja2Templates(directory="templates")#all the html files will be available in this directory
app.mount("/static",StaticFiles(directory="static"),name="static") #this is seperate path for the images which is not like app.get or app.put so we are mounting it  
#changes made in the html file will make it to connect with the image and it will be found in the home page


@app.get("/",response_class=HTMLResponse)
async def get_mainpage(request:Request):
    return templates.TemplateResponse("mainhtml.html",{"request":request})#this request is used to take the input we are giving to the html

@app.get("/user", response_class=HTMLResponse)
async def get_user_page(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})

@app.get("/query", response_class=HTMLResponse)
async def get_query_page(request: Request):
    return templates.TemplateResponse("query.html", {"request": request})

@app.get("/admin_insert", response_class=HTMLResponse)
async def get_admin_insert_page(request: Request):
    return templates.TemplateResponse("admin_insert.html", {"request": request})

@app.get("/admin_update", response_class=HTMLResponse)
async def get_admin_update_page(request: Request):
    return templates.TemplateResponse("admin_update.html", {"request": request})

@app.get("/admin_delete", response_class=HTMLResponse)
async def get_admin_delete_page(request: Request):
    return templates.TemplateResponse("admin_delete.html", {"request": request})


@app.post("/admin_insert",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,artist_id:str=Form(...),artist_name:str=Form(...),artist_gender:str=Form(...),no_of_songs:int=Form(...),phone:int=Form(...),artist_age:int=Form(...),artist1_id:str=Form(...),playbks_id:str=Form(...),playbks_name:str=Form(...),playbks_gender:str=Form(...),playbks_age:int=Form(...),artist2_id:str=Form(...),band_id:str=Form(...),band_name:str=Form(...),instrumentplayer_name:str=Form(...),instrumentname:str=Form(...),instrumentplayer_age:int=Form(...),genre_id:str=Form(...),genre_name:str=Form(...),artist3_id:str=Form(...),genre1_id:str=Form(...),song_id:str=Form(...),song_name:str=Form(...),artist4_id:str=Form(...),location_id:str=Form(...),location_name:str=Form(...),accomodation:int=Form(...),concert_date:date=Form(...),concert_time:time=Form(...),location1_id:str=Form(...),ticket_type:str=Form(...),ticket_name:str=Form(...),available_tickets:int=Form(...),price:int=Form(...)):
    db_art=models.Artist(artist_id=artist_id,artist_name=artist_name,artist_gender=artist_gender,artist_age=artist_age,no_of_songs=no_of_songs,phone=phone)
    db.add(db_art)
    db.commit()
    db.refresh(db_art)

    db_play=models.PlaybackSinger(artist_id=artist1_id,playbks_id=playbks_id,playbks_name=playbks_name,playbks_gender=playbks_gender,playbks_age=playbks_age)
    db.add(db_play)
    db.commit()
    db.refresh(db_play)

    db_loc=models.Location(artist_id=artist2_id,location_id=location_id,location_name=location_name,accomodation=accomodation,date=concert_date,time=concert_time)
    db.add(db_loc)
    db.commit()
    db.refresh(db_loc)

    db_tic=models.Ticket(ticket_type=ticket_type,location_id=location1_id,ticket_name=ticket_name,available_tickets=available_tickets,price=price)
    db.add(db_tic)
    db.commit()
    db.refresh(db_tic)

    db_genre=models.Genre(genre_id=genre_id,genre_name=genre_name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)

    db_s=models.Song(artist_id=artist3_id,genre_id=genre1_id,song_id=song_id,song_name=song_name)
    db.add(db_s)
    db.commit()
    db.refresh(db_s)
    
    db_b=models.InstrumentalBand(band_id=band_id,artist_id=artist4_id,band_name=band_name,instrumentplayer_name=instrumentplayer_name,instrumentname=instrumentname,instrumentplayer_age=instrumentplayer_age)
    db.add(db_b)
    db.commit()
    db.refresh(db_b)


@app.post("/user",status_code=status.HTTP_201_CREATED)
async def book_tickets(db:db_dependency,fan_name:str=Form(...),artist1_name:str=Form(...),location1_name:str=Form(...),ticket1_type:str=Form(...),no_of_tickets:int=Form(...),book_id:str=Form(...)):    
    db_bo=models.Booking(book_id=book_id,ticket_type=ticket1_type,no_of_tickets=no_of_tickets,fan_name=fan_name,art_name=artist1_name,loc_name=location1_name)
    db.add(db_bo)
    db.commit()
    db.refresh(db_bo)

@app.post("/admin_update",status_code=status.HTTP_201_CREATED)
async def update_data(db:db_dependency,location2_id:str=Form(...),ticket2_type:str=Form(...),ticket1_name:str=Form(...),available1_tickets:int=Form(...),price1:int=Form(...),location3_id:str=Form(...),ticket3_type:str=Form(...),ticket2_name:str=Form(...),available2_tickets:int=Form(...),price2:int=Form(...)):
    db_update=db.query(models.Ticket).filter(models.Ticket.ticket_type == ticket2_type).first()
    db_update.location_id=location3_id
    db_update.ticket_name=ticket2_name
    db_update.available_tickets=available2_tickets
    db_update.price=price2
    db.commit()



@app.post("/admin_delete",status_code=status.HTTP_204_NO_CONTENT)
async def delete_artist(db:db_dependency, artist5_id:str=Form(...)):
    artist = db.query(models.Artist).filter(models.Artist.artist_id == artist5_id).first()
    db.delete(artist)
    db.commit()


#@app.post("/query", response_model=artist_name ,location_name, status_code=status.HTTP_201_CREATED):
#@app.get("/query", response_class=HTMLResponse)
#async def get_user_page(request: Request):
#    return templates.TemplateResponse("user.html", {"request": request})





#@app.get("/concert1",response_model=list[ArtistBase])
@app.get("/concert1/{artist_id}",response_model=list[schemas.ArtistBase])
async def print_artist(request:Request,id:str,db:db_dependency):
    result=db.query(models.Artist).filter(models.Artist.artist_id==id).first()
    return templates.TemplateResponse("mainhtml.html",{"request":request})

@app.get("/concert2")
async def print_artist(db:db_dependency):
    result=db.query(models.Artist).all()
    return result

@app.get("/concert3")#here returning pydantic model
async def print_artist(db:db_dependency):
    result1=db.query(models.Artist).all()
    result2=db.query(models.PlaybackSinger).all()
    return result1,result2

#@app.get("/concert4",response_model=list[ArtistSong])#here new pydantic model is created and made as a list as join makes new table we make new pydantic
@app.get("/concert4",response_model=list[schemas.ArtistSong])
async def print_join(db:db_dependency):
    result=db.query(models.Artist,models.Song).join(models.Song,models.Artist.artist_id == models.Song.artist_id).all()#return type of this is dictionary so we are converting it to list
     # as we want only to return list of pydantic model here the new pydantic of join is returned as a list of pydantic model 
    return [ArtistSong(
                artist_id=a.artist_id,
                artist_name=a.artist_name,
                artist_gender=a.artist_gender,
                no_of_songs=a.no_of_songs,
                phone=a.phone,
                artist_age=a.artist_age,
                genre_id=s.genre_id,
                song_id=s.song_id,
                song_name=s.song_name,
            )
            for a,s in result]

