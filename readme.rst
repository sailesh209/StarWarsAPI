Usage
========
To run the test suite to run the test cases in apitestcase module
    install HtmlTestRunner


Command line command:
    python3 smoke_suite.py 

Results
=======
Html reports will be generated with the test case results and stored under reports>html_reports folder

TestCases
=========
Total 10 test cases were written to test star wars api.

1.Test If the people endpoint is getting the result back with status code 200
2.Test If the films endpoint is getting the result back with status code 200
3.Test If the planets endpoint is getting the result back with status code 200
4.Test If the species endpoint is getting the result back with status code 200
5.Test If the starships endpoint is getting the result back with status code 200
6.Test If the vehicle endpoint is getting the result back with status code 200
7.Test if the number of people whose height is more than 200 and check the count and check the names of the people whose height is more than 200
8.Test if empire strikes back file data matches with the director and title
9.Test the  planet naboo data with checking films and resident count
10.Test the vehicle snowspeeder data

Methods
=======

getSpecificPersonData(id)
--------------------------
Return single person entire data

getSpecificFilmData(id)
-----------------------
Return single film entire data

getSpecificPlanetData(id)
-------------------------
Return single planet entire data

getSpecificSpeciesData(id)
--------------------------
Return single species entire data

getSpecificStarshipData(id)
----------------------------
Return single starship entire data

getSpecificVehicleData(id)
--------------------------
Return single vehicle entire data

getAllPersonsData()
--------------------
return all people data in the star api universe

getData(url)
-------------
this is the method which takes the url and does the get method with the url and return the response