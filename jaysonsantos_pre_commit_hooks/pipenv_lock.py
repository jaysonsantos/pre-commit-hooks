from __future__ import print_function, unicode_literals
import sys

from pipenv.project import Project


def main():
    p = Project()
    return_code = 0
    if p.get_lockfile_hash() != p.calculate_pipfile_hash():
        print("Your pipenv lock is not up to date", file=sys.stderr)
        return_code |= 1

    exit(return_code)


if __name__ == "__main__":
    main()
