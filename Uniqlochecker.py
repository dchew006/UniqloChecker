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
        "Cookie": "oidc.sid=s%3A-nBAACZ9H0z4kHQDVmkyKwA46ZvnlTFy.%2F%2BVV6lEaCYZ0DB1AyxIj1Z8RwuiHr3IwN5pa%2FVuZG%2BU; akavpau_www_uniqlo_com_sg_ec_vp_tree2=1674307282~id=04b782a71705a196dd453180102d9f62; bm_mi=FE5EB4A606A0C6389ACACC89EF51C159~YAAQLNrIF0SFL86FAQAAvA551BJKLq70ywXhkKtDBns6WJp+m/oARlhrsKJStATkgnLMIJ79jXym3FCvVCanZbfcX3AjoteXahklkVoBzLVV/J1K6VCgzxzsmZQToJswSAoDBpnpWI3YqoL8/2QDxzyalGHayHBdE4JUjhooT+A4g2HvkztKFsFBX7ba8UlrFam1AYllz8Mqb8OdMjclKOAk/0IpH8b4lYrasFhySocNkShDEOFIEPnCFMp4l5lg6nnx7q14WuryGW7V22a56HvhmnhWnha/+i1FceuaRl6ilutBId0FqzsuovnPcLFSCX1bl+cTEzLLX+EZ~1; akavpau_www_uniqlo_com_sg_api_commerce_vp_tree2=1674307262~id=114529b65ab2cdda7cd7703365ea8d2a; newsletteroverlayopened=true; fr.sid=s%3AeVfufBeeVG46gnUt1c4lXwDELzfOhOj1.UMYUsYAHpp0qV1bgZIfifBXr6qohoK99Ok3icc1S7UU; isLoggedIn=true; sub=83bfc3aa7ef804ed560b36b140071279; _abck=4FBE84FBF40819A8BE2DF0679171B21B~0~YAAQLNrIF8+CL86FAQAAt6521Amen/PLX0tmAD0dDiwYZTVT+bS1RM0zZx3DzaBwNlRQ8h4JL8gSlr77WwRvILt0cuY+NZKLx2jcyJQOtFY1/vUI1if2xDhWQV5bu9xkpd2gzwaHELz2EHZuJcmD1ad2ol3juIUVKwKFLHoh5WgIMmZyMn0u9WaJQV6WJPnlHSJvay/+L4StZuKQz43dvwqftD1YrWztRnVCv9bnITbJiRwDdrcdPAWz87d/+SAaa0H4nmosV5eOebQCm5RAx3wdJjJ5K5YEr+FgYfALy7GuxD1x1n1hihUy3UMJrn1RXmTFgbCep7+vqDIfbxPiqKCIeLab/Tb3DiZJVoA9ci/GFHtt215Y60ArizcRNH+ayJJAWVtDb9QPSDKoFhBl7WHvCqdXreoUIQ==~-1~-1~-1; ak_bmsc=A8438B5A80680CEB1A791A38B8862502~000000000000000000000000000000~YAAQLNrIF8GCL86FAQAAwnt21BI8LcA/RPJqtDb1fEeV9yrSJPsoIqznp+MB/b6vLrHaWEte5gB+LAz5T934AndRySD/azIylrkq3aqPYwkCDbDrpNctZ54UJO6ceJvgGVFfXk2lYEfhcI2/tOe0lzdBrrKQZH49CzLMvrH1MoHjoCjb5EJ5tz5Do3p+oGzlzRxhlER+SUXLAUH3B/1Faa/yOwrjaoznOatOn0+EvpDhprW1sTqdlgnIABwtoN99n7FyCi5+Ag48yurQzlaxTjqclln8VMG8eG26l8t4XvfXu5k94ejTsiAsc+bR5uck4/37oHVqbnK8g4qQh40o3bMlQCIvuiyDIpYjLPHvWBt2YnRsVNvz+zWrtaXnVg8Kr83U7qeJr/zbhg==; bm_sz=7AE1C67FBCC914258668A077ADBEA37D~YAAQLNrIF8CCL86FAQAAGHt21BIqY8th4sNLV6DsnTOUNl7FO26chwzvioXQNuZTcYv5XfQWrTkSlxfjo/keS7Os0ZmvfrjMtRMMyQzqDdKxeguo25jdh8JXjA3SXYht0+okpu8MVGFItClKhkkCseC63wH7OJpX8UDDZa+kM0sqnLscsRFCtsyvAC/oBSb+7n+oYC7BS2a1eWAb3uLPCTQZbAmWI11+F6pkfhW+pmeMn/3Zj6Ix7z2zqXUoZdGHgGZ1bEEhnNfDOiz9Ptdm0Hw6PIJefc1ZlPghSN4H5i3meLE=~4468803~3553094; sn3t4d1n=A7ZKQP6AAQAAv5oS2nlrwEoGFhkEORcf43YXlcQNOAs_M1yUdw1FvcMWlereAXRY6dL6K_z8NeQAAOfvAAAAAA|1|1|4d8caafefcce5635323a19eff25342319a0d7706",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
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