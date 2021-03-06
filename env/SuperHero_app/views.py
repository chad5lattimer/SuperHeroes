from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
import requests
# Create your views here.


def home(request):

    if 'name' in request.POST:
        name = request.POST['name']
        access_token = '10158877596033137'
        api_url = 'https://superheroapi.com/api/'+access_token+'/search/'+name
        api_data = requests.get(api_url)
        api_json = api_data.json()
        
        api_response = api_json
        heroPicture= api_response["results"][0]["image"]["url"]
        heroName= api_response["results"][0]['name']
        intelligence= api_response["results"][0]['powerstats']['intelligence']
        strength= api_response["results"][0]['powerstats']['strength']
        durability= api_response["results"][0]['powerstats']['durability']
        power= api_response["results"][0]['powerstats']['power']
        combat= api_response["results"][0]['powerstats']['combat']
        
        name = request.POST['card3']
        access_token = '10158877596033137'
        api_url = 'https://superheroapi.com/api/'+access_token+'/search/'+name
        api_data = requests.get(api_url)
        api_json = api_data.json()
          
        api_response = api_json
        heroPicture2= api_response["results"][0]["image"]["url"]
        heroName2= api_response["results"][0]['name']
        intelligence2= api_response["results"][0]['powerstats']['intelligence']
        strength2= api_response["results"][0]['powerstats']['strength']
        durability2= api_response["results"][0]['powerstats']['durability']
        power2= api_response["results"][0]['powerstats']['power']
        combat2= api_response["results"][0]['powerstats']['combat']
          
          
        
        
        
        context={     
        "heroPicture": heroPicture,
        "heroName": heroName,
        "intelligence": intelligence,
        "strength": strength,
        "durability":durability,
        "power": power,
        "combat":combat,
        "heroPicture2": heroPicture2,
        "heroName2": heroName2,
        "intelligence2": intelligence2,
        "strength2": strength2,
        "durability2":durability2,
        "power2": power2,
        "combat2":combat2,  
        }
    else:
        context={
        
        }
        
        
        
   
        
        
    return render(request, 'SuperHero_app/index.html', context )

def about(request):
  return render(request, 'SuperHero_app/about.html')





def style(request):
  return render(request, 'style.htm')



{
  "response": "success",
  "results-for": "batman",
  "results": [
    {
      "id": "69",
      "name": "Batman",
      "powerstats": {
        "intelligence": "81",
        "strength": "40",
        "speed": "29",
        "durability": "55",
        "power": "63",
        "combat": "90"
      },
      "biography": {
        "full-name": "Terry McGinnis",
        "alter-egos": "No alter egos found.",
        "aliases": [
          "Batman II",
          "The Tomorrow Knight",
          "The second Dark Knight",
          "The Dark Knight of Tomorrow",
          "Batman Beyond"
        ],
        "place-of-birth": "Gotham City, 25th Century",
        "first-appearance": "Batman Beyond #1",
        "publisher": "DC Comics",
        "alignment": "good"
      },
      "appearance": {
        "gender": "Male",
        "race": "Human",
        "height": [
          "5'10",
          "178 cm"
        ],
        "weight": [
          "170 lb",
          "77 kg"
        ],
        "eye-color": "Blue",
        "hair-color": "Black"
      },
      "work": {
        "occupation": "-",
        "base": "21st Century Gotham City"
      },
      "connections": {
        "group-affiliation": "Batman Family, Justice League Unlimited",
        "relatives": "Bruce Wayne (biological father), Warren McGinnis (father, deceased), Mary McGinnis (mother), Matt McGinnis (brother)"
      },
      "image": {
        "url": "https://www.superherodb.com/pictures2/portraits/10/100/10441.jpg"
      }
    },
    {
      "id": "70",
      "name": "Batman",
      "powerstats": {
        "intelligence": "100",
        "strength": "26",
        "speed": "27",
        "durability": "50",
        "power": "47",
        "combat": "100"
      },
      "biography": {
        "full-name": "Bruce Wayne",
        "alter-egos": "No alter egos found.",
        "aliases": [
          "Insider",
          "Matches Malone"
        ],
        "place-of-birth": "Crest Hill, Bristol Township; Gotham County",
        "first-appearance": "Detective Comics #27",
        "publisher": "DC Comics",
        "alignment": "good"
      },
      "appearance": {
        "gender": "Male",
        "race": "Human",
        "height": [
          "6'2",
          "188 cm"
        ],
        "weight": [
          "210 lb",
          "95 kg"
        ],
        "eye-color": "blue",
        "hair-color": "black"
      },
      "work": {
        "occupation": "Businessman",
        "base": "Batcave, Stately Wayne Manor, Gotham City; Hall of Justice, Justice League Watchtower"
      },
      "connections": {
        "group-affiliation": "Batman Family, Batman Incorporated, Justice League, Outsiders, Wayne Enterprises, Club of Heroes, formerly White Lantern Corps, Sinestro Corps",
        "relatives": "Damian Wayne (son), Dick Grayson (adopted son), Tim Drake (adopted son), Jason Todd (adopted son), Cassandra Cain (adopted ward)\nMartha Wayne (mother, deceased), Thomas Wayne (father, deceased), Alfred Pennyworth (former guardian), Roderick Kane (grandfather, deceased), Elizabeth Kane (grandmother, deceased), Nathan Kane (uncle, deceased), Simon Hurt (ancestor), Wayne Family"
      },
      "image": {
        "url": "https://www.superherodb.com/pictures2/portraits/10/100/639.jpg"
      }
    },
    {
      "id": "71",
      "name": "Batman II",
      "powerstats": {
        "intelligence": "88",
        "strength": "11",
        "speed": "33",
        "durability": "28",
        "power": "36",
        "combat": "100"
      },
      "biography": {
        "full-name": "Dick Grayson",
        "alter-egos": "Nightwing, Robin",
        "aliases": [
          "Dick Grayson"
        ],
        "place-of-birth": "-",
        "first-appearance": "-",
        "publisher": "Nightwing",
        "alignment": "good"
      },
      "appearance": {
        "gender": "Male",
        "race": "Human",
        "height": [
          "5'10",
          "178 cm"
        ],
        "weight": [
          "175 lb",
          "79 kg"
        ],
        "eye-color": "Blue",
        "hair-color": "Black"
      },
      "work": {
        "occupation": "-",
        "base": "Gotham City; formerly Bludhaven, New York City"
      },
      "connections": {
        "group-affiliation": "Justice League Of America, Batman Family",
        "relatives": "John Grayson (father, deceased), Mary Grayson (mother, deceased), Bruce Wayne / Batman (adoptive father), Damian Wayne / Robin (foster brother), Jason Todd / Red Hood (adoptive brother), Tim Drake / Red Robin (adoptive brother), Cassandra Cain / Batgirl IV (adoptive sister)"
      },
      "image": {
        "url": "https://www.superherodb.com/pictures2/portraits/10/100/1496.jpg"
      }
    }
  ]
}