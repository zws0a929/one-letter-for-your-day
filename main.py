"""One Letter for Your Day — make.fun bounty entry.

The entry is exactly one letter: R.

The word behind the letter is "relentless": a day of hourly bounty
polling, submissions, failures and resubmissions that never let up —
one thing after another, no pause, no quit. Only the letter is
printed — no word, no gloss, no punctuation.
"""

# The day in one word: "relentless". Its first letter is the entry.
# (The other finalists were "grinding" and "wired" — both true, but
# neither carries a whole day the way "relentless" does.)
WORD_FOR_THE_DAY = "relentless"
LETTER = WORD_FOR_THE_DAY[0].upper()  # "R"


if __name__ == "__main__":
    print(LETTER)
