import json
import requests
import os


class apiCall():
    def __init__(self) -> None:
        api_path = os.path.join(os.path.dirname(__file__),'api_path.json')
        self.api_urls = json.load(open(api_path))
        

    def getData(self, url):
        headers = {'User-Agent': 'swapi-python'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception('Not able to get the resource')
        return response

    def getSpecificPersonData(self,personid):
        url = self.api_urls['people'] + str(personid)
        resp = self.getData(url) 
        resp_data = resp.json()
        return resp_data  

    def getSpecificFilmData(self,filmid):
        url = self.api_urls['films'] + str(filmid)
        resp = self.getData(url) 
        resp_data = resp.json()
        return resp_data

    def getSpecificPlanetData(self,planetid):
        url = self.api_urls['planets'] + str(planetid)
        resp = self.getData(url) 
        resp_data = resp.json()
        return resp_data

    def getSpecificSpeciesData(self,speciesid):
        url = self.api_urls['species'] + str(speciesid)
        resp = self.getData(url) 
        resp_data = resp.json()
        return resp_data

    def getSpecificStarshipData(self,starshipid):
        url = self.api_urls['starships'] + str(starshipid)
        resp = self.getData(url) 
        resp_data = resp.json()
        return resp_data 
    
    def getSpecificVehicleData(self,vehicleid):
        url = self.api_urls['vehicles'] + str(vehicleid)
        resp = self.getData(url) 
        resp_data = resp.json()
        return resp_data
    
    def getAllPersonsData(self):
        present_url = self.api_urls['people']
        flag = True
        all_people_data = {}
        num_of_people = 0
        total_people_data = []
        while flag:
            resp = self.getData(present_url)
            resp_data = resp.json()
            next_url = resp_data['next']
            num_of_people = resp_data['count']
            total_people_data.extend(resp_data['results'])
            
            if next_url:
                present_url = next_url
            else:
                flag = False
        
        all_people_data['count'] = num_of_people
        all_people_data['people_data'] = total_people_data

        return all_people_data

    




