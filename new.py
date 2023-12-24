from tkinter import *
from tkinter import ttk

data= [{
    "flight_IATA": "GF963",
    "departure_airport": "Queen Alia International",
    "org_departure_time\"": "2023-12-21T15:35:00+00:00",
    "estimated_arrival_time\"": "2023-12-21T15:35:00+00:00",
    "arrival_terminal": "1",
    "departure_delay": 18,
    "arrival_gate": None
  },
  {
    "flight_IATA": "SV6515",
    "departure_airport": "Faisalabad",
    "org_departure_time\"": "2023-12-21T19:00:00+00:00",
    "estimated_arrival_time\"": "2023-12-21T19:00:00+00:00",
    "arrival_terminal": "1",
    "departure_delay": 19,
    "arrival_gate": None
  },
  {
    "flight_IATA": "TK8349",
    "departure_airport": "Istanbul Airport",
    "org_departure_time\"": "2023-12-21T19:00:00+00:00",
    "estimated_arrival_time\"": "2023-12-21T19:00:00+00:00",
    "arrival_terminal": "1",
    "departure_delay": 36,
    "arrival_gate": None
  },
  {
    "flight_IATA": "GF543",
    "departure_airport": "Abu Dhabi International",
    "org_departure_time\"": "2023-12-21T18:10:00+00:00",
    "estimated_arrival_time\"": "2023-12-21T18:10:00+00:00",
    "arrival_terminal": "1",
    "departure_delay": 18,
    "arrival_gate": None
  },
  {
    "flight_IATA": "GF155",
    "departure_airport": "Ninoy Aquino International",
    "org_departure_time\"": "2023-12-21T16:35:00+00:00",
    "estimated_arrival_time\"": "2023-12-21T16:35:00+00:00",
    "arrival_terminal": "1",
    "departure_delay": 23,
    "arrival_gate": None
  },
]


noOfRecords=5

# Creating a 2D array (3x3) filled with zeros
rows = 3
cols = 3
matrix = [[0 for j in range(cols)] for i in range(rows)]

# Accessing and modifying elements
matrix[0][0] = 1
matrix[1][1] = 2
matrix[2][2] = 3

# Printing the 2D array
for row in matrix:
    print(row)
