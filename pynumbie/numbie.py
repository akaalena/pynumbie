import argparse
from random import choice


def random_integer(start, stop, excluded = []):
    return choice(list(set(range(start, stop)) - set(excluded)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='PYNUMBIE'
    )
    parser.add_argument('-s', '--start', required=True, type=int, help='Start of the range')
    parser.add_argument('-e', '--end', required=True, type=int, help='End of the range')
    parser.add_argument('-x', '--excluded', nargs='+', required=False, default=[], type=int, help='Number to exclude')
    args = parser.parse_args()
    
    number = random_integer(args.start, args.end, args.excluded)
    print(f"{number}")