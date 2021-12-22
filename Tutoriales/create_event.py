from datetime import datetime, timedelta
from calendar_setup import get_calendar_service
import assistent
import time

def take_event_title():
    assistent.talk("¿Cuál es el título del evento?")
    listened_title = assistent.listen()
    return listened_title

def take_event_desc():
    assistent.talk("¿Cuál es la descripción del evento?")
    listen_desc = assistent.listen()
    return listen_desc

def take_start_date():
    assistent.talk("¿En qué fecha y hora será el evento?")
    listened_date = assistent.listen().replace(' a las ', ' del ')
    if '2000' in listened_date:
        listened_date = listened_date.replace('2000 21', '2021')
    print(listened_date)
    listened_date = listened_date.split(' del ')
    new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
        + ' ' + listened_date[3]
    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat

def take_end_date():
    assistent.talk("¿En qué fecha y hora terminará el evento?")
    listened_date = assistent.listen().replace(' a las ', ' del ')
    if '2000' in listened_date:
        listened_date = listened_date.replace('2000 21', '2021')
    listened_date = listened_date.split(' del ')
    new_date = listened_date[2] + '-' + listened_date[1] + '-' + listened_date[0]\
        + ' ' + listened_date[3]
    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat



def create_event():
    event_title = take_event_title()
    time.sleep(0.5)
    event_desc = take_event_desc()
    time.sleep(0.5)
    start_date = take_start_date()
    time.sleep(0.5)
    end_date = take_end_date()
    time.sleep(0.5)
    calendar_service = get_calendar_service() 
    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start": {"dateTime": start_date, "timeZone": 'America/Guayaquil'},
            "end": {"dateTime": end_date, "timeZone": 'America/Guayaquil'},
        }
    ).execute()

    print("Evento creado con éxito!")
    print("Título: ", event_result['summary'])
    print("Descripción: ", event_result["description"])
    print("Empieza en: ", event_result["start"])
    print("Termina en: ", event_result["end"])


if __name__ == '__main__':
    create_event()