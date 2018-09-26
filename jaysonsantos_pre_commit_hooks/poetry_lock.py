from __future__ import print_function, unicode_literals
import sys

from poetry.poetry import Poetry


def main():
    locker = Poetry.create(".").locker
    return_code = 0
    if not locker.is_locked():
        print("Your poetry is not locked", file=sys.stderr)
        return_code |= 1

    if not locker.is_fresh():
        print("Your poetry lock is not up to date", file=sys.stderr)
        return_code |= 1

    exit(return_code)


if __name__ == "__main__":
    main()
