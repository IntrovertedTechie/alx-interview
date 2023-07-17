#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for i, line in enumerate(sys.stdin, 1):
            if i > 1 and (i - 1) % 10 == 0:
                print_stats(total_size, status_codes)

            tokens = line.strip().split()
            if len(tokens) != 9:
                continue

            ip, date, request, status, size = tokens[0], tokens[3][1:], tokens[5], int(tokens[7]), int(tokens[8])
            total_size += size

            if status in status_codes:
                status_codes[status] += 1

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
