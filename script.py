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