import webbrowser
import datetime
from pandas import *

schedule_file = ExcelFile("horario.xlsx")
schedule_dataframe = schedule_file.parse(schedule_file.sheet_names[0])
schedule_dict = schedule_dataframe.to_dict()

days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
started = False
i = 0

while i < len(schedule_dict["Hora"]):
    index_day = datetime.datetime.now().weekday()
    week_day = days[index_day]
    for day in schedule_dict.keys():
      if day == week_day:
            hour = schedule_dict["Hora"][i].strftime("%H:%M:%S")
            link_key = "Enlace" + week_day
            link = schedule_dict[link_key][i]

            while started != True:
                if datetime.datetime.now().strftime('%H:%M:%S') == hour:
                    print("Abriendo clase...")
                    webbrowser.open(link)
                    started = True
                else:
                    continue

    i += 1
    started = False
