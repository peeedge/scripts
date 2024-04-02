import requests
import time

def ping_urls(url_list):
    for url in url_list:
        try:
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()
            response_time = end_time - start_time

            print(f"URL: {url}, Response Time: {response_time} seconds")
        except requests.RequestException as e:
            print(f"URL: {url}, Error: {e}")

# Example usage:
urls_to_ping = ["https://www.example.com", "https://www.google.com", "https://www.github.com"]

 # urls_to_ping = ["https://docs.google.com/document/d/18kyRYhbUqFB6ughISiavD6lKJbGy0lwnpvr8iZAL908/edit",
 # "https://docs.google.com/spreadsheets/d/1MAljm_ax13Azsbf29lfYsTw5t4BDhQn9NJXc6B8EAXI/edit#gid=0",
 # "https://www.justwatch.com/us",
 # "http://www.fandango.com/fairfaxcorner14+xtreme_aarcj/theaterpage",
 # "https://www.regmovies.com/theaters/regal-fairfax-towne-center-10/C00793898916",
 # "https://www.angelikafilmcenter.com/mosaic/showtimes-and-tickets/now-playing",
 # "https://www.showplaceicon.com/Browsing/Cinemas/Compare?Cinemas=8877&Date=2022-07-05",
 # "https://purchase.tickets.com/buy/TicketPurchase?orgid=51529&event_val=22HAZY_TGMAV&schedule=list",
 # "http://www.imdb.com/",
 # "https://drafthouse.com/northern-virginia/theater/one-loudoun"]

urls_to_ping = [ "https://www.google.com", "http://www.cnn.com"]

ping_urls(urls_to_ping)



