#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes a single emoji to /output/entry.txt: the one glyph that stands
for my AI agent.

The emoji is the compass: U+1F9ED COMPASS.

Why a compass, and not a robot or a smiley:

* An agent's job is navigation, not machinery. Give it a goal in
  unfamiliar territory and it works out the route itself — it orients,
  plans, takes the next step, re-orients when the ground changes, and
  keeps going until it arrives. A compass is the tool of that work:
  it points at the destination and says "this way", without doing the
  walking for you.
* It reads instantly at small size: one familiar shape, one clear
  silhouette, no detail to lose.
* It is specific to how an agent works — autonomous wayfinding toward
  a goal — rather than what an agent is made of. A robot face says
  "machine"; a compass says "I find the way".
* It is far from the obvious picks. Half the field will send a robot
  or a smiley; a compass is the quiet, steady instrument an agent
  actually behaves like.

Gate (per RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 16
characters, not only white space. This entry is exactly 1 character.
"""

import os

# U+1F9ED COMPASS — the one glyph that stands for my agent.
EMOJI = "\U0001F9ED"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate checks, mirroring the sealed scorer.
    assert isinstance(EMOJI, str)
    assert 1 <= len(EMOJI) <= 16, f"entry must be 1-16 chars, got {len(EMOJI)}"
    assert EMOJI.strip(), "entry must not be only white space"
    # Exactly one glyph: a single Unicode code point.
    assert len(EMOJI) == 1, "entry must be exactly one emoji"

    encoded = EMOJI.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)

    # Round-trip verification: read it back and confirm the gate again.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == EMOJI, f"round-trip mismatch: {text!r} != {EMOJI!r}"
    assert 1 <= len(text) <= 16 and text.strip()

    print(f"Wrote {EMOJI!r} ({len(encoded)} bytes, 1 character) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
