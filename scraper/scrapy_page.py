import requests

from bs4 import BeautifulSoup


def extract_amazon_return_policy(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    policy_sections = soup.find_all('h2')

    policy_data = {}
    for section in policy_sections:
        title = section.get_text()
        content = section.find_next('p').get_text()
        policy_data[title] = content

    return policy_data


if __name__ == "__main__":
    url = 'https://www.amazon.co.uk/gp/help/customer/display.html?nodeId=GKM69DUUYKQWKWX7'
    policy_data = extract_amazon_return_policy(url)
    print(policy_data)
