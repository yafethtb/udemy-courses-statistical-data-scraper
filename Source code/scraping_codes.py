import json
from dataclasses import asdict
from udemy_scraper import course_scraper


def etl_process(subcategory: str, country: str, start: int, stop: int): 
    """ETL Process.
    
    Parameters:
    ---
    - Subcategory: a subcategory from udemy course. Check the list from udemy.com.
    - country: an ISO 3166-1 alpha-2 code of target country. The price and currency data will based on the target country.
    - start: the first page to be scraped.
    - stop: the last page to be scraped.
    """
    print(">>>ETL Process start.")
    data = course_scraper(sub = subcategory, country = country, start = start, stop = stop)
    dict_data = dict()

    for num, datum in enumerate(data):
        dict_data.update({num: asdict(datum)})

    combination = {
        'subcategory': subcategory,
        'amount': len(data),
        'data': dict_data
    }

    with open(f'{subcategory} {country} page {start} to {stop} data.json', 'w', encoding = 'utf-8') as f:
        json.dump(combination, f, indent = 4, ensure_ascii = False)
    
    print(">>> ETL process completed.")
        
