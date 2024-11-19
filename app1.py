import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import os





players =[
  {
    "id": 1,
    "first_name": "Alex",
    "last_name": "Abrines",
    "position": "G",
    "height": "6-6",
    "weight": "190",
    "jersey_number": "8",
    "college": "FC Barcelona",
    "country": "Spain",
    "draft_year": 2013,
    "draft_round": 2,
    "draft_number": 32,
    "team": {
      "id": 21,
      "conference": "West",
      "division": "Northwest",
      "city": "Oklahoma City",
      "name": "Thunder",
      "full_name": "Oklahoma City Thunder",
      "abbreviation": "OKC"
    }
  },
  {
    "id": 2,
    "first_name": "Jaylen",
    "last_name": "Adams",
    "position": "G",
    "height": "6-0",
    "weight": "225",
    "jersey_number": "10",
    "college": "St. Bonaventure",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 1,
      "conference": "East",
      "division": "Southeast",
      "city": "Atlanta",
      "name": "Hawks",
      "full_name": "Atlanta Hawks",
      "abbreviation": "ATL"
    }
  },
  {
    "id": 3,
    "first_name": "Steven",
    "last_name": "Adams",
    "position": "C",
    "height": "6-11",
    "weight": "265",
    "jersey_number": "12",
    "college": "Pittsburgh",
    "country": "New Zealand",
    "draft_year": 2013,
    "draft_round": 1,
    "draft_number": 12,
    "team": {
      "id": 11,
      "conference": "West",
      "division": "Southwest",
      "city": "Houston",
      "name": "Rockets",
      "full_name": "Houston Rockets",
      "abbreviation": "HOU"
    }
  },
  {
    "id": 4,
    "first_name": "Bam",
    "last_name": "Adebayo",
    "position": "C-F",
    "height": "6-9",
    "weight": "255",
    "jersey_number": "13",
    "college": "Kentucky",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 1,
    "draft_number": 14,
    "team": {
      "id": 16,
      "conference": "East",
      "division": "Southeast",
      "city": "Miami",
      "name": "Heat",
      "full_name": "Miami Heat",
      "abbreviation": "MIA"
    }
  },
  {
    "id": 5,
    "first_name": "DeVaughn",
    "last_name": "Akoon-Purcell",
    "position": "G-F",
    "height": "6-5",
    "weight": "201",
    "jersey_number": "44",
    "college": "Illinois State",
    "country": "Trinidad and Tobago",
    "draft_year": 2016,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 8,
      "conference": "West",
      "division": "Northwest",
      "city": "Denver",
      "name": "Nuggets",
      "full_name": "Denver Nuggets",
      "abbreviation": "DEN"
    }
  },
  {
    "id": 6,
    "first_name": "LaMarcus",
    "last_name": "Aldridge",
    "position": "F",
    "height": "6-11",
    "weight": "250",
    "jersey_number": "21",
    "college": "University of Texas at Austin",
    "country": "USA",
    "draft_year": 2006,
    "draft_round": 1,
    "draft_number": 2,
    "team": {
      "id": 3,
      "conference": "East",
      "division": "Atlantic",
      "city": "Brooklyn",
      "name": "Nets",
      "full_name": "Brooklyn Nets",
      "abbreviation": "BKN"
    }
  },
  {
    "id": 7,
    "first_name": "Rawle",
    "last_name": "Alkins",
    "position": "G",
    "height": "6-5",
    "weight": "225",
    "jersey_number": "20",
    "college": "Arizona",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 5,
      "conference": "East",
      "division": "Central",
      "city": "Chicago",
      "name": "Bulls",
      "full_name": "Chicago Bulls",
      "abbreviation": "CHI"
    }
  },
  {
    "id": 8,
    "first_name": "Grayson",
    "last_name": "Allen",
    "position": "G",
    "height": "6-4",
    "weight": "198",
    "jersey_number": "8",
    "college": "Duke",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 21,
    "team": {
      "id": 24,
      "conference": "West",
      "division": "Pacific",
      "city": "Phoenix",
      "name": "Suns",
      "full_name": "Phoenix Suns",
      "abbreviation": "PHX"
    }
  },
  {
    "id": 9,
    "first_name": "Jarrett",
    "last_name": "Allen",
    "position": "C",
    "height": "6-9",
    "weight": "243",
    "jersey_number": "31",
    "college": "Texas",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 1,
    "draft_number": 22,
    "team": {
      "id": 6,
      "conference": "East",
      "division": "Central",
      "city": "Cleveland",
      "name": "Cavaliers",
      "full_name": "Cleveland Cavaliers",
      "abbreviation": "CLE"
    }
  },
  {
    "id": 10,
    "first_name": "Al-Farouq",
    "last_name": "Aminu",
    "position": "F",
    "height": "6-8",
    "weight": "220",
    "jersey_number": "5",
    "college": "Wake Forest",
    "country": "USA",
    "draft_year": 2010,
    "draft_round": 1,
    "draft_number": 8,
    "team": {
      "id": 25,
      "conference": "West",
      "division": "Northwest",
      "city": "Portland",
      "name": "Trail Blazers",
      "full_name": "Portland Trail Blazers",
      "abbreviation": "POR"
    }
  },
  {
    "id": 11,
    "first_name": "Justin",
    "last_name": "Anderson",
    "position": "G-F",
    "height": "6-5",
    "weight": "231",
    "jersey_number": "10",
    "college": "Virginia",
    "country": "USA",
    "draft_year": 2015,
    "draft_round": 1,
    "draft_number": 21,
    "team": {
      "id": 12,
      "conference": "East",
      "division": "Central",
      "city": "Indiana",
      "name": "Pacers",
      "full_name": "Indiana Pacers",
      "abbreviation": "IND"
    }
  },
  {
    "id": 12,
    "first_name": "Kyle",
    "last_name": "Anderson",
    "position": "F",
    "height": "6-9",
    "weight": "230",
    "jersey_number": "1",
    "college": "UCLA",
    "country": "USA",
    "draft_year": 2014,
    "draft_round": 1,
    "draft_number": 30,
    "team": {
      "id": 10,
      "conference": "West",
      "division": "Pacific",
      "city": "Golden State",
      "name": "Warriors",
      "full_name": "Golden State Warriors",
      "abbreviation": "GSW"
    }
  },
  {
    "id": 13,
    "first_name": "Ryan",
    "last_name": "Anderson",
    "position": "F",
    "height": "6-10",
    "weight": "240",
    "jersey_number": "31",
    "college": "California",
    "country": "USA",
    "draft_year": 2008,
    "draft_round": 1,
    "draft_number": 21,
    "team": {
      "id": 19,
      "conference": "West",
      "division": "Southwest",
      "city": "New Orleans",
      "name": "Pelicans",
      "full_name": "New Orleans Pelicans",
      "abbreviation": "NOP"
    }
  },
  {
    "id": 14,
    "first_name": "Ike",
    "last_name": "Anigbogu",
    "position": "C",
    "height": "6-10",
    "weight": "262",
    "jersey_number": "13",
    "college": "UCLA",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 47,
    "team": {
      "id": 12,
      "conference": "East",
      "division": "Central",
      "city": "Indiana",
      "name": "Pacers",
      "full_name": "Indiana Pacers",
      "abbreviation": "IND"
    }
  },
  {
    "id": 15,
    "first_name": "Giannis",
    "last_name": "Antetokounmpo",
    "position": "F",
    "height": "6-11",
    "weight": "243",
    "jersey_number": "34",
    "college": "Filathlitikos",
    "country": "Greece",
    "draft_year": 2013,
    "draft_round": 1,
    "draft_number": 15,
    "team": {
      "id": 17,
      "conference": "East",
      "division": "Central",
      "city": "Milwaukee",
      "name": "Bucks",
      "full_name": "Milwaukee Bucks",
      "abbreviation": "MIL"
    }
  },
  {
    "id": 16,
    "first_name": "Kostas",
    "last_name": "Antetokounmpo",
    "position": "F",
    "height": "6-10",
    "weight": "200",
    "jersey_number": "37",
    "college": "Dayton",
    "country": "Greece",
    "draft_year": 2018,
    "draft_round": 2,
    "draft_number": 60,
    "team": {
      "id": 5,
      "conference": "East",
      "division": "Central",
      "city": "Chicago",
      "name": "Bulls",
      "full_name": "Chicago Bulls",
      "abbreviation": "CHI"
    }
  },
  {
    "id": 17,
    "first_name": "Carmelo",
    "last_name": "Anthony",
    "position": "F",
    "height": "6-7",
    "weight": "238",
    "jersey_number": "7",
    "college": "Syracuse",
    "country": "USA",
    "draft_year": 2003,
    "draft_round": 1,
    "draft_number": 3,
    "team": {
      "id": 14,
      "conference": "West",
      "division": "Pacific",
      "city": "Los Angeles",
      "name": "Lakers",
      "full_name": "Los Angeles Lakers",
      "abbreviation": "LAL"
    }
  },
  {
    "id": 18,
    "first_name": "OG",
    "last_name": "Anunoby",
    "position": "F",
    "height": "6-7",
    "weight": "240",
    "jersey_number": "8",
    "college": "Indiana",
    "country": "United Kingdom",
    "draft_year": 2017,
    "draft_round": 1,
    "draft_number": 23,
    "team": {
      "id": 20,
      "conference": "East",
      "division": "Atlantic",
      "city": "New York",
      "name": "Knicks",
      "full_name": "New York Knicks",
      "abbreviation": "NYK"
    }
  },
  {
    "id": 19,
    "first_name": "Ryan",
    "last_name": "Arcidiacono",
    "position": "G",
    "height": "6-3",
    "weight": "195",
    "jersey_number": "51",
    "college": "Villanova",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 20,
      "conference": "East",
      "division": "Atlantic",
      "city": "New York",
      "name": "Knicks",
      "full_name": "New York Knicks",
      "abbreviation": "NYK"
    }
  },
  {
    "id": 20,
    "first_name": "Trevor",
    "last_name": "Ariza",
    "position": "F",
    "height": "6-8",
    "weight": "215",
    "jersey_number": "8",
    "college": "UCLA",
    "country": "USA",
    "draft_year": 2004,
    "draft_round": 2,
    "draft_number": 43,
    "team": {
      "id": 14,
      "conference": "West",
      "division": "Pacific",
      "city": "Los Angeles",
      "name": "Lakers",
      "full_name": "Los Angeles Lakers",
      "abbreviation": "LAL"
    }
  },
  {
    "id": 21,
    "first_name": "D.J.",
    "last_name": "Augustin",
    "position": "G",
    "height": "5-11",
    "weight": "183",
    "jersey_number": "4",
    "college": "Texas",
    "country": "USA",
    "draft_year": 2008,
    "draft_round": 1,
    "draft_number": 9,
    "team": {
      "id": 14,
      "conference": "West",
      "division": "Pacific",
      "city": "Los Angeles",
      "name": "Lakers",
      "full_name": "Los Angeles Lakers",
      "abbreviation": "LAL"
    }
  },
  {
    "id": 22,
    "first_name": "Deandre",
    "last_name": "Ayton",
    "position": "C",
    "height": "7-0",
    "weight": "252",
    "jersey_number": "2",
    "college": "Arizona",
    "country": "Bahamas",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 1,
    "team": {
      "id": 25,
      "conference": "West",
      "division": "Northwest",
      "city": "Portland",
      "name": "Trail Blazers",
      "full_name": "Portland Trail Blazers",
      "abbreviation": "POR"
    }
  },
  {
    "id": 23,
    "first_name": "Dwayne",
    "last_name": "Bacon",
    "position": "G-F",
    "height": "6-6",
    "weight": "221",
    "jersey_number": "8",
    "college": "Florida State",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 40,
    "team": {
      "id": 14,
      "conference": "West",
      "division": "Pacific",
      "city": "Los Angeles",
      "name": "Lakers",
      "full_name": "Los Angeles Lakers",
      "abbreviation": "LAL"
    }
  },
  {
    "id": 24,
    "first_name": "Marvin",
    "last_name": "Bagley III",
    "position": "F",
    "height": "6-10",
    "weight": "235",
    "jersey_number": "35",
    "college": "Duke",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 2,
    "team": {
      "id": 30,
      "conference": "East",
      "division": "Southeast",
      "city": "Washington",
      "name": "Wizards",
      "full_name": "Washington Wizards",
      "abbreviation": "WAS"
    }
  },
  {
    "id": 25,
    "first_name": "Ron",
    "last_name": "Baker",
    "position": "G",
    "height": "6-4",
    "weight": "220",
    "jersey_number": "31",
    "college": "Wichita State",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 20,
      "conference": "East",
      "division": "Atlantic",
      "city": "New York",
      "name": "Knicks",
      "full_name": "New York Knicks",
      "abbreviation": "NYK"
    }
  },
  {
    "id": 26,
    "first_name": "Wade",
    "last_name": "Baldwin IV",
    "position": "G",
    "height": "6-4",
    "weight": "202",
    "jersey_number": "2",
    "college": "Vanderbilt",
    "country": "USA",
    "draft_year": 2016,
    "draft_round": 1,
    "draft_number": 17,
    "team": {
      "id": 15,
      "conference": "West",
      "division": "Southwest",
      "city": "Memphis",
      "name": "Grizzlies",
      "full_name": "Memphis Grizzlies",
      "abbreviation": "MEM"
    }
  },
  {
    "id": 27,
    "first_name": "Lonzo",
    "last_name": "Ball",
    "position": "G",
    "height": "6-6",
    "weight": "190",
    "jersey_number": "2",
    "college": "UCLA",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 1,
    "draft_number": 2,
    "team": {
      "id": 5,
      "conference": "East",
      "division": "Central",
      "city": "Chicago",
      "name": "Bulls",
      "full_name": "Chicago Bulls",
      "abbreviation": "CHI"
    }
  },
  {
    "id": 28,
    "first_name": "Mo",
    "last_name": "Bamba",
    "position": "C",
    "height": "7-0",
    "weight": "231",
    "jersey_number": "4",
    "college": "Texas",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 6,
    "team": {
      "id": 13,
      "conference": "West",
      "division": "Pacific",
      "city": "LA",
      "name": "Clippers",
      "full_name": "LA Clippers",
      "abbreviation": "LAC"
    }
  },
  {
    "id": 29,
    "first_name": "J.J.",
    "last_name": "Barea",
    "position": "G",
    "height": "5-10",
    "weight": "180",
    "jersey_number": "5",
    "college": "Northeastern",
    "country": "Puerto Rico",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 7,
      "conference": "West",
      "division": "Southwest",
      "city": "Dallas",
      "name": "Mavericks",
      "full_name": "Dallas Mavericks",
      "abbreviation": "DAL"
    }
  },
  {
    "id": 30,
    "first_name": "Harrison",
    "last_name": "Barnes",
    "position": "F",
    "height": "6-8",
    "weight": "225",
    "jersey_number": "40",
    "college": "North Carolina",
    "country": "USA",
    "draft_year": 2012,
    "draft_round": 1,
    "draft_number": 7,
    "team": {
      "id": 27,
      "conference": "West",
      "division": "Southwest",
      "city": "San Antonio",
      "name": "Spurs",
      "full_name": "San Antonio Spurs",
      "abbreviation": "SAS"
    }
  },
  {
    "id": 31,
    "first_name": "Will",
    "last_name": "Barton",
    "position": "G",
    "height": "6-5",
    "weight": "181",
    "jersey_number": "1",
    "college": "Memphis",
    "country": "USA",
    "draft_year": 2012,
    "draft_round": 2,
    "draft_number": 40,
    "team": {
      "id": 28,
      "conference": "East",
      "division": "Atlantic",
      "city": "Toronto",
      "name": "Raptors",
      "full_name": "Toronto Raptors",
      "abbreviation": "TOR"
    }
  },
  {
    "id": 32,
    "first_name": "Keita",
    "last_name": "Bates-Diop",
    "position": "F",
    "height": "6-8",
    "weight": "229",
    "jersey_number": "13",
    "college": "Ohio State",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 2,
    "draft_number": 48,
    "team": {
      "id": 18,
      "conference": "West",
      "division": "Northwest",
      "city": "Minnesota",
      "name": "Timberwolves",
      "full_name": "Minnesota Timberwolves",
      "abbreviation": "MIN"
    }
  },
  {
    "id": 33,
    "first_name": "Nicolas",
    "last_name": "Batum",
    "position": "F-G",
    "height": "6-8",
    "weight": "230",
    "jersey_number": "33",
    "college": "Le Mans",
    "country": "France",
    "draft_year": 2008,
    "draft_round": 1,
    "draft_number": 25,
    "team": {
      "id": 13,
      "conference": "West",
      "division": "Pacific",
      "city": "LA",
      "name": "Clippers",
      "full_name": "LA Clippers",
      "abbreviation": "LAC"
    }
  },
  {
    "id": 34,
    "first_name": "Jerryd",
    "last_name": "Bayless",
    "position": "G",
    "height": "6-3",
    "weight": "200",
    "jersey_number": "8",
    "college": "Arizona",
    "country": "USA",
    "draft_year": 2008,
    "draft_round": 1,
    "draft_number": 11,
    "team": {
      "id": 17,
      "conference": "East",
      "division": "Central",
      "city": "Milwaukee",
      "name": "Bucks",
      "full_name": "Milwaukee Bucks",
      "abbreviation": "MIL"
    }
  },
  {
    "id": 35,
    "first_name": "Aron",
    "last_name": "Baynes",
    "position": "C-F",
    "height": "6-10",
    "weight": "260",
    "jersey_number": "46",
    "college": "Washington State",
    "country": "Australia",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 9,
      "conference": "East",
      "division": "Central",
      "city": "Detroit",
      "name": "Pistons",
      "full_name": "Detroit Pistons",
      "abbreviation": "DET"
    }
  },
  {
    "id": 36,
    "first_name": "Kent",
    "last_name": "Bazemore",
    "position": "G",
    "height": "6-4",
    "weight": "195",
    "jersey_number": "9",
    "college": "Old Dominion",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 26,
      "conference": "West",
      "division": "Pacific",
      "city": "Sacramento",
      "name": "Kings",
      "full_name": "Sacramento Kings",
      "abbreviation": "SAC"
    }
  },
  {
    "id": 37,
    "first_name": "Bradley",
    "last_name": "Beal",
    "position": "G",
    "height": "6-4",
    "weight": "207",
    "jersey_number": "3",
    "college": "Florida",
    "country": "USA",
    "draft_year": 2012,
    "draft_round": 1,
    "draft_number": 3,
    "team": {
      "id": 24,
      "conference": "West",
      "division": "Pacific",
      "city": "Phoenix",
      "name": "Suns",
      "full_name": "Phoenix Suns",
      "abbreviation": "PHX"
    }
  },
  {
    "id": 38,
    "first_name": "Malik",
    "last_name": "Beasley",
    "position": "G",
    "height": "6-4",
    "weight": "187",
    "jersey_number": "5",
    "college": "Florida State",
    "country": "USA",
    "draft_year": 2016,
    "draft_round": 1,
    "draft_number": 19,
    "team": {
      "id": 9,
      "conference": "East",
      "division": "Central",
      "city": "Detroit",
      "name": "Pistons",
      "full_name": "Detroit Pistons",
      "abbreviation": "DET"
    }
  },
  {
    "id": 39,
    "first_name": "Michael",
    "last_name": "Beasley",
    "position": "F",
    "height": "6-9",
    "weight": "235",
    "jersey_number": "8",
    "college": "Kansas State",
    "country": "USA",
    "draft_year": 2008,
    "draft_round": 1,
    "draft_number": 2,
    "team": {
      "id": 16,
      "conference": "East",
      "division": "Southeast",
      "city": "Miami",
      "name": "Heat",
      "full_name": "Miami Heat",
      "abbreviation": "MIA"
    }
  },
  {
    "id": 40,
    "first_name": "Marco",
    "last_name": "Belinelli",
    "position": "G-F",
    "height": "6-5",
    "weight": "220",
    "jersey_number": "18",
    "college": "Fortitudo Bologna",
    "country": "Italy",
    "draft_year": 2007,
    "draft_round": 1,
    "draft_number": 18,
    "team": {
      "id": 27,
      "conference": "West",
      "division": "Southwest",
      "city": "San Antonio",
      "name": "Spurs",
      "full_name": "San Antonio Spurs",
      "abbreviation": "SAS"
    }
  },
  {
    "id": 41,
    "first_name": "Jordan",
    "last_name": "Bell",
    "position": "F",
    "height": "6-8",
    "weight": "216",
    "jersey_number": "7",
    "college": "Oregon",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 38,
    "team": {
      "id": 5,
      "conference": "East",
      "division": "Central",
      "city": "Chicago",
      "name": "Bulls",
      "full_name": "Chicago Bulls",
      "abbreviation": "CHI"
    }
  },
  {
    "id": 42,
    "first_name": "DeAndre'",
    "last_name": "Bembry",
    "position": "F",
    "height": "6-5",
    "weight": "210",
    "jersey_number": "95",
    "college": "St. Joseph's (PA)",
    "country": "USA",
    "draft_year": 2016,
    "draft_round": 1,
    "draft_number": 21,
    "team": {
      "id": 17,
      "conference": "East",
      "division": "Central",
      "city": "Milwaukee",
      "name": "Bucks",
      "full_name": "Milwaukee Bucks",
      "abbreviation": "MIL"
    }
  },
  {
    "id": 43,
    "first_name": "Dragan",
    "last_name": "Bender",
    "position": "F",
    "height": "7-1",
    "weight": "225",
    "jersey_number": "35",
    "college": "Maccabi Tel Aviv",
    "country": "Croatia",
    "draft_year": 2016,
    "draft_round": 1,
    "draft_number": 4,
    "team": {
      "id": 24,
      "conference": "West",
      "division": "Pacific",
      "city": "Phoenix",
      "name": "Suns",
      "full_name": "Phoenix Suns",
      "abbreviation": "PHX"
    }
  },
  {
    "id": 44,
    "first_name": "Davis",
    "last_name": "Bertans",
    "position": "F",
    "height": "6-10",
    "weight": "225",
    "jersey_number": "9",
    "college": "Baskonia",
    "country": "Latvia",
    "draft_year": 2011,
    "draft_round": 2,
    "draft_number": 42,
    "team": {
      "id": 4,
      "conference": "East",
      "division": "Southeast",
      "city": "Charlotte",
      "name": "Hornets",
      "full_name": "Charlotte Hornets",
      "abbreviation": "CHA"
    }
  },
  {
    "id": 45,
    "first_name": "Patrick",
    "last_name": "Beverley",
    "position": "G",
    "height": "6-2",
    "weight": "180",
    "jersey_number": "21",
    "college": "Arkansas",
    "country": "USA",
    "draft_year": 2009,
    "draft_round": 2,
    "draft_number": 42,
    "team": {
      "id": 17,
      "conference": "East",
      "division": "Central",
      "city": "Milwaukee",
      "name": "Bucks",
      "full_name": "Milwaukee Bucks",
      "abbreviation": "MIL"
    }
  },
  {
    "id": 46,
    "first_name": "Khem",
    "last_name": "Birch",
    "position": "C",
    "height": "6-8",
    "weight": "233",
    "jersey_number": "24",
    "college": "UNLV",
    "country": "Canada",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 27,
      "conference": "West",
      "division": "Southwest",
      "city": "San Antonio",
      "name": "Spurs",
      "full_name": "San Antonio Spurs",
      "abbreviation": "SAS"
    }
  },
  {
    "id": 47,
    "first_name": "Jabari",
    "last_name": "Bird",
    "position": "G",
    "height": "6-6",
    "weight": "198",
    "jersey_number": "26",
    "college": "California",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 56,
    "team": {
      "id": 2,
      "conference": "East",
      "division": "Atlantic",
      "city": "Boston",
      "name": "Celtics",
      "full_name": "Boston Celtics",
      "abbreviation": "BOS"
    }
  },
  {
    "id": 48,
    "first_name": "Bismack",
    "last_name": "Biyombo",
    "position": "C",
    "height": "6-8",
    "weight": "255",
    "jersey_number": "15",
    "college": "Baloncesto Fuenlabrada",
    "country": "Democratic Republic of the Congo",
    "draft_year": 2011,
    "draft_round": 1,
    "draft_number": 7,
    "team": {
      "id": 21,
      "conference": "West",
      "division": "Northwest",
      "city": "Oklahoma City",
      "name": "Thunder",
      "full_name": "Oklahoma City Thunder",
      "abbreviation": "OKC"
    }
  },
  {
    "id": 49,
    "first_name": "Nemanja",
    "last_name": "Bjelica",
    "position": "F",
    "height": "6-9",
    "weight": "234",
    "jersey_number": "8",
    "college": "Fenerbahce",
    "country": "Serbia",
    "draft_year": 2010,
    "draft_round": 2,
    "draft_number": 35,
    "team": {
      "id": 10,
      "conference": "West",
      "division": "Pacific",
      "city": "Golden State",
      "name": "Warriors",
      "full_name": "Golden State Warriors",
      "abbreviation": "GSW"
    }
  },
  {
    "id": 50,
    "first_name": "Antonio",
    "last_name": "Blakeney",
    "position": "G",
    "height": "6-4",
    "weight": "192",
    "jersey_number": "9",
    "college": "Louisiana State",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 5,
      "conference": "East",
      "division": "Central",
      "city": "Chicago",
      "name": "Bulls",
      "full_name": "Chicago Bulls",
      "abbreviation": "CHI"
    }
  },
  {
    "id": 51,
    "first_name": "Eric",
    "last_name": "Bledsoe",
    "position": "G",
    "height": "6-1",
    "weight": "214",
    "jersey_number": "5",
    "college": "Kentucky",
    "country": "USA",
    "draft_year": 2010,
    "draft_round": 1,
    "draft_number": 18,
    "team": {
      "id": 25,
      "conference": "West",
      "division": "Northwest",
      "city": "Portland",
      "name": "Trail Blazers",
      "full_name": "Portland Trail Blazers",
      "abbreviation": "POR"
    }
  },
  {
    "id": 52,
    "first_name": "Trevon",
    "last_name": "Bluiett",
    "position": "G-F",
    "height": "6-6",
    "weight": "198",
    "jersey_number": "5",
    "college": "Xavier",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 29,
      "conference": "West",
      "division": "Northwest",
      "city": "Utah",
      "name": "Jazz",
      "full_name": "Utah Jazz",
      "abbreviation": "UTA"
    }
  },
  {
    "id": 53,
    "first_name": "Bogdan",
    "last_name": "Bogdanovic",
    "position": "G",
    "height": "6-5",
    "weight": "225",
    "jersey_number": "13",
    "college": "Fenerbahce",
    "country": "Serbia",
    "draft_year": 2014,
    "draft_round": 1,
    "draft_number": 27,
    "team": {
      "id": 1,
      "conference": "East",
      "division": "Southeast",
      "city": "Atlanta",
      "name": "Hawks",
      "full_name": "Atlanta Hawks",
      "abbreviation": "ATL"
    }
  },
  {
    "id": 54,
    "first_name": "Bojan",
    "last_name": "Bogdanovic",
    "position": "F",
    "height": "6-7",
    "weight": "226",
    "jersey_number": "44",
    "college": "Fenerbahce",
    "country": "Croatia",
    "draft_year": 2011,
    "draft_round": 2,
    "draft_number": 31,
    "team": {
      "id": 3,
      "conference": "East",
      "division": "Atlantic",
      "city": "Brooklyn",
      "name": "Nets",
      "full_name": "Brooklyn Nets",
      "abbreviation": "BKN"
    }
  },
  {
    "id": 55,
    "first_name": "Jonah",
    "last_name": "Bolden",
    "position": "F",
    "height": "6-10",
    "weight": "220",
    "jersey_number": "43",
    "college": "UCLA",
    "country": "Australia",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 36,
    "team": {
      "id": 23,
      "conference": "East",
      "division": "Atlantic",
      "city": "Philadelphia",
      "name": "76ers",
      "full_name": "Philadelphia 76ers",
      "abbreviation": "PHI"
    }
  },
  {
    "id": 56,
    "first_name": "Isaac",
    "last_name": "Bonga",
    "position": "G",
    "height": "6-8",
    "weight": "180",
    "jersey_number": "17",
    "college": "Skyliners Frankfurt",
    "country": "Germany",
    "draft_year": 2018,
    "draft_round": 2,
    "draft_number": 39,
    "team": {
      "id": 28,
      "conference": "East",
      "division": "Atlantic",
      "city": "Toronto",
      "name": "Raptors",
      "full_name": "Toronto Raptors",
      "abbreviation": "TOR"
    }
  },
  {
    "id": 57,
    "first_name": "Devin",
    "last_name": "Booker",
    "position": "G",
    "height": "6-6",
    "weight": "206",
    "jersey_number": "1",
    "college": "Kentucky",
    "country": "USA",
    "draft_year": 2015,
    "draft_round": 1,
    "draft_number": 13,
    "team": {
      "id": 24,
      "conference": "West",
      "division": "Pacific",
      "city": "Phoenix",
      "name": "Suns",
      "full_name": "Phoenix Suns",
      "abbreviation": "PHX"
    }
  },
  {
    "id": 58,
    "first_name": "Chris",
    "last_name": "Boucher",
    "position": "F",
    "height": "6-9",
    "weight": "200",
    "jersey_number": "25",
    "college": "Oregon",
    "country": "Saint Lucia",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 28,
      "conference": "East",
      "division": "Atlantic",
      "city": "Toronto",
      "name": "Raptors",
      "full_name": "Toronto Raptors",
      "abbreviation": "TOR"
    }
  },
  {
    "id": 59,
    "first_name": "Avery",
    "last_name": "Bradley",
    "position": "G",
    "height": "6-3",
    "weight": "180",
    "jersey_number": "20",
    "college": "University of Texas at Austin",
    "country": "USA",
    "draft_year": 2010,
    "draft_round": 1,
    "draft_number": 19,
    "team": {
      "id": 14,
      "conference": "West",
      "division": "Pacific",
      "city": "Los Angeles",
      "name": "Lakers",
      "full_name": "Los Angeles Lakers",
      "abbreviation": "LAL"
    }
  },
  {
    "id": 60,
    "first_name": "Tony",
    "last_name": "Bradley",
    "position": "C",
    "height": "6-10",
    "weight": "248",
    "jersey_number": "13",
    "college": "North Carolina",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 1,
    "draft_number": 28,
    "team": {
      "id": 5,
      "conference": "East",
      "division": "Central",
      "city": "Chicago",
      "name": "Bulls",
      "full_name": "Chicago Bulls",
      "abbreviation": "CHI"
    }
  },
  {
    "id": 61,
    "first_name": "Mikal",
    "last_name": "Bridges",
    "position": "F",
    "height": "6-6",
    "weight": "209",
    "jersey_number": "25",
    "college": "Villanova",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 10,
    "team": {
      "id": 20,
      "conference": "East",
      "division": "Atlantic",
      "city": "New York",
      "name": "Knicks",
      "full_name": "New York Knicks",
      "abbreviation": "NYK"
    }
  },
  {
    "id": 62,
    "first_name": "Miles",
    "last_name": "Bridges",
    "position": "F",
    "height": "6-7",
    "weight": "225",
    "jersey_number": "0",
    "college": "Michigan State",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 12,
    "team": {
      "id": 4,
      "conference": "East",
      "division": "Southeast",
      "city": "Charlotte",
      "name": "Hornets",
      "full_name": "Charlotte Hornets",
      "abbreviation": "CHA"
    }
  },
  {
    "id": 63,
    "first_name": "Isaiah",
    "last_name": "Briscoe",
    "position": "G",
    "height": "6-3",
    "weight": "215",
    "jersey_number": "13",
    "college": "Kentucky",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 22,
      "conference": "East",
      "division": "Southeast",
      "city": "Orlando",
      "name": "Magic",
      "full_name": "Orlando Magic",
      "abbreviation": "ORL"
    }
  },
  {
    "id": 64,
    "first_name": "Ryan",
    "last_name": "Broekhoff",
    "position": "G-F",
    "height": "6-6",
    "weight": "215",
    "jersey_number": "45",
    "college": "Valparaiso",
    "country": "Australia",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 7,
      "conference": "West",
      "division": "Southwest",
      "city": "Dallas",
      "name": "Mavericks",
      "full_name": "Dallas Mavericks",
      "abbreviation": "DAL"
    }
  },
  {
    "id": 65,
    "first_name": "Malcolm",
    "last_name": "Brogdon",
    "position": "G",
    "height": "6-4",
    "weight": "229",
    "jersey_number": "15",
    "college": "Virginia",
    "country": "USA",
    "draft_year": 2016,
    "draft_round": 2,
    "draft_number": 36,
    "team": {
      "id": 30,
      "conference": "East",
      "division": "Southeast",
      "city": "Washington",
      "name": "Wizards",
      "full_name": "Washington Wizards",
      "abbreviation": "WAS"
    }
  },
  {
    "id": 66,
    "first_name": "Dillon",
    "last_name": "Brooks",
    "position": "G-F",
    "height": "6-6",
    "weight": "225",
    "jersey_number": "9",
    "college": "Oregon",
    "country": "Canada",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 45,
    "team": {
      "id": 11,
      "conference": "West",
      "division": "Southwest",
      "city": "Houston",
      "name": "Rockets",
      "full_name": "Houston Rockets",
      "abbreviation": "HOU"
    }
  },
  {
    "id": 67,
    "first_name": "MarShon",
    "last_name": "Brooks",
    "position": "G",
    "height": "6-5",
    "weight": "200",
    "jersey_number": "8",
    "college": "Providence",
    "country": "USA",
    "draft_year": 2011,
    "draft_round": 1,
    "draft_number": 25,
    "team": {
      "id": 3,
      "conference": "East",
      "division": "Atlantic",
      "city": "Brooklyn",
      "name": "Nets",
      "full_name": "Brooklyn Nets",
      "abbreviation": "BKN"
    }
  },
  {
    "id": 68,
    "first_name": "Troy",
    "last_name": "Brown Jr.",
    "position": "F",
    "height": "6-7",
    "weight": "215",
    "jersey_number": "7",
    "college": "Oregon",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 15,
    "team": {
      "id": 9,
      "conference": "East",
      "division": "Central",
      "city": "Detroit",
      "name": "Pistons",
      "full_name": "Detroit Pistons",
      "abbreviation": "DET"
    }
  },
  {
    "id": 69,
    "first_name": "Bruce",
    "last_name": "Brown",
    "position": "G",
    "height": "6-4",
    "weight": "202",
    "jersey_number": "11",
    "college": "Miami",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 2,
    "draft_number": 42,
    "team": {
      "id": 28,
      "conference": "East",
      "division": "Atlantic",
      "city": "Toronto",
      "name": "Raptors",
      "full_name": "Toronto Raptors",
      "abbreviation": "TOR"
    }
  },
  {
    "id": 70,
    "first_name": "Jaylen",
    "last_name": "Brown",
    "position": "G",
    "height": "6-6",
    "weight": "223",
    "jersey_number": "7",
    "college": "California",
    "country": "USA",
    "draft_year": 2016,
    "draft_round": 1,
    "draft_number": 3,
    "team": {
      "id": 2,
      "conference": "East",
      "division": "Atlantic",
      "city": "Boston",
      "name": "Celtics",
      "full_name": "Boston Celtics",
      "abbreviation": "BOS"
    }
  },
  {
    "id": 71,
    "first_name": "Lorenzo",
    "last_name": "Brown",
    "position": "G",
    "height": "6-5",
    "weight": "189",
    "jersey_number": "4",
    "college": "North Carolina State",
    "country": "USA",
    "draft_year": 2013,
    "draft_round": 2,
    "draft_number": 52,
    "team": {
      "id": 28,
      "conference": "East",
      "division": "Atlantic",
      "city": "Toronto",
      "name": "Raptors",
      "full_name": "Toronto Raptors",
      "abbreviation": "TOR"
    }
  },
  {
    "id": 72,
    "first_name": "Sterling",
    "last_name": "Brown",
    "position": "G",
    "height": "6-5",
    "weight": "219",
    "jersey_number": "0",
    "college": "Southern Methodist",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 46,
    "team": {
      "id": 14,
      "conference": "West",
      "division": "Pacific",
      "city": "Los Angeles",
      "name": "Lakers",
      "full_name": "Los Angeles Lakers",
      "abbreviation": "LAL"
    }
  },
  {
    "id": 73,
    "first_name": "Jalen",
    "last_name": "Brunson",
    "position": "G",
    "height": "6-2",
    "weight": "190",
    "jersey_number": "11",
    "college": "Villanova",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 2,
    "draft_number": 33,
    "team": {
      "id": 20,
      "conference": "East",
      "division": "Atlantic",
      "city": "New York",
      "name": "Knicks",
      "full_name": "New York Knicks",
      "abbreviation": "NYK"
    }
  },
  {
    "id": 74,
    "first_name": "Thomas",
    "last_name": "Bryant",
    "position": "C",
    "height": "6-10",
    "weight": "248",
    "jersey_number": "31",
    "college": "Indiana",
    "country": "USA",
    "draft_year": 2017,
    "draft_round": 2,
    "draft_number": 42,
    "team": {
      "id": 16,
      "conference": "East",
      "division": "Southeast",
      "city": "Miami",
      "name": "Heat",
      "full_name": "Miami Heat",
      "abbreviation": "MIA"
    }
  },
  {
    "id": 75,
    "first_name": "Reggie",
    "last_name": "Bullock",
    "position": "G-F",
    "height": "6-6",
    "weight": "205",
    "jersey_number": "25",
    "college": "North Carolina",
    "country": "USA",
    "draft_year": 2013,
    "draft_round": 1,
    "draft_number": 25,
    "team": {
      "id": 11,
      "conference": "West",
      "division": "Southwest",
      "city": "Houston",
      "name": "Rockets",
      "full_name": "Houston Rockets",
      "abbreviation": "HOU"
    }
  },
  {
    "id": 76,
    "first_name": "Trey",
    "last_name": "Burke",
    "position": "G",
    "height": "6-0",
    "weight": "185",
    "jersey_number": "3",
    "college": "Michigan",
    "country": "USA",
    "draft_year": 2013,
    "draft_round": 1,
    "draft_number": 9,
    "team": {
      "id": 7,
      "conference": "West",
      "division": "Southwest",
      "city": "Dallas",
      "name": "Mavericks",
      "full_name": "Dallas Mavericks",
      "abbreviation": "DAL"
    }
  },
  {
    "id": 77,
    "first_name": "Alec",
    "last_name": "Burks",
    "position": "G",
    "height": "6-5",
    "weight": "214",
    "jersey_number": "18",
    "college": "Colorado",
    "country": "USA",
    "draft_year": 2011,
    "draft_round": 1,
    "draft_number": 12,
    "team": {
      "id": 16,
      "conference": "East",
      "division": "Southeast",
      "city": "Miami",
      "name": "Heat",
      "full_name": "Miami Heat",
      "abbreviation": "MIA"
    }
  },
  {
    "id": 78,
    "first_name": "Deonte",
    "last_name": "Burton",
    "position": "G",
    "height": "6-4",
    "weight": "240",
    "jersey_number": "30",
    "college": "Iowa State",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 21,
      "conference": "West",
      "division": "Northwest",
      "city": "Oklahoma City",
      "name": "Thunder",
      "full_name": "Oklahoma City Thunder",
      "abbreviation": "OKC"
    }
  },
  {
    "id": 79,
    "first_name": "Jimmy",
    "last_name": "Butler",
    "position": "G-F",
    "height": "6-7",
    "weight": "230",
    "jersey_number": "22",
    "college": "Marquette",
    "country": "USA",
    "draft_year": 2011,
    "draft_round": 1,
    "draft_number": 30,
    "team": {
      "id": 16,
      "conference": "East",
      "division": "Southeast",
      "city": "Miami",
      "name": "Heat",
      "full_name": "Miami Heat",
      "abbreviation": "MIA"
    }
  },
  {
    "id": 80,
    "first_name": "Jose",
    "last_name": "Calderon",
    "position": "G",
    "height": "6-3",
    "weight": "200",
    "jersey_number": "81",
    "college": "Tau Ceramica",
    "country": "Spain",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 28,
      "conference": "East",
      "division": "Atlantic",
      "city": "Toronto",
      "name": "Raptors",
      "full_name": "Toronto Raptors",
      "abbreviation": "TOR"
    }
  },
  {
    "id": 81,
    "first_name": "Kentavious",
    "last_name": "Caldwell-Pope",
    "position": "G",
    "height": "6-5",
    "weight": "204",
    "jersey_number": "3",
    "college": "Georgia",
    "country": "USA",
    "draft_year": 2013,
    "draft_round": 1,
    "draft_number": 8,
    "team": {
      "id": 22,
      "conference": "East",
      "division": "Southeast",
      "city": "Orlando",
      "name": "Magic",
      "full_name": "Orlando Magic",
      "abbreviation": "ORL"
    }
  },
  {
    "id": 82,
    "first_name": "Isaiah",
    "last_name": "Canaan",
    "position": "G",
    "height": "6-0",
    "weight": "201",
    "jersey_number": "0",
    "college": "Murray State",
    "country": "USA",
    "draft_year": 2013,
    "draft_round": 2,
    "draft_number": 34,
    "team": {
      "id": 23,
      "conference": "East",
      "division": "Atlantic",
      "city": "Philadelphia",
      "name": "76ers",
      "full_name": "Philadelphia 76ers",
      "abbreviation": "PHI"
    }
  },
  {
    "id": 83,
    "first_name": "Clint",
    "last_name": "Capela",
    "position": "C",
    "height": "6-10",
    "weight": "256",
    "jersey_number": "15",
    "college": "Elan Chalon",
    "country": "Switzerland",
    "draft_year": 2014,
    "draft_round": 1,
    "draft_number": 25,
    "team": {
      "id": 1,
      "conference": "East",
      "division": "Southeast",
      "city": "Atlanta",
      "name": "Hawks",
      "full_name": "Atlanta Hawks",
      "abbreviation": "ATL"
    }
  },
  {
    "id": 84,
    "first_name": "DeMarre",
    "last_name": "Carroll",
    "position": "F",
    "height": "6-6",
    "weight": "215",
    "jersey_number": "9",
    "college": "Missouri",
    "country": "USA",
    "draft_year": 2009,
    "draft_round": 1,
    "draft_number": 27,
    "team": {
      "id": 1,
      "conference": "East",
      "division": "Southeast",
      "city": "Atlanta",
      "name": "Hawks",
      "full_name": "Atlanta Hawks",
      "abbreviation": "ATL"
    }
  },
  {
    "id": 85,
    "first_name": "Wendell",
    "last_name": "Carter Jr.",
    "position": "F",
    "height": "6-10",
    "weight": "270",
    "jersey_number": "34",
    "college": "Duke",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 1,
    "draft_number": 7,
    "team": {
      "id": 22,
      "conference": "East",
      "division": "Southeast",
      "city": "Orlando",
      "name": "Magic",
      "full_name": "Orlando Magic",
      "abbreviation": "ORL"
    }
  },
  {
    "id": 86,
    "first_name": "Michael",
    "last_name": "Carter-Williams",
    "position": "G",
    "height": "6-5",
    "weight": "190",
    "jersey_number": "11",
    "college": "Syracuse",
    "country": "USA",
    "draft_year": 2013,
    "draft_round": 1,
    "draft_number": 11,
    "team": {
      "id": 22,
      "conference": "East",
      "division": "Southeast",
      "city": "Orlando",
      "name": "Magic",
      "full_name": "Orlando Magic",
      "abbreviation": "ORL"
    }
  },
  {
    "id": 87,
    "first_name": "Jevon",
    "last_name": "Carter",
    "position": "G",
    "height": "6-1",
    "weight": "200",
    "jersey_number": "5",
    "college": "West Virginia",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": 2,
    "draft_number": 32,
    "team": {
      "id": 5,
      "conference": "East",
      "division": "Central",
      "city": "Chicago",
      "name": "Bulls",
      "full_name": "Chicago Bulls",
      "abbreviation": "CHI"
    }
  },
  {
    "id": 88,
    "first_name": "Vince",
    "last_name": "Carter",
    "position": "F-G",
    "height": "6-6",
    "weight": "220",
    "jersey_number": "15",
    "college": "North Carolina",
    "country": "USA",
    "draft_year": 1998,
    "draft_round": 1,
    "draft_number": 5,
    "team": {
      "id": 28,
      "conference": "East",
      "division": "Atlantic",
      "city": "Toronto",
      "name": "Raptors",
      "full_name": "Toronto Raptors",
      "abbreviation": "TOR"
    }
  },
  {
    "id": 89,
    "first_name": "Alex",
    "last_name": "Caruso",
    "position": "G",
    "height": "6-5",
    "weight": "186",
    "jersey_number": "9",
    "college": "Texas A&M",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 21,
      "conference": "West",
      "division": "Northwest",
      "city": "Oklahoma City",
      "name": "Thunder",
      "full_name": "Oklahoma City Thunder",
      "abbreviation": "OKC"
    }
  },
  {
    "id": 90,
    "first_name": "Omri",
    "last_name": "Casspi",
    "position": "F",
    "height": "6-9",
    "weight": "225",
    "jersey_number": "18",
    "college": "Maccabi Tel Aviv",
    "country": "Israel",
    "draft_year": 2009,
    "draft_round": 1,
    "draft_number": 23,
    "team": {
      "id": 26,
      "conference": "West",
      "division": "Pacific",
      "city": "Sacramento",
      "name": "Kings",
      "full_name": "Sacramento Kings",
      "abbreviation": "SAC"
    }
  },
  {
    "id": 91,
    "first_name": "Willie",
    "last_name": "Cauley-Stein",
    "position": "C",
    "height": "7-0",
    "weight": "240",
    "jersey_number": "00",
    "college": "Kentucky",
    "country": "USA",
    "draft_year": 2015,
    "draft_round": 1,
    "draft_number": 6,
    "team": {
      "id": 23,
      "conference": "East",
      "division": "Atlantic",
      "city": "Philadelphia",
      "name": "76ers",
      "full_name": "Philadelphia 76ers",
      "abbreviation": "PHI"
    }
  },
  {
    "id": 92,
    "first_name": "Troy",
    "last_name": "Caupain",
    "position": "G",
    "height": "6-4",
    "weight": "210",
    "jersey_number": "3",
    "college": "Cincinnati",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 22,
      "conference": "East",
      "division": "Southeast",
      "city": "Orlando",
      "name": "Magic",
      "full_name": "Orlando Magic",
      "abbreviation": "ORL"
    }
  },
  {
    "id": 93,
    "first_name": "Tyler",
    "last_name": "Cavanaugh",
    "position": "F",
    "height": "6-9",
    "weight": "238",
    "jersey_number": "34",
    "college": "George Washington",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 1,
      "conference": "East",
      "division": "Southeast",
      "city": "Atlanta",
      "name": "Hawks",
      "full_name": "Atlanta Hawks",
      "abbreviation": "ATL"
    }
  },
  {
    "id": 94,
    "first_name": "Tyson",
    "last_name": "Chandler",
    "position": "C",
    "height": "7-0",
    "weight": "235",
    "jersey_number": "6",
    "college": "Dominguez HS (CA)",
    "country": "USA",
    "draft_year": 2001,
    "draft_round": 1,
    "draft_number": 2,
    "team": {
      "id": 20,
      "conference": "East",
      "division": "Atlantic",
      "city": "New York",
      "name": "Knicks",
      "full_name": "New York Knicks",
      "abbreviation": "NYK"
    }
  },
  {
    "id": 95,
    "first_name": "Wilson",
    "last_name": "Chandler",
    "position": "F",
    "height": "6-8",
    "weight": "235",
    "jersey_number": "21",
    "college": "DePaul",
    "country": "USA",
    "draft_year": 2007,
    "draft_round": 1,
    "draft_number": 23,
    "team": {
      "id": 8,
      "conference": "West",
      "division": "Northwest",
      "city": "Denver",
      "name": "Nuggets",
      "full_name": "Denver Nuggets",
      "abbreviation": "DEN"
    }
  },
  {
    "id": 96,
    "first_name": "Joe",
    "last_name": "Chealey",
    "position": "G",
    "height": "6-3",
    "weight": "190",
    "jersey_number": "31",
    "college": "College of Charleston",
    "country": "USA",
    "draft_year": 2018,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 4,
      "conference": "East",
      "division": "Southeast",
      "city": "Charlotte",
      "name": "Hornets",
      "full_name": "Charlotte Hornets",
      "abbreviation": "CHA"
    }
  },
  {
    "id": 97,
    "first_name": "Marquese",
    "last_name": "Chriss",
    "position": "F",
    "height": "6-9",
    "weight": "240",
    "jersey_number": "35",
    "college": "Washington",
    "country": "USA",
    "draft_year": 2016,
    "draft_round": 1,
    "draft_number": 8,
    "team": {
      "id": 7,
      "conference": "West",
      "division": "Southwest",
      "city": "Dallas",
      "name": "Mavericks",
      "full_name": "Dallas Mavericks",
      "abbreviation": "DAL"
    }
  },
  {
    "id": 98,
    "first_name": "Gary",
    "last_name": "Clark",
    "position": "F",
    "height": "6-6",
    "weight": "225",
    "jersey_number": "12",
    "college": "Cincinnati",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 19,
      "conference": "West",
      "division": "Southwest",
      "city": "New Orleans",
      "name": "Pelicans",
      "full_name": "New Orleans Pelicans",
      "abbreviation": "NOP"
    }
  },
  {
    "id": 99,
    "first_name": "Ian",
    "last_name": "Clark",
    "position": "G",
    "height": "6-3",
    "weight": "175",
    "jersey_number": "2",
    "college": "Belmont",
    "country": "USA",
    "draft_year": None,
    "draft_round": None,
    "draft_number": None,
    "team": {
      "id": 10,
      "conference": "West",
      "division": "Pacific",
      "city": "Golden State",
      "name": "Warriors",
      "full_name": "Golden State Warriors",
      "abbreviation": "GSW"
    }
  },
  {
    "id": 100,
    "first_name": "Jordan",
    "last_name": "Clarkson",
    "position": "G",
    "height": "6-3",
    "weight": "194",
    "jersey_number": "00",
    "college": "Missouri",
    "country": "USA",
    "draft_year": 2014,
    "draft_round": 2,
    "draft_number": 46,
    "team": {
      "id": 29,
      "conference": "West",
      "division": "Northwest",
      "city": "Utah",
      "name": "Jazz",
      "full_name": "Utah Jazz",
      "abbreviation": "UTA"
    }
  }
]



# Filter out players where 'draft_year', 'draft_round', or 'draft_number' is None
filtered_players = [player for player in players if player['draft_year'] is not None]

# Extract countries from the filtered players
countries = [player['country'] for player in filtered_players]

# Count occurrences of each country
country_counts = Counter(countries)

# Sort the countries in descending order by the number of players
sorted_country_counts = dict(sorted(country_counts.items(), key=lambda item: item[1], reverse=True))

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_country_counts.keys(), sorted_country_counts.values())
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.title('Number of Players per Country')
plt.xticks(rotation=45)
plt.tight_layout()

# Define the path 
save_path = '/workspaces/codespaces-flask/static/players_per_country_chart.png'

# Save the plot
plt.savefig(save_path)

# Show the plot
plt.show()


def convert_height_to_inches(height):
    feet, inches = height.split('-')
    return int(feet) * 12 + int(inches)

# Weight vs Height (Scatter Plot), Sorted by Height
heights = [convert_height_to_inches(player['height']) for player in players]
weights = [player['weight'] for player in players]

# Sort heights and weights
sorted_heights = sorted(heights)
sorted_weights = sorted(weights)


# Create a scatter plot of sorted weight vs height
plt.figure(figsize=(10, 6))
plt.scatter(sorted_heights, sorted_weights, color='#A1EEBD')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (lbs)')
plt.title('Weight vs Height of Players')
plt.tight_layout()

# Save the scatter plot
plt.savefig('/workspaces/codespaces-flask/static/weight_vs_height_sorted_chart.png')

# Show the plot
plt.show()



#  **Height Distribution (Histogram)**
plt.figure(figsize=(10, 6))
plt.hist(heights, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Height (inches)')
plt.ylabel('Number of Players')
plt.title('Height Distribution of Players')
plt.tight_layout()
plt.savefig('/workspaces/codespaces-flask/static/height_distribution_chart.png')
plt.show()

