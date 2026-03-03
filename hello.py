#!/usr/bin/env python3
# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    """returns the full name"""
    # İsim ve soyisim arasına boşluk koyduk ve kenardaki boşlukları temizledik
    name = f"{first_name.capitalize()} {last_name.capitalize()}".strip()
    return name

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Boşluklara ve ünlem işaretlerine dikkat!
        print(f'Hello {full_name("", "")}!')
    elif len(sys.argv) == 2:
        
        print(f'Hello {full_name(sys.argv[1], "")}!')
    else:
        print(f'Hello {full_name(sys.argv[1], sys.argv[2])}!')