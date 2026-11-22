# Electric Dev mood board review

2026-11-21

The design holds up well. My pick is **Pacific Current**, with two pieces borrowed from Live Wire.

## Checked and true

- I recomputed every contrast ratio, and they all match the board within rounding. Every text pair passes AA. The one nuance is Pacific's accent, which is 5.8:1 on white but 5.5:1 on the page background. That still passes.
- The font facts are right. Plex was drawn for IBM, Atkinson Hyperlegible comes from the Braille Institute, and all eight fonts are OFL and self-hosted.

## Assumptions that don't hold up

- **Stripe as the serif-and-sans reference.** As far as I know, Stripe's site is set almost entirely in a sans. Swap in a reference that actually pairs a serif headline with a sans body.
- **"Dark tells the AI story faster."** The fix log tells the AI story, and it's identical in all three directions. Dark versus light is mostly about mood, not message.
- **Live Wire "suits IT directors."** All three of its references are tools sold to software engineers. An IT director at a 300-person company buys from vendors that look more like Pacific.
- **Atkinson "helps with the accessibility statement."** A font doesn't change WCAG conformance. It's a nice choice, but not a compliance asset.
- **The plan asked for screenshots of the reference sites.** The board has links only.

## Suggested improvements

- **Warm Circuit:** the secondary button's border is 2.75:1 on the kraft panel, which falls short of the 3:1 non-text minimum. Darken `--line` a step.
- **Pacific:** its own honest risk is looking like every other navy-and-teal IT vendor. Give Beacon amber a bigger role, for status, highlights and the "Most popular" badge, so it has a signature color.
- **The fix log:** make it a signature element whichever direction you pick, and adopt Live Wire's "mono means the machine is talking" rule.
- **Font weights:** the style guide allows two, but the board uses 400, 500, 600 and 700. Settle on two before step 2.

## Why Pacific Current

For 100 to 1,000 employee companies, the buyer is weighing risk, and Pacific looks accountable and grown up. Warm Circuit's own note says it may read as too small-business, and I agree. Live Wire looks like a developer tool. Pacific's colors plus Live Wire's fix log and mono rule would give you both trust and a clear AI story.

## Sources

- `design/mood-board/index.html`, with contrast ratios recomputed from its CSS color values using the WCAG 2 formula.
