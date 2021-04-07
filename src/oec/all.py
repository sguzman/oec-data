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


def prod_params(rev_str: str) -> Dict:
    param_prod: Dict = {
        'cube': f'complexity_pci_a_{rev_str}_hs6',
        'drilldowns': 'HS6,PCI+Rank,Year',
        'measures': 'PCI',
        'parents': 'true',
        'sparse': 'true',
    }

    return param_prod


def prods() -> List[Tuple]:
    pd: List[Tuple] = []
    url: str = 'https://oec.world/olap-proxy/data.jsonrecords'

    for a in rev():
        params: Dict[str, str] = prod_params(a)
        resp: str = requests.get(url, params=params).text
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


def tarr_params(hs6_str: str) -> Dict:
    param_tarr: Dict = {
        'HS6':  hs6_str,
        'cube': 'tariffs_i_wits_a_hs_new',
        'drilldowns': 'Year,HS6,Partner+Country,Reporter+Country,Agreement',
        'measures': 'Tariff',
        'parents': 'true',
        'sparse': 'true',
    }

    return param_tarr


def tarrifs(hs6s: List[str]) -> List[Tuple]:
    hs: List[Tuple] = []
    url: str = 'https://oec.world/olap-proxy/data'

    for a in hs6s:
        print('Getting', a)

        params: Dict = tarr_params(a)
        resp: str = requests.get(url, params=params).text
        js_obj: Dict = json.loads(resp)

        for c in js_obj['data']:
            tup: Tuple = (
                c['Year'],
                c['Section ID'],
                c['Section'],
                c['HS2 ID'],
                c['HS2'],
                c['HS4 ID'],
                c['HS4'],
                c['HS6 ID'],
                c['HS6'],
                c.get('Partner Continent ID'),
                c.get('Partner Continent'),
                c.get('Partner Country ID'),
                c.get('Partner Country'),
                c.get('Reporter Continent ID'),
                c.get('Reporter Continent'),
                c.get('Reporter Country ID'),
                c.get('Reporter Country'),
                c.get('Agreement ID'),
                c.get('Agreement'),
                c['Tariff'],
            )

            hs.append(tup)

    return hs