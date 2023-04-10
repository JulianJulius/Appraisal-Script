import requests
from bs4 import BeautifulSoup

def fetch_average_ebay_price(player_name, card_year, card_condition, rarity):
    search_query = f"{player_name} {card_year} baseball card {card_condition} {rarity}"
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_query}&_sacat=0&LH_Sold=1&LH_Complete=1"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    sold_items = soup.find_all("li", class_="s-item")
    total_price = 0
    num_items = 0

    for item in sold_items:
        price_str = item.find("span", class_="s-item__price").text
        price = float(price_str.replace("$", "").replace(",", ""))
        total_price += price
        num_items += 1

    average_price = total_price / num_items if num_items > 0 else 0
    return average_price

if __name__ == "__main__":
    player_name = input("Enter player's name: ")
    card_year = int(input("Enter card year: "))
    card_condition = input("Enter card condition (Mint, Excellent, Good, Fair, Poor): ")
    rarity = input("Enter card rarity (Common, Uncommon, Rare, Very Rare): ")

    average_price = fetch_average_ebay_price(player_name, card_year, card_condition, rarity)
    print(f"Average eBay price for {player_name}'s {card_year} card in {card_condition} condition ({rarity}): ${average_price:.2f}")
