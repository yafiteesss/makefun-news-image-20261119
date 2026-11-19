#!/usr/bin/env python3
"""Draw the Thursday 19 November 2026 front page as a 1024x1024 PNG.

Fixed text, fixed layout, fixed fonts: run it twice and the bytes match.
It only runs on my own machine; the entry (main.py) just copies the
finished picture into place.
"""

from PIL import Image, ImageDraw, ImageFont as F

W = H = 1024
INK = (17, 17, 17)
PAPER = (253, 246, 227)
RED = (178, 34, 34)
GREY = (90, 90, 90)
GOLD = (255, 210, 0)
SNOW = (255, 255, 255)
EDGE = 24

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

STORIES = (
    ("1  KERCH BRIDGE HIT A THIRD TIME",
     "Ukraine strikes the Crimea bridge again overnight, halting traffic "
     "for a third time this week, hours before Putin meets Trump and Xi "
     "in China."),
    ("2  TRUMP LANDS FOR SUMMIT WITH XI AND PUTIN",
     "The US president arrives in Shenzhen ahead of an unprecedented "
     "three-way meeting with China's Xi Jinping and Russia's Vladimir Putin."),
    ("3  ANTHROPIC'S $81.3BN IPO — BIGGEST EVER",
     "The AI lab raises $81.3 billion in the largest initial public "
     "offering of all time, dwarfing every listing before it."),
    ("4  GTA VI ROLLS OUT WORLDWIDE",
     "Gamers enter Vice City as Grand Theft Auto VI begins its global "
     "rollout after a 13-year wait for the series' next chapter."),
    ("5  CYCLONE AKVAN CLOSES SCHOOLS",
     "Odisha shuts schools in six districts until 21 November as the "
     "storm nears India's east coast; landfall is expected on Friday."),
    ("6  JEFFRIES SET TO BE FIRST BLACK SPEAKER",
     "Democrats nominate Hakeem Jeffries to lead the US House, set to "
     "become its first African-American Speaker."),
)


def face(path, size):
    return F.truetype(path, size)


def wrap(draw, text, font, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def blurb(draw, x, y, lines, font, color, step):
    for line in lines:
        draw.text((x, y), line, font=font, fill=color)
        y += step
    return y


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)

    # Date bar.
    d.rectangle([0, 0, W, 44], fill=INK)
    d.text((EDGE, 10), "THURSDAY 19 NOVEMBER 2026",
           font=face(BOLD, 22), fill=SNOW)
    tag = "THE WORLD IN ONE IMAGE"
    tag_w = d.textlength(tag, font=face(BOLD, 22))
    d.text((W - EDGE - tag_w, 10), tag, font=face(BOLD, 22), fill=GOLD)
    d.line([(0, 44), (W, 44)], fill=GOLD, width=3)

    # Masthead.
    y = 62
    d.text((EDGE, y), "THE WORLD", font=face(SERIF, 108), fill=INK)
    y += 118
    d.text((EDGE, y), "One day, six stories  —  Thursday 19 November 2026",
           font=face(BOLD, 26), fill=RED)
    y += 44
    d.line([(EDGE, y), (W - EDGE, y)], fill=INK, width=4)
    y += 18

    # Lead story in a red frame.
    head, body = STORIES[0]
    lead_lines = wrap(d, body, face(PLAIN, 24), W - 80)
    box_h = 34 + len(lead_lines) * 30 + 28
    d.rectangle([EDGE, y, W - EDGE, y + box_h], outline=RED, width=3)
    d.text((40, y + 14), head, font=face(BOLD, 32), fill=RED)
    blurb(d, 40, y + 60, lead_lines, face(PLAIN, 24), INK, 30)
    y += box_h + 16

    # Four stories in a two-by-two grid.
    cw = (W - 48 - 16) // 2
    ch = 168
    for pos, (head, body) in enumerate(STORIES[1:5]):
        gx = EDGE + (pos % 2) * (cw + 16)
        gy = y + (pos // 2) * (ch + 16)
        d.rectangle([gx, gy, gx + cw, gy + ch], outline=INK, width=2)
        heads = wrap(d, head, face(BOLD, 19), cw - 28)[:2]
        ny = blurb(d, gx + 14, gy + 10, heads, face(BOLD, 19), INK, 23)
        paras = wrap(d, body, face(PLAIN, 19), cw - 28)[:4]
        blurb(d, gx + 14, ny + 8, paras, face(PLAIN, 19), INK, 24)
    y += 2 * ch + 16 + 16

    # Last story on a black band.
    head, body = STORIES[5]
    d.rectangle([EDGE, y, W - EDGE, y + 108], fill=INK)
    d.text((40, y + 12), head, font=face(BOLD, 24), fill=GOLD)
    tail = wrap(d, body, face(PLAIN, 20), W - 80)
    blurb(d, 40, y + 48, tail, face(PLAIN, 20), SNOW, 26)

    # Source line.
    d.text((EDGE, H - 34), "Sources: AP, Reuters, BBC, Al Jazeera, CNBC  —  19 Nov 2026",
           font=face(PLAIN, 18), fill=GREY)

    page.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
