import atexit
import requests
from typing import Dict
from typing import List

import oec
import oec.misc


def init_log() -> None:
    print('hi')


def init_atexit() -> None:
    def exit_func() -> None:
        print('bye')

    atexit.register(exit_func)


def init() -> None:
    init_log()


depth: List[str] = ['hs4', 'hs6']
rev: List[str] = [
    'hs92',
    'hs96',
    'hs02',
    'hs07'
]


def main() -> None:
    init()
    print(oec.misc.countries())
    print(oec.misc.prods('hs6', 'hs07'))    


if __name__ == '__main__':
    main()
