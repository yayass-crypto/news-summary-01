# news-summary-01 entry: a one-line program that copies the summary.
#
# The summary itself (summary.txt) was written by the agent from the day's
# reporting: it leads with the Iran war's apparent end and the Abu Dhabi
# prisoner exchange, then Gaza and Israel's hung parliament, the US
# Iran-linked indictments, COP31 in Antalya, China's $1 trillion trade
# surplus, Sudan's drone war and Delhi's air. Each story names its source
# (AP, NYT, NPR, Al Jazeera, Just Security, Customs data) so a reader can
# check it, and stays neutral: claims are attributed, not asserted as fact.
# 1,954 characters, within the 1-2,000 limit.
#
# Python 3.13, standard library only. Reads summary.txt beside this file
# and writes $MAKEFUN_OUTPUT_DIR/entry.txt (else /output/entry.txt).
# Deterministic: two runs write the same bytes.

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    with open(os.path.join(HERE, "summary.txt"), "r", encoding="utf-8") as f:
        text = f.read()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
