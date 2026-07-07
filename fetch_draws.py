#!/usr/bin/env python3
"""
Fetch recent 8 weeks lotto draw numbers from dhlottery stats page and write web/draws.json

Note: Requires `requests` and `beautifulsoup4`.
Usage: python fetch_draws.py
"""
import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

OUT = Path(__file__).resolve().parent / 'web' / 'draws.json'
URL = 'https://www.dhlottery.co.kr/lt645/stats'


def parse_from_stats(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Try to find table rows that contain draw info
    rows = soup.select('table.tbl_data tr') or soup.select('table tr')
    draws = []
    for tr in rows:
        balls = tr.select('.ball_645') or tr.select('.num') or tr.select('span')
        nums = []
        for b in balls:
            txt = b.get_text().strip()
            if re.fullmatch(r"\d{1,2}", txt):
                nums.append(int(txt))
        if len(nums) >= 6:
            # take first 6 as main numbers, optional 7th as bonus
            main = nums[:6]
            bonus = nums[6] if len(nums) > 6 else None
            draws.append({'numbers': main, 'bonus': bonus})
        if len(draws) >= 8:
            break

    # Fallback: regex search for repeated runs of 6 numbers
    if len(draws) < 8:
        text = soup.get_text(separator=' ')
        runs = re.findall(r'(?:\b(\d{1,2})\b[\s,.-]*){6,7}', text)
        # The above returns only last capture group in Python; instead find all digits then group
        digits = re.findall(r'\b(\d{1,2})\b', text)
        # group into sliding windows of 6
        grouped = [list(map(int, digits[i:i+6])) for i in range(0, len(digits), 6) if len(digits[i:i+6])==6]
        for g in grouped:
            draws.append({'numbers': g, 'bonus': None})
            if len(draws) >= 8:
                break

    return draws[:8]


def fetch():
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()
    draws = parse_from_stats(resp.text)
    if not draws:
        raise RuntimeError('No draws parsed from page; page structure may have changed')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('w', encoding='utf-8') as f:
        json.dump({'source': URL, 'draws': draws}, f, ensure_ascii=False, indent=2)
    print(f'Wrote {len(draws)} draws to {OUT}')


if __name__ == '__main__':
    fetch()
