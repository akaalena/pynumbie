import argparse
from random import choice


excluded = []
def random_integer(start, stop, excluded):
    return choice(list(set(range(start, stop) - set(excluded))))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='PYNUMBIE'
    )
    parser.add_argument('--s', required=True, type=int, help='Start of the range')
    parser.add_argument('--e', required=True, type=int, help='End of the range')
    parser.add_argument('--x', required=False, type=int, help='Number to exclude')
    args = parser.parse_args()
    excluded.append(args.x)
    
    number = random_integer(args.s, args.e, excluded)
    print(f"{number}")