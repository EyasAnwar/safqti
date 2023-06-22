import requests
import json
import regex as re
import time
from tqdm import tqdm


def extract_pairs(data):
    # Get catalogs
    catalogs = data['data']['catalogs']
    # Combine articles from all catalogs
    articles = list(map(lambda c: c['articles'], catalogs))
    # Combine all article lists to a single list
    articles = [item for sublist in articles for item in sublist]
    # Extract titles from the articles
    titles = list(map(lambda a: a['title'], articles))
    # Extract the pairs from the titles
    pairs = list(map(lambda t: re.findall('([A-Z]+)\/([A-Z]+)', t), titles))
    # Remove empty pairs []
    pairs = [x for x in pairs if len(x) != 0]
    # Combine the pairs in a single string
    pairs = [''.join(item) for sublist in pairs for item in sublist]
    return pairs


binance_announcements_api = f'https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&pageSize=50&pageNo=%d'
file_name = '../../delisted.txt'


unique_pairs = set()
file = open(file_name, 'r')
pre_fetched = set([item.replace('\n', '') for item in file.readlines()])

with open(file_name, 'a') as f:
    for page in tqdm(range(1, 58)):
        x = requests.get(binance_announcements_api % page)
        data = json.loads(x.text)
        pairs = extract_pairs(data)
        unique_pairs = unique_pairs.union(set(pairs))
        [f.write(p+'\n') for p in pairs if p not in pre_fetched]
        f.flush()
        time.sleep(1)
