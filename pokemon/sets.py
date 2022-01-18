from pokemontcgsdk import RestClient
from pokemontcgsdk import Set
import csv
import datetime

RestClient.configure('b5811667-5697-4cd7-8179-e8bb9c8e5e5c')

HEADERS = ['series', 'id', 'name', 'releaseDate', 'printedTotal', 'total', 'legalityUnlimited', 'legalityExpanded', 'legalityStandard']

def create_sets_csv():
    # current_date = str(datetime.datetime.today().strftime ('%d%m%Y'))
    # file_name = "pokemon_sets_" + current_date + ".csv"
    file_name = "pokemon_sets.csv"
    sets = Set.all()
    with open(file_name, 'w') as pokemon:
        pokemon_writer = csv.writer(pokemon, delimiter=',', lineterminator = '\n')
        pokemon_writer.writerow(HEADERS)
        for card_set in sets:
            pokemon_writer.writerow([card_set.series, card_set.id, card_set.name, card_set.releaseDate, card_set.printedTotal, card_set.total,
                                     card_set.legalities.unlimited, card_set.legalities.expanded, card_set.legalities.standard])