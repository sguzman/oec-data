import atexit
import requests
from typing import Dict
from typing import List

import oec
import oec.misc
import oec.all


def init_log() -> None:
    print('hi')


def init_atexit() -> None:
    def exit_func() -> None:
        print('bye')

    atexit.register(exit_func)


def init() -> None:
    init_log()


def main() -> None:
    init()

    prod = oec.misc.prods('hs6', 'hs07')
    print(prod)
    print(oec.all.tarrifs(prod))


if __name__ == '__main__':
    main()
