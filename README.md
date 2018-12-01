# HikeTrack Project
READ ME Created by Edward Im @ 12/1/2018

BASIC INFORMATION
This is a personal project done as a assignment for a coding bootcamp assignment. The project started as a way to create
a free and easy way for users to search for hiking trails and to create and join trips that they would like to go on with other users.
Functionalities include:
1. Login and Registration w/validations
2. Searching for popular trails using a city location
3. Seeing other users planned trips and joining.
4. Ability to set overnight trips


TECHNOLOGY USED
The back-end of this application was written in Python 3.7 and using Django 2.1 framework and SQLite for it's database.
As for the front-end of the application, I used Bootstrap as a framework.

API USED
The application uses Google Geolocation API and REI Hiking Project API together to show it's users the trail data according
to the location inputed. Since the only parameters accepted by the REI API are longitude and latitude coordinates, The application
first makes a call to Google Geolocation to turn the city into coordinates and then makes a second call to REI API with the coordinates.

