from typing import Dict
from typing import List
from typing import Tuple

import json
import requests


def count_params(depth: str, rev: str) -> Dict:
    param_count: Dict = {
        'cube': f'complexity_eci_a_{rev}_{depth}',
        'drilldowns': 'Country,Year',
        'measures': 'ECI',
        'parents': 'true',
        'sparse': 'true'
    }

    return param_count


def depth() -> List[str]:
    return [
        'hs4',
        'hs6'
    ]


def rev() -> List[str]:
    return [
        'hs92',
        'hs96',
        'hs02',
        'hs07'
    ]


def countries() -> List[Tuple]:
    cs: List[Tuple] = []
    url_country: str = 'https://oec.world/olap-proxy/data.jsonrecords'

    for a in depth():
        for b in rev():
            params: Dict = count_params(a, b)
            resp: str = requests.get(url_country, params=params).text
            js_obj: Dict = json.loads(resp)

            for c in js_obj['data']:
                tup: Tuple = (
                    c['Continent ID'],
                    c['Continent'],
                    c['Country'],
                    c['Country ID'],
                    c['Year'],
                    c['ECI']
                )
                cs.append(tup)

    return cs

url_prod: str = 'https://oec.world/olap-proxy/data.jsonrecords'


def prod_params(rev: str) -> Dict:
    param_prod: Dict = {
        'cube': f'complexity_pci_a_{rev}_hs6',
        'drilldowns': 'HS6,PCI+Rank,Year',
        'measures': 'PCI',
        'parents': 'true',
        'sparse': 'true',
    }

    return param_prod


def prods() -> List[Tuple]:
    pd: List[Tuple] = []

    for a in rev():
        params: Dict[str, str] = prod_params(a)
        resp: str = requests.get(url_prod, params=params).text
        js_obj: Dict = json.loads(resp)

        for c in js_obj['data']:
            tup: Tuple = (
                c['Section ID'],
                c['Section'],
                c['HS2 ID'],
                c['HS2'],
                c['HS4 ID'],
                c['HS4'],
                c['HS6 ID'],
                c['HS6'],
                c.get('PCI Rank', None),
                c.get('Year', None),
                c['PCI']
            )

            pd.append(tup)

    return pd
