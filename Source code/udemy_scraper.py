from dataconstant import UdemyCourseData, SUBCATEGORY
import requests
from time import sleep
from random import uniform

HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US',                
            'Referer': 'https://www.udemy.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Udemy-Cache-Version': '1',
            'X-Udemy-Cache-Language': 'en',
            'X-Udemy-Cache-Device': 'None',
            'X-Udemy-Cache-Logged-In': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

PARAMS = {
            'page_size': '16',
            'subcategory': '',
            'instructional_level': '',
            'lang': '',
            'price': '',
            'duration': '',
            'closed_captions': '',
            'subs_filter_type': '',            
            'source_page': 'subcategory_page',
            'locale': 'en_US',
            'navigation_locale': 'en_US',
            'skip_price': 'true',
            'sos': 'ps',
            'fl': 'scat',
        }


def course_scraper(sub: str, country:str, start:int = 1, stop:int = 625): 
    """Scraping data from Udemy.com"""
    ids = SUBCATEGORY[sub]
    scraped_data = []
    # Accessing Udemy
    with requests.Session() as s:
        headers = HEADERS
        params = PARAMS
        headers['X-Udemy-Cache-Marketplace-Country'] = country
        headers['X-Udemy-Cache-Price-Country'] = country
        params['subcategory_id'] = str(ids)
        
        for page in range(start, stop + 1):
            print(f"---> Accessing page {page} ...")
            params['p'] = f'{page}'
            # Sleep
            pause = uniform(3.5, 4.5)
            print(f'Sleep for {pause} seconds.')
            sleep(pause)
            # Session connection
            req = s.get(
                headers = headers, 
                params = params, 
                url = 'https://www.udemy.com/api-2.0/discovery-units/all_courses/')
            data = req.json()
            items = data['unit']['items']
            # Check and transform data
            print(">> ... Data Aqcuired ....")
            if len(items) > 0:
                print(">> ... Start transforming data ....")
                from_generator = [*data_catcher(header = headers , data = items)]                
                print(">> ... Appending ....")
                scraped_data.extend(from_generator)    
            else:
                print("--> No more page exist.")
                break
    return scraped_data

def data_catcher(header: dict, data: list):
    """Transform data taken from Udemy"""
    for num, datum in enumerate(data, start = 1):
        print(f"  > Transform element {num}.")
        id = datum['id']
        title = datum['title']
        url = 'https//www.udemy.com' + datum['url']
        rating = datum['rating']
        reviews = datum['num_reviews']
        students = datum['num_subscribers']
        tot_lecture = datum['num_published_lectures']
        tot_time = datum['content_info_short']
        pub_time =  datum['published_time']
        last_update =  datum['last_update_date']
        lv = datum['instructional_level_simple']
        cat = datum['context_info']['category']
        category = cat['title'] if cat else 'No Category'
        lab = datum['context_info']['label']
        label = lab['title'] if lab else 'No Label'
        price, currency_symbol = price_tracker(ids = id, header = header)
        yield UdemyCourseData(id, title, url, price, currency_symbol,rating, reviews, students, tot_lecture, tot_time, pub_time, last_update, lv, category, label)
        
def price_tracker(ids, header):
    """Tracking real price of a Udemy course"""
    with requests.Session() as s:
        url = f'https://www.udemy.com/api-2.0/pricing/?course_ids={ids}&fields[pricing_result]=price,discount_price,list_price,price_detail,price_serve_tracking_id'
        price_response = s.get(url = url, headers = header)
        price_data = price_response.json()
        price: float = price_data['courses'][f'{ids}']['price']['amount']
        currency_symbol: str = price_data['courses'][f'{ids}']['price']['currency_symbol']
        yield price
        yield currency_symbol

