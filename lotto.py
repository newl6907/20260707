#!/usr/bin/env python3
"""
Simple Lotto number generator (6/45).
Usage: python lotto.py -n 3
"""

import argparse
import random
import sys

def generate_ticket():
    """Generate a single lotto ticket: 6 unique numbers from 1 to 45."""
    nums = random.sample(range(1, 46), 6)
    nums.sort()
    return nums

def format_ticket(nums):
    return " ".join(f"{n:02d}" for n in nums)

def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(description="Generate Lotto numbers (6/45).")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of tickets to generate")
    parser.add_argument("-s", "--seed", type=int, help="Random seed (optional)")
    args = parser.parse_args(argv)

    if args.seed is not None:
        random.seed(args.seed)

    for i in range(args.count):
        ticket = generate_ticket()
        print(f"Ticket {i+1}: {format_ticket(ticket)}")


if __name__ == "__main__":
    main()
