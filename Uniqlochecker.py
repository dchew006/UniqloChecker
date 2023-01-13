import requests
from dataclasses import dataclass, asdict
import pickle as pk
import os

#################### Credentials ####################
chat_id = os.environ.get('CHAT_ID')
token = os.environ.get('TOKEN')

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
        "cookie": "_abck=4FBE84FBF40819A8BE2DF0679171B21B~-1~YAAQn96bfGChRaSFAQAANGgApgl%2FFMVMq8SPZyA5bLcNmiQdZpEeBnMKzjKzTq866aSYeVTAN2PCBMHrQkyZ5nKA%2BSc9enIlPRgIEmT2DitsFcacs5r5m5NI%2FinB4PMOcwppltnBNf0jbxvYMHdkS2duwqJsLVsJIq3%2FBWXLeOMKRPZx94VVfk4B0DAvCrN9NA0jginR8NURcDtGeNKn92OTEyFrJCKhppV08omFJrJVdIP3kzy48gtht0iNg78fMbRLDZNBijj7%2FF8zQT3iHO4JdSC1BQJ4aWZFPbi3WeH%2BD0Lj854qGcUGRIi06p0TwkPPmlSs1lFtI4T%2FnGp9uuFoQKscuqIH7YpZ%2BnLBGLOiiqR1x5XvBlN42O%2FLjo%2Bvo3hpWVXthfjq0L3qXQMOrNZBIKsWMOjGHQ%3D%3D~0~-1~-1; ak_bmsc=3A2583E9B2E6906114558E89D91CC5DB~000000000000000000000000000000~YAAQn96bfO%2B1RaSFAQAAxAcTphI7Yo4EmL8v%2BOTHMJCFrVCNpO3DdfO%2Bx0h2sQUgYxOjXa4nMk2L%2BBkHwZedVtah5lNxAGWRWH1KsS9r%2BgwW9tB%2BV1oAowf9ehzjIJRP6CUDGEFV3aP2EFY9gVb4gm36xqcJWxoIYZUNQVsSBwCP7VwVYZ4rrk1DMxLJhTnHmz9QWoZ6OaT3WBv%2BwB%2BRqINB1DZHrjnPemMXO%2FXOVsMkP6CmAY%2B%2BxMF%2FHvNfpUuIgOOldjzqWnt%2FW0SUiPMyRQGQ1g9L6In3YyRJQdr0CqF5ctTBipF50MqIf%2FucSv99xjrFcCS6YQ5kwNMfRqD8PMcCNbV%2F5pgExLTRhXmp10PBs7ztOT%2BXQtonx2DqBIC6heLVBU4hU5GlLdPXySUio7KsTgXEzROi%2B7HmxlvpWSncZeo5UWCk%2FarJKbgZ",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": "oidc.sid=s%3APHofvJMKRQnzFGMKERlyjFWA2otE7ZaO.m%2F%2FIcC3LjgNmdyx2IVE1sSl5xbgrqEHjxJwQGu8T54U; akavpau_www_uniqlo_com_sg_ec_vp_tree2=1673528774~id=1dd2cece62fdbb4f22fe4bee6c10ec62; bm_mi=C3D3D3292C182EA0069AE50E8704412E~YAAQn96bfJ60RaSFAQAA4PQRphJ8QAIzDRF/xjiVsNDhDdfEIzRinJOeLbawH87o79xHyCZP7tTWst+0x44IIgJfQ2JIhnAja93lxfcy227t9hcT8hhOIs54mkjc1keHMvMZvIzxeQI/wWuskHrUW6a7VQIPB8Llxcl7GIRVlWq851ddI/n64SsVqBEuVeFeFhVRjSPp4G14iBGOt0mtWh3PVY99Jyl2d8bMFLkQTGRX+LqAlkGB4/JAqNXcDQNpDIJLhpvQriW2HI9naS/HixEmNCT20kBn8fDbFHFrYJqbv97XMQNoSAJvcDrPT97x5JEDUMIAm4d3Vnvq~1; akavpau_www_uniqlo_com_sg_api_commerce_vp_tree2=1673528729~id=b18187c2d97cdaee3382c7603f0fa576; fr.sid=s%3AdGaKpQazNaLE6DpaOVGXl22X6uoqEyFe.SnmmiH11%2FAQiGNtsRvVzsYZDq5nwC%2BPd3U6%2BdAHbqsA; isLoggedIn=true; newsletteroverlayopened=true; sub=83bfc3aa7ef804ed560b36b140071279; _abck=4FBE84FBF40819A8BE2DF0679171B21B~0~YAAQn96bfC6zRaSFAQAASl8Qpglvmy5DKz8Fwun1b28pada298/v3lrOYJZH4xQHnh3l09ZMRGw8ba3vnAjlanDHdaG8/SboOyZoGrD7iInDygEmXcMNc8qVY5/MLMdQNh6JBLT4osQIZphprDgHgxqpQ8M6rzUik2+mFDlPBOP9Feg+W14faEl7v5Jt7XitXNTZveZIEbeSfNSfxPTFiLPb3B6QxTcb32fu14iwC3sU+DTQuLNF1N1MHcvCI/buB+w5d0TfDU3k4c7X44mafiwZ1e3JfLWq89Seu6azHCkmrJDqsVFNqd4nEr1m2BfO/vCKBh78AhNqBncfDQEY9fCdhcZnjEjV994LjA5jJ0ylcTJZMxQd+iht/jfbBCGw+njHHbpYQ5HS4rUqBTbYy3cFKMMdAPPZKQ==~-1~-1~-1; ak_bmsc=3A2583E9B2E6906114558E89D91CC5DB~000000000000000000000000000000~YAAQn96bfNucRaSFAQAAzhv8pRLk0KmvfHLQ2S2BLWk2gVMJebnY3Ef+8rgkU/FiJ9BK6xQuKkesPkfLM6mOTHbmCh/m8txQ67yld3Admx98U6fpSqLKObCklV0Eh86/Jos/d/OCtIPsIjLCcNitGST5w3BxuMWoBf4aQWhIWTvsSNeaYNH9yOl9xbEDVUo4v/BaCpcCitl7RfO9YShoW4wfG/ewiaxZEAxrh6VSN9xzVnzcQye50fJoX2GVWwiigQkbWb7l9byF2yM+b2iZ7tNwe0TtHFSRPd59PB00ut6bTXLnBy1V/AZujSRlpKBjN311WE9+/IbLBj3HcmsX++qGfedu8+88/kJsWxNSWDsDU9pt6ipfnnREALXq1t+L/PnYVftZD3vWQw==; bm_sz=247536ACBF0244BF53322D6D230AE53C~YAAQn96bfNqcRaSFAQAAbRv8pRJ7NP4Zxzg8/JxB5Zs32Wq1ILlJhAYNrl2LRtbF189qGj4l93XqvimPnJTOpLh+O/IRfdBerexF5sMiIQghLBAEuCzF3/tg+3dStn4AwFh9n/1Lr81CowOcye490ucFw2RcJQI8QP/VCRTEybw6ufZrM6xdoDC3kWCkZDbt9HpLD1qjwKxvkYIHcpoeGBHSLE9tCm9af6yJpRojxfnvuM6QZHHm3/gbOCQcdyvyAVzuGO6FTX+P3V1MjLk+Whk7ivqEp8JC3+cGkGSoxES85Ys=~3293745~3485766; sn3t4d1n=A7ZKQP6AAQAAv5oS2nlrwEoGFhkEORcf43YXlcQNOAs_M1yUdw1FvcMWlereAXRY6dL6K_z8NeQAAOfvAAAAAA|1|1|4d8caafefcce5635323a19eff25342319a0d7706",
        "Accept-Encoding": "gzip, deflate, br",
        "Host": "www.uniqlo.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
        "Referer": "https://www.uniqlo.com/sg/en/wishlist",
        "Accept-Language": "en-GB,en;q=0.9",
        "Connection": "keep-alive"
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
    sku = [i['sku'] for i in on_promo]
    with open('uniqlo_promo_items.pk', 'wb') as f:
        pk.dump(sku, f)

# checks list of sent skus to make sure we are not sending the message twice
def check_newitems():
    """ checks list of sent skus to make sure we are not sending the message twice 
    returns list of new items on promotion **
    """
    with open('uniqlo_promo_items.pk', 'rb') as f:
        sent_items = pk.load(f)
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