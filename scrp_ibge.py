import requests
from bs4 import BeautifulSoup
import pandas as pd


def scraping_uf(uf: str):
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'
    browsers = {'user agent': "Mozilla/5.0 (WINDOWS NT 10.0; Win64; x64) AppleWebKit/537.36"}

    page = requests.get(uf_url, headers=browsers)
    soup = BeautifulSoup(page.content, 'html.parser')
    indicators = soup.select('.indicador')

    uf_dict = {
        data.select('.ind-label')[0].text: data.select('.ind-value')[0].text
        for data in indicators
    }

    return uf_dict


state = scraping_uf('rj')

for indicator in state:
    if ']' in state[indicator]:
        state[indicator] = state[indicator].split(']')[0][:-8]
    else:
        state[indicator] = state[indicator]

df = pd.DataFrame(state.values(), index=state.keys())
print(df)
