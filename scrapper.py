import csv
from scrapegraphai.graphs import SmartScraperGraph
from model import Company, fields
from config import config


with open("prompt.txt", "r") as f:
    prompt = f.read()
with open("urls.txt", "r") as f:
    urls = [ u.rstrip('\n')  for u in f.readlines() ] 

def scrape_urls(url):
    scrapped_rows = []
    for url in urls:
        smart_scraper_graph = SmartScraperGraph(
            prompt=prompt,
            source=url,
            config=config,
            schema=Company
        )
        result = smart_scraper_graph.run()
        print(result)
        result = {k: ('' if (not(k in result) or result[k] == 'NA') else result[k]) for k in fields}
        scrapped_rows.append(result)
    return scrapped_rows

def write_file(rows, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

all_rows = scrape_urls(urls)

write_file(all_rows, 'companies.csv')