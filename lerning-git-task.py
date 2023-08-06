lista_zakupów = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marcher", "seler", "rukola"]
}


lista_zakupów_z_dużej_litery = {key.title(): [item.title(
) for item in value] for key, value in lista_zakupów.items()}


for shop, items in lista_zakupów_z_dużej_litery.items():
    sentence = f"Idę do {shop} i kupuję tam {items}."
    print(sentence)

