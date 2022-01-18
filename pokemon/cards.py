from pokemontcgsdk import RestClient
from pokemontcgsdk import Card
import csv
import datetime

RestClient.configure('b5811667-5697-4cd7-8179-e8bb9c8e5e5c')

HEADERS = ['series', 'set_name', 'supertype', 'rarity', 'card_number', 'card_title', 'pokemon', 'pokemon2', 
        'release_date', 'normal_price', 'holo_price', 'rev_holo_price', 'fe_holo_price', 'fe_norm_price']

def create_cards_csv():
    # current_date = str(datetime.datetime.today().strftime ('%d%m%Y'))
    # file_name = "pokemon_sets_" + current_date + ".csv"
    file_name = "pokemon_cards.csv"
    cards = Card.all()
    with open(file_name, 'w', encoding="utf-8") as pokemon:
        pokemon_writer = csv.writer(pokemon, delimiter=',', lineterminator = '\n')
        pokemon_writer.writerow(HEADERS)
        for card in cards:
            def_prices = ["N/A", "N/A", "N/A", "N/A", "N/A"]
            if card.tcgplayer:
                prices_split = prices(card.tcgplayer, def_prices)
            else:
                prices_split = def_prices
            print(card.name)
            if card.supertype == "Pokémon":
                pokemon_num_1, pokemon_num_2 = pokedex(card.nationalPokedexNumbers)
            else:
                pokemon_num_1, pokemon_num_2 = "N/A", "N/A"
            pokemon_writer.writerow([card.set.series, card.set.name, card.supertype, card.rarity, card.number, card.name, 
                                     pokemon_num_1, pokemon_num_2, card.set.releaseDate, prices_split[0],
                                     prices_split[1], prices_split[2], prices_split[3], prices_split[4]])

def pokedex(pokedex_nums):
    if pokedex_nums:
        num1 = min(pokedex_nums)
        num2 = max(pokedex_nums)
        if num1 == num2:
            num2 = "N/A"
        return num1, num2
    else:
        return "N/A", "N/A"

def types(poke_types):
    if poke_types:
        type1 = poke_types[0]
        if len(poke_types) > 1:
            type2 = poke_types[1]
        else:
            type2 = "N/A"
        return type1, type2
    else:
        return "N/A", "N/A"

def prices(tcgplayer, prices):
    if (tcgprices := tcgplayer.prices):
        if tcgprices.normal:
            prices[0] = tcgprices.normal.market
        if tcgprices.holofoil:
            prices[1] = tcgprices.holofoil.market
        if tcgprices.reverseHolofoil:
            prices[2] = tcgprices.reverseHolofoil.market
        if tcgprices.firstEditionHolofoil:
            prices[3] = tcgprices.firstEditionHolofoil.market
        if tcgprices.firstEditionNormal:
            prices[4] = tcgprices.firstEditionNormal.market

    return prices