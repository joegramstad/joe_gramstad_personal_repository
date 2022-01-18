from pokemontcgsdk import RestClient
from pokemontcgsdk import Type
import csv
from cards import create_cards_csv

RestClient.configure('b5811667-5697-4cd7-8179-e8bb9c8e5e5c')

# card = Card.find('xy1-1')
# print(card.attacks)
# sets = Set.all()
# with open('pokemon_sets.csv', 'w') as pokemon:
#     pokemon_writer = csv.writer(pokemon, delimiter=',', lineterminator = '\n')
#     pokemon_writer.writerow(['series', 'id', 'name', 'releaseDate', 'printedTotal', 'total', 'legalityUnlimited', 'legalityExpanded', 'legalityStandard'])
#     for card_set in sets:
#         pokemon_writer.writerow([card_set.series, card_set.id, card_set.name, card_set.releaseDate, card_set.printedTotal, card_set.total,
#                                  card_set.legalities.unlimited, card_set.legalities.expanded, card_set.legalities.standard])

create_cards_csv()