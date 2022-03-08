import unittest
from lib.api_call import apiCall


class apiTestcase(unittest.TestCase):
    # This method will be executed only once for this test case class. 
    # It will execute before all test methods. Must decorated with @classmethod.

    @classmethod
    def setUpClass(cls):
        print("setUpClass execute. ")
        
    # Similar with setupClass method, it will be executed after all test method run.    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass execute. ") 
    
    # first test all the api endpoint are providing data
    def test_people_endpoint(self):
        print("test_people endpoint execute.")
        person_data = apiCall().getSpecificPersonData(1)
        self.assertNotEqual(len(person_data), 0)
        self.assertEquals(person_data['name'], "Luke Skywalker")
        
    def test_films_endpoint(self):
        print("test_films endpoint execute.")
        film_data = apiCall().getSpecificFilmData(1)
        self.assertNotEqual(len(film_data), 0)
    
    def test_planets_endpoint(self):
        print("test_planets execute.")
        planet_data = apiCall().getSpecificPlanetData(2)
        self.assertNotEqual(len(planet_data), 0)
    
    def test_species_endpoint(self):
        print("test_species execute.")
        species_data = apiCall().getSpecificSpeciesData(1)
        self.assertNotEqual(len(species_data), 0)
    
    def test_starships_endpoint(self):
        print("test_starships execute.")
        starship_data = apiCall().getSpecificStarshipData(2)
        self.assertNotEqual(len(starship_data), 0)
    
    def test_vehicles_endpoint(self):
        print("test_vehicle execute.")
        vehicle_data = apiCall().getSpecificVehicleData(4)
        self.assertNotEqual(len(vehicle_data), 0)
    
    #This test case is get all the people whose height more than 200
    def test_people_height_more_than_200(self):
        print('test people height data')
        response = apiCall().getAllPersonsData()
        test_data = ['Darth Vader','Chewbacca', 'Roos Tarpals', 'Rugor Nass', 'Yarael Poof', 'Lama Su', 'Tuan We', 'Grievous', 'Tarfful', 'Tion Medon']
        actual_data = []
        all_people_data = response['people_data']
        for person in all_people_data:
            if person['height'] != 'unknown' and int(person['height']) > 200:
                actual_data.append(person['name'])

        self.assertEqual(len(actual_data),10)
        self.assertEqual(response['count'],82)
        self.assertEqual(test_data.sort(),actual_data.sort())

    #Below 3 test cases is to test a partcular film , planet data and vehicle data
    def test_empire_strikes_back_film_data(self):
        print("test_films empire strikes back execute.")
        film_data = apiCall().getSpecificFilmData(2)
        self.assertNotEqual(len(film_data), 0)
        self.assertEqual(film_data['title'],'The Empire Strikes Back')
        self.assertEqual(film_data['director'],"Irvin Kershner")
        
    def test_planet_naboo_data(self):
        print("test_planet naboo execute.")
        planet_data = apiCall().getSpecificPlanetData(8)
        self.assertNotEqual(len(planet_data), 0)
        self.assertEqual(len(planet_data['films']),4)
        self.assertEqual(len(planet_data['residents']),11)
    
    def test_vehicle_snowspeeder_data(self):
        print('test vehicle snowspeeder data')
        vehicle_data = apiCall().getSpecificVehicleData(14)
        self.assertNotEqual(len(vehicle_data), 0)
        self.assertEqual(vehicle_data['vehicle_class'],'airspeeder')
        self.assertEqual(vehicle_data['cargo_capacity'],'10')
    


