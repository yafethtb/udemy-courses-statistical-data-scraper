import json
from dataclasses import asdict
from udemy_scraper import course_scraper


def etl_process(subcategory: str, country: str, start: int, stop: int): 
    """ETL Process."""
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
        