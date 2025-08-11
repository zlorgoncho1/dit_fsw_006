from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html')

def get_properties():
    return [
        {
            'id': 1,
            'title': 'Maison familiale à Bordeaux',
            'description': '4 chambres, 2 salles de bain, jardin, garage',
            'price': 420000,
            'image': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80',
            'surface': 150,
            'rooms': 4,
            'bathrooms': 2,
            'garage': True,
            'garden': True,
            'city': 'Bordeaux',
            'postal_code': '33000',
            'year_built': 2005,
            'energy_rating': 'B'
        },
        {
            'id': 2,
            'title': 'Appartement moderne à Paris',
            'description': '2 chambres, balcon, proche métro',
            'price': 650000,
            'image': 'https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80',
            'surface': 68,
            'rooms': 2,
            'bathrooms': 1,
            'garage': False,
            'garden': False,
            'city': 'Paris',
            'postal_code': '75015',
            'year_built': 2018,
            'energy_rating': 'A'
        },
        {
            'id': 3,
            'title': 'Villa avec piscine à Nice',  
            'description': '5 chambres, piscine, vue mer',
            'price': 1200000,
            'image': 'https://images.unsplash.com/photo-1507089947368-19c1da9775ae?auto=format&fit=crop&w=400&q=80',
            'surface': 220,
            'rooms': 5,
            'bathrooms': 3,
            'garage': True,
            'garden': True,
            'city': 'Nice',
            'postal_code': '06000',
            'year_built': 2012,
            'energy_rating': 'B',
            'pool': True,
            'sea_view': True
        },
        {
            'id': 4,
            'title': 'Loft contemporain à Lyon',    
            'description': '3 chambres, terrasse, centre-ville',
            'price': 780000,
            'image': 'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&w=400&q=80',
            'surface': 110,
            'rooms': 3,
            'bathrooms': 2,
            'garage': False,
            'garden': False,
            'city': 'Lyon',
            'postal_code': '69002',
            'year_built': 2015,
            'energy_rating': 'A',
            'terrace': True
        },
        {
            'id': 5,
            'title': 'Studio cosy à Toulouse',
            'description': '1 pièce, rénové, proche université',
            'price': 180000,
            'image': 'https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80',
            'surface': 28,
            'rooms': 1,
            'bathrooms': 1,
            'garage': False,
            'garden': False,
            'city': 'Toulouse',
            'postal_code': '31000',
            'year_built': 1998,
            'energy_rating': 'C'
        },
        {
            'id': 6,
            'title': 'Maison de campagne à Sarlat',
            'description': '3 chambres, grand terrain, calme absolu',
            'price': 320000,
            'image': 'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=400&q=80',
            'surface': 130,
            'rooms': 3,
            'bathrooms': 2,
            'garage': True,
            'garden': True,
            'city': 'Sarlat',
            'postal_code': '24200',
            'year_built': 1985,
            'energy_rating': 'D',
            'land_size': 2500
        },
        {
            'id': 7,
            'title': 'Appartement haussmannien à Paris 16e',
            'description': '4 pièces, parquet, moulures, cheminée',
            'price': 950000,
            'image': 'https://images.unsplash.com/photo-1464037866556-6812c9d1c72e?auto=format&fit=crop&w=400&q=80',
            'surface': 120,
            'rooms': 4,
            'bathrooms': 2,
            'garage': False,
            'garden': False,
            'city': 'Paris',
            'postal_code': '75016',
            'year_built': 1890,
            'energy_rating': 'E',
            'fireplace': True
        },
        {
            'id': 8,
            'title': 'Chalet en bois à Chamonix',
            'description': '2 chambres, vue montagne, proche pistes',
            'price': 540000,
            'image': 'https://images.unsplash.com/photo-1503389152951-9c3d8bca6c94?auto=format&fit=crop&w=400&q=80',
            'surface': 75,
            'rooms': 2,
            'bathrooms': 1,
            'garage': True,
            'garden': True,
            'city': 'Chamonix',
            'postal_code': '74400',
            'year_built': 2008,
            'energy_rating': 'C',
            'mountain_view': True,
            'ski_access': True
        },
        {
            'id': 9,
            'title': 'Duplex lumineux à Nantes',
            'description': '3 chambres, dernier étage, terrasse',
            'price': 410000,
            'image': 'https://images.unsplash.com/photo-1460518451285-97b6aa326961?auto=format&fit=crop&w=400&q=80',
            'surface': 95,
            'rooms': 3,
            'bathrooms': 2,
            'garage': False,
            'garden': False,
            'city': 'Nantes',
            'postal_code': '44000',
            'year_built': 2010,
            'energy_rating': 'B',
            'terrace': True,
            'floor': 5
        },
        {
            'id': 10,
            'title': 'Maison de ville à Montpellier',
            'description': '4 chambres, patio, proche tramway',
            'price': 370000,
            'image': 'https://images.unsplash.com/photo-1509395176047-4a66953fd231?auto=format&fit=crop&w=400&q=80',
            'surface': 105,
            'rooms': 4,
            'bathrooms': 2,
            'garage': False,
            'garden': False,
            'city': 'Montpellier',
            'postal_code': '34000',
            'year_built': 1995,
            'energy_rating': 'C',
            'patio': True
        },
        {
            'id': 11,
            'title': 'Penthouse avec vue à Marseille',
            'description': '5 pièces, grande terrasse, vue mer',
            'price': 1350000,
            'image': 'https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80',
            'surface': 180,
            'rooms': 5,
            'bathrooms': 3,
            'garage': True,
            'garden': False,
            'city': 'Marseille',
            'postal_code': '13007',
            'year_built': 2016,
            'energy_rating': 'A',
            'terrace': True,
            'sea_view': True
        },
        {
            'id': 12,
            'title': 'Maison ancienne à Dijon',
            'description': '6 pièces, poutres apparentes, cave voûtée',
            'price': 295000,
            'image': 'https://images.unsplash.com/photo-1460474647541-4edd0cd0c746?auto=format&fit=crop&w=400&q=80',
            'surface': 160,
            'rooms': 6,
            'bathrooms': 2,
            'garage': True,
            'garden': True,
            'city': 'Dijon',
            'postal_code': '21000',
            'year_built': 1850,
            'energy_rating': 'F',
            'cellar': True,
            'exposed_beams': True
        },
        {
            'id': 13,
            'title': 'Appartement neuf à Lille',
            'description': '2 chambres, parking, proche commerces',
            'price': 260000,
            'image': 'https://images.unsplash.com/photo-1465101178521-c1a9136a3c8b?auto=format&fit=crop&w=400&q=80',
            'surface': 60,
            'rooms': 2,
            'bathrooms': 1,
            'garage': True,
            'garden': False,
            'city': 'Lille',
            'postal_code': '59000',
            'year_built': 2022,
            'energy_rating': 'A',
            'parking': True
        },
        {   
            'id': 14,
            'title': 'Villa d’architecte à Biarritz',
            'description': '4 chambres, piscine, design contemporain',
            'price': 1850000,
            'image': 'https://images.unsplash.com/photo-1507089947368-19c1da9775ae?auto=format&fit=crop&w=400&q=80',
            'surface': 250,
            'rooms': 4,
            'bathrooms': 3,
            'garage': True,
            'garden': True,
            'city': 'Biarritz',
            'postal_code': '64200',
            'year_built': 2020,
            'energy_rating': 'A',
            'pool': True,
            'architect_design': True
        },
        {
            'id': 15,
            'title': 'Maison en pierre à Saint-Malo',
            'description': '3 chambres, jardin clos, proche plage',
            'price': 520000,
            'image': 'https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80',
            'surface': 115,
            'rooms': 3,
            'bathrooms': 2,
            'garage': True,
            'garden': True,
            'city': 'Saint-Malo',
            'postal_code': '35400',
            'year_built': 1930,
            'energy_rating': 'D',
            'stone_house': True,
            'beach_access': True
        }
    ]
    

def properties(request):
    sectionTitle = "Propriétés en vedette"
    return render(request, 'properties.html', context={'properties': get_properties(), 'title': sectionTitle})

def property_detail(request, property_id):
    properties = get_properties()
    for property in properties:
        if property['id'] == property_id:
            return render(request, 'property_detail.html', context={'property': property})
    return HttpResponse(f"Propriété non trouvée avec l'ID {property_id}")

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
