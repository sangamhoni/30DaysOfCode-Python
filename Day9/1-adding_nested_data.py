# To add data on the given nested list with a dictionary and a list within a dictionary

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def adding_country(country_name, total_visits, cities):
    new_dict={}
    new_dict['country']=country_name
    new_dict['visits']=total_visits
    new_dict['ciites']=cities
    
    travel_log.append(new_dict)

country=input("Enter the name of country: ")
no_of_visits=int(input("How many times have you visited the country: "))
cities_list=input("Nmae the cities you visited separated by a comma: ").split(", ")

adding_country(country_name=country, total_visits=no_of_visits, cities=cities_list)

print(travel_log)