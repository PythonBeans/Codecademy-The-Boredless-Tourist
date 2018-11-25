destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = []
for destination in destinations:
  attractions.append([])

def get_destination_index(destination):
  for i in range(len(destinations)):
    if destination == destinations[i]:
      destination_index = i
      return destination_index
      break
  return "Typo???"
  
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index


def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except TypeError:
    print("Error caught!")
  return

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attractions_with_interest.append(possible_attraction[0])
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest == attraction_tags:
        attractions_with_interest.append(possible_attraction)
  return attractions_with_interest

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
