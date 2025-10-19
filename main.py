#!/usr/bin/env python3
"""
clean_magnet.py

Reads a magnet link from input, removes all 'tr=' (tracker) parameters,
and prints a cleaned version.
"""

import urllib.parse

def clean_magnet(magnet_link: str) -> str:
    if not magnet_link.startswith("magnet:?"):
        raise ValueError("Not a valid magnet link")

    prefix, query = magnet_link.split("?", 1)
    params = urllib.parse.parse_qsl(query, keep_blank_values=True)
    cleaned_params = [(k, v) for k, v in params if k.lower() != "tr"]
    cleaned_query = urllib.parse.urlencode(cleaned_params)
    return prefix + "?" + cleaned_query if cleaned_query else prefix + "?"

def main():
    magnet = input("Paste magnet link: ").strip()
    if not magnet:
        print("No link provided.")
        return

    try:
        cleaned = clean_magnet(magnet)
        print("\nCleaned magnet link:")
        print(cleaned)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
