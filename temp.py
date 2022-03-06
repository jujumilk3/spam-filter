import re
import requests

from bs4 import BeautifulSoup


def is_spam(content, spam_domains, depth):
    if 'http' not in content:
        return False
    session = requests.Session()
    print(content, spam_domains, depth)
    found_addresses = re.findall(r'(https?://\S+)', content)
    print(found_addresses)
    for address in found_addresses:
        while depth:
            depth -= 1
            response = session.head(address, allow_redirects=False)
            print(response.content)
            if response.status_code in [301, 302]:
                address = response.headers['Location']
            else:
                bs4_content = BeautifulSoup(requests.get(address).content, 'html.parser')
                found_link = bs4_content.find('a')
                if found_link.has_attr('href'):
                    address = found_link['href']
        print("final address is:", address)
        bs4_content = None
        found_links = None
        for spam_domain in spam_domains:
            if spam_domain in address:
                return True
            else:
                if bs4_content is None:
                    bs4_content = BeautifulSoup(requests.get(address).content, 'html.parser')
                    found_links = bs4_content.find_all('a')
                for found_link in found_links:
                    if found_link.has_attr('href'):
                        found_address = found_link['href']
                        if spam_domain in found_address:
                            return True
                        print(found_address)
    print('----------------------------------------')
    print()
    return False

# spam
assert is_spam('asdw https://goo.gl/88srfV', ['pearsoncmg.com'], 1)
# no spam
assert is_spam('asdw https://goo.gl/88srfV', ['nospam'], 1) == False
# find from html
assert is_spam('asdw https://goo.gl/88srfV', ['accessibility'], 1)
# many addresses at content
assert is_spam('asdw https://goo.gl/88srfV http://bit.ly/silly', ['pearsoncmg.com'], 1)


