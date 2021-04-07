from typing import Dict
from typing import List

import json
import requests


def depth() -> List[str]:
    return [
        'hs2',
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


url_country: str = 'https://oec.world/olap-proxy/data.jsonrecords'
param_country: Dict[str, str] = {
    'cube': 'complexity_eci_a_hs96_hs6',
    'Year': 2019,
    'drilldowns': 'Country',
    'measures': 'ECI',
    'parents': 'true',
    'sparse': 'false'
}


def countries() -> List[str]:
    resp: str = requests.get(url_country, params=param_country).text
    js_obj: Dict = json.loads(resp)

    cs: List[str] = []
    for c in js_obj['data']:
        obj: str = c['Country ID']
        cs.append(obj)

    return cs


url_prod: str = 'https://oec.world/olap-proxy/data.jsonrecords'


def prod_params(depth: str, rev: str) -> Dict[str, str]:
    param_prod: Dict[str, str] = {
        'cube': f'complexity_pci_a_{rev}_{depth}',
        'Year': 2019,
        'drilldowns': depth.upper(),
        'measures': 'PCI',
        'parents': 'true',
        'sparse': 'false',
    }

    return param_prod


def prods(depth: str, rev: str) -> List[str]:
    params: Dict[str, str] = prod_params(depth, rev)
    resp: str = requests.get(url_prod, params=params).text
    js_obj: Dict = json.loads(resp)

    pd: List[str] = []
    for c in js_obj['data']:
        obj: str = c[f'{depth.upper()} ID']
        pd.append(obj)

    return pd