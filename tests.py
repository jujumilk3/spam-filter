import re
import requests

from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


def is_spam(content, spam_domains, depth):
    if 'http' not in content:
        return False
    session = requests.Session()
    found_addresses = re.findall(r'(https?://\S+)', content)
    for address in found_addresses:
        while depth:
            depth -= 1
            response = session.head(address, allow_redirects=False)
            if response.status_code in [301, 302]:
                address = response.headers['Location']
            else:
                bs4_content = BeautifulSoup(requests.get(address).content, 'html.parser')
                found_link = bs4_content.find('a')
                if found_link.has_attr('href'):
                    address = found_link['href']
        bs4_content = None
        found_links = None
        for spam_domain in spam_domains:
            if spam_domain in address:
                return True
            else:
                if bs4_content is None:
                    try:
                        get_response = requests.get(address)
                    except ConnectionError:
                        continue
                    bs4_content = BeautifulSoup(get_response.content, 'html.parser')
                    found_links = bs4_content.find_all('a')
                for found_link in found_links:
                    if found_link.has_attr('href'):
                        found_address = found_link['href']
                        if spam_domain in found_address:
                            return True
    return False
