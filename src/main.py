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
    print(oec.misc.depth())
    print(oec.misc.rev())
    print(oec.misc.countries())
    print(oec.misc.prods('hs6', 'hs07'))
    print(oec.all.countries())
    print(oec.all.prods())


if __name__ == '__main__':
    main()
