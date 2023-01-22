import requests
from dataclasses import dataclass, asdict
import pickle as pk
import os
from datetime import datetime

#################### Credentials ####################
chat_id = os.environ.get('CHAT_ID')
token = os.environ.get('TOKEN')

today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

@dataclass
class Discount_item:
    name: str
    promo_price: float
    photo: str
    sku: str
    
# gets all items on wishlist
def get_items():
    url = "https://www.uniqlo.com/sg/api/commerce/v3/en/favorites"

    querystring = {"limit": "20", "offset": "0"}


    headers = {
        "cookie": "oidc.sid=s%3A9GrTHvC5pHQPo434sXycOMdYC-wvvc5A.xma9pa3JHCYhUJjk%2F5QYIeNuls%2FUJpIdXk2jSZlUQ8I; akavpau_www_uniqlo_com_sg_ec_vp=1665032527~id=6162b0b6eb932e3f8c508f6c7158dbaf; ak_bmsc=84BFCB9FD9A74DEB194CEE4BA77A4A3A~000000000000000000000000000000~YAAQBescuLahW8+FAQAAyEPd1hL1T2goEZMdNPqOec1YASi/9la1/yx1nwi0mHEzYL05tn0SDjVZKOmH+UdJEQ8sEwiDuBKyDeKjJu9ecjOv68j6Y12+GfYYz+uOgiRuWrbOpttI9XDQmWOLWy3MyWoTgsmDX5aAk3A4Y11bLD3xE88NIwEUyRMAKK9I6jJkdE646FEV4skYQW1/uMh+BcbIzloeu/qYoP9NhorpEwwLkNiyqezivpkx4jOVmg4s1Vgq17rPfYns7RsJ0ic6RjnNzikxUyMVapZaX40bGR33kgpzL5Vlc5pN8GCboM651cZb6izuys9qWlTgpbW8cvwiI8SuxVRjliMiZY7U8zNSc/66WBMMeT1P5eCehUz274OAXmLqw9UDnYU=; bm_sz=7DD81DF79D208BFC2A3675334F98958E~YAAQBescuLihW8+FAQAAyEPd1hK95/284LGhPfCAUDtytdUNBBsX6KgFkkomJvCYK/HcLVFVD1GATffrR1XN0q44Kea4tc0gEspa3J9P3fNO5zPJVzTduyrwedSppGZyZRIqYUWGkhsJU0x2rLao61SjB7XH0tDt8K9Ve0WNderOb2xMRCnpsaRHZ8H45csXXADqj+3QjFTc8VPLqM8XKmlD1N6tmdc/c4LBv8TtPb0QSPfa1Ud/nEY5Peqq/wvtv2FczUvVew9cihsU6kErKdxgPsJhOJBiwdPQSmhLQrGAJp0=~3487796~4408130; _gcl_au=1.1.755258778.1674347104; sn3t4d1n=A42Dp6uDAQAAlCWut3hE38OIPuZxCpW9yBUUB9K-0iZpDjDr8byFE4IZCFuyAXRY6dKucjv8wH8AAOfvAAAAAA|1|1|672d002fe62d9b7ac68ce87b1bd49b57d65d5450; bm_mi=9CED939DA0017EB856487020F3BC5D94~YAAQLNrIF2TDMc6FAQAAbgTq1hLPIkq7t38TKE2qhehnlHCbouwvolGdrdTwWyYdT9V82XQmLYqFe6WMoxKLmom6cnCnC3wwLimHPWVxNnIAfsm6veiBBD204OhYLRR5jXzCHhOQHkWuV6q9Fbhgy+JTQxapi5fxKX0AFVM0iroqeUrZuGcF8ofckh/8RE4dnjGajtDqOyLqkHSnez99RhrXXt8b9DqkNl8rqM9u7WaGSj8YijxUhR/UaAk5q6V3diPjBt2pNgz5bgSRrtLwZw69qmUj5YuBndY3RW4NRwuxXNT7OwcMv7AcoTd2wJT9PEPrUQ17jCnfIQtS~1; akavpau_www_uniqlo_com_sg_api_commerce_vp_tree2=1674348336~id=42dc951bc76f1f29362fa51c7a550104; BVBRANDID=72295bbc-ed06-4616-bae8-ebd701b17e93; BVBRANDSID=965ea2eb-5f46-464d-befa-8116eaa09895; _abck=B88FF9EB491ED7937CB5C6042DA0020F~-1~YAAQLNrIFwbGMc6FAQAAWT7t1gkBvYavz/W+adyQo7AIFfE2Jdio9U+L9gEkdDXHHovE3wjff12fxUzMfnL5JL+8gFePip03cWbpvUuoOJesyk0l53D8lqV1yyZ1KiCUqj0Ft3xcb6ojsPo91I7OibTEjGjxaX9axoa3zvSccr+6Dm2e2pW/UdHtGtYSICvPy5RdR0ArA7gliMGM9YwW4y9/oQ+n0EhKTzoqHmTrxQU39QPcENygIEOppQZnVXsi1ABS1tnea2cG/hx+vpuAn1A9lKByTW8kytA1dujiAh1EAjZ5tsNvn54QB9xN3cargDqwWKWm9f9XYT5uaX9FQCuifBYcs/PAspHZqJc4VFWzcr26/GF9ssUI9FR/urzGW2yxpGqOTw==~-1~-1~-1; sub=83bfc3aa7ef804ed560b36b140071279; isLoggedIn=true; fr.sid=s%3AIpQnXeycq0nktosrbjbKzq6bhwIPmY8W.tisLxo4ds%2FUdVXuzTTgOJ4j2ia%2FoSquLZ6x4Bsx8rfI; akavpau_www_uniqlo_com_sg_ec_vp_tree2=1674348921~id=91fcf552f040822a1a95071b82b2d3be",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()['result']['items']

# returns discount items
def get_dictionary():
    items = get_items()
    results = []
    
    for i in items:
        name = i['name']
        photo = i['images']['main'][0]['url']
        try:
            promo_price=float(i['prices']['promo']['value'])
        except:
            promo_price=None
        sku = i['productId']
        
        populate = Discount_item(
            name = name,
            photo = photo,
            promo_price = promo_price,
            sku = sku,
        )
        results.append(asdict(populate)   
        )

    return results

# finds all items in dictionary that are on promotion
def on_promotion():
    on_promo =  [i for i in get_dictionary() if i['promo_price'] != None]
    return on_promo

# find sku of items that are on promotion then dumps them in a pk file
def promo_save_sku():
    ''' returns a list of skus once message has been sent '''
    on_promo = on_promotion()
    # sku = [i['sku'] for i in on_promo]
    sku_dict = {
        "sku": [i['sku'] for i in on_promo],
        "date": today
    }
    with open('uniqlo_promo_items.pk', 'wb') as f:
        pk.dump(sku_dict, f)

# checks list of sent skus to make sure we are not sending the message twice
def check_newitems():
    """ checks list of sent skus to make sure we are not sending the message twice 
    returns list of new items on promotion **
    """
    with open('uniqlo_promo_items.pk', 'rb') as f:
        sent_items = pk.load(f)['sku']
    on_promo = on_promotion()
    new_items = [i for i in on_promo if i['sku'] not in sent_items]
    
    return new_items

# sends message to telegram bot
def sendmessage():
    """ sends message to telegram bot """
    
    new_items = check_newitems()
    if new_items != []:
        for i in new_items:
            name = i['name']
            photo = i['photo']
            promo_price = i['promo_price']
            sku = i['sku']
            message = f"New item on promotion! \n\nName: {name} \n\nPrice: {promo_price} \n\nSKU: {sku} \n\nPhoto: {photo}"
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}")
        
        promo_save_sku()
        
    else:
        promo_save_sku()


# runs for the first time
def initialise():
    items = on_promotion()
    if items != []:
        for i in items:
            name = i['name']
            photo = i['photo']
            promo_price = i['promo_price']
            message = f"New item on promotion! \n\nName: {name} \nPrice: ${promo_price} \nPhoto: {photo}"
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}")
        
        promo_save_sku()
    else:
        promo_save_sku()
        

def main():
    try:
        sendmessage()
    except:
        initialise()

if __name__ == "__main__":
    main()