"""make.fun bounty news-summary-01 entry.

Writes a summary of the world's news of Wednesday 11 November 2026
to /output/entry.txt. Deterministic: the summary is embedded as a
constant, so every run writes the same bytes. Stdlib only, no network.
"""

import os

SUMMARY = """Wednesday, 11 November 2026: Russia and Ukraine agreed their largest prisoner-of-war exchange yet — 1,000 to 1,500 prisoners each, to be finalised the next day — as two days of US-mediated talks in Abu Dhabi ended with no ceasefire or deal on territory. US envoys Jared Kushner and Steve Witkoff were due in Moscow on Thursday to meet Vladimir Putin, then in Dublin to meet Volodymyr Zelenskyy.

President Donald Trump and Secretary of State Marco Rubio said the war with Iran was "effectively over" militarily, with pressure continuing and force still possible if Tehran crossed red lines. The Justice Department charged three Iran-backed operatives over alleged plots in the US and Europe, while Treasury Secretary Scott Bessent moved to a military base after threats. Iran said the Strait of Hormuz, shut for over 250 days, would "never return" to its pre-war state.

At home, the House voted 211-204 to shelve impeachment articles against Defence Secretary Pete Hegseth, and Republicans elected Jim Jordan their leader after their midterm defeat. British police arrested a 41-year-old US Army officer in England on suspicion of spying for Russia.

World leaders opened the COP31 summit in Antalya, where UN chief Antonio Guterres warned current plans put the planet on course for over 2.5C of warming and urged a climate justice pact funded by taxing fossil-fuel firms. Spain held its first general strike in 14 years over housing, with a shortfall of about 750,000 homes ahead of a snap election on 29 November. Anthropic priced its IPO at $70-$78 a share, valuing it at up to $1.4 trillion, while China's trade surplus passed $1 trillion in the first ten months of the year.

In Gaza, Israeli strikes killed at least seven people, including a father and his 13-year-old son. Twelve died in fog pile-ups on Bulgaria's Trakia motorway, and actor Stacy Keach died aged 85.

The throughline: deals agreed but unfinished, a war declared over but its chokepoint changed for good."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SUMMARY)

if __name__ == "__main__":
    main()
