# FECHAS
# Para usar las fechas debemos importar el modulo datetime del core de python
from datetime import datetime

# FECHA DE HOY
now = datetime.now()


# mostrar fecha con funciones
def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)


print_date(now)

"""
Representacion unica de un tiempo, se muestra en formato posix
NOTA: se usa para propagar la fecha para pasarla atravez de una llamada a api
"""
timespamp = now.timestamp()
print(timespamp)

# CREAR FECHA EN BASE A UNOS DATOS
# Creamos fecha del siguiente año
year_2025 = datetime(2025, 1, 1)
print(year_2025)


# Este modulo proporciona diferentes funciones con el tiempo
from datetime import time


current_time = time(16, 4, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# Modulo date
from datetime import date

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Modulo date con parametros
current_date = date(2024, 1, 8)
print(current_date)

# OPERACIONES CON FECHAS
current_date = date(
    current_date.year, current_date.month + 1, current_date.day
)  # Sumamos uno al mes

print(current_date.month)

diff = year_2025 - now  # Restamos de  fecha del año siguiente a now(tiempo de hoy)
print(diff)
# NOTA: si los objetos son del mismo tipo se puede hacer operaciones si no no

from datetime import timedelta

# Sirve para operar con diferencias de fecha
start_time_delta = timedelta(200, 100, 100, weeks=10)
end_time_delta = timedelta(300, 100, 100, weeks=13)
print(end_time_delta - start_time_delta)
print(end_time_delta + start_time_delta)
