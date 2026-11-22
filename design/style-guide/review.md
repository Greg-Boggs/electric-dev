# Style guide review: Pacific Current

2026-11-21

I opened `index.html` in a browser at 1440px and 375px wide, measured the parts that looked off, and read `tokens.css` and `site.css` line by line. Screenshots are in `review-shots/`.

> **Update, 2026-11-22:** I've applied most of the fixes below. See [Fixes applied](#fixes-applied) at the end. The screenshots in `review-shots/` show the page before those fixes.

The short version: the system is well thought out, and the page looks calm, credible and on-brief. One reset bug is making every padded box larger than the CSS says, and the plan cards, footer and mobile header have visible flaws. Amber also reads as brown in most of the places it appears, which weakens the signature the direction depends on.

## What works

- **The overall tone fits the buyer.** Navy, white and teal with lots of room looks like a vendor that will still be around in five years. The hero (`review-shots/hero.jpg`) is the best part of the page: Source Serif at display size gives it authority, and the faint tide rings add texture without decoration for its own sake.
- **The fix log is a strong signature.** Dark, mono, an ordered list, the amber "approval" step and the green "fixed" step tell the AI story in six lines. The rule that logs must be real, anonymized tickets is the right one to write down now.
- **The rules are clear and enforceable.** Two weights with `font-synthesis-weight: none`, "mono means the machine is talking", one amber highlight per screen, approved contrast pairs with ratios. A builder can follow these without asking.
- **The token tiers are clean.** Palette, then semantic, then a few component tokens (`--btn-*`, `--callout-*`) is the right size of system for a marketing site.
- **The accessibility basics are there.** 44px targets, real button borders for forced colors, `:user-invalid` so errors wait until the reader leaves a field, status that pairs a dot with words, and reduced motion zeroing every duration.
- **The voice section is the most useful part for the build.** "Say who does what" and the tone-by-place table will do more for the site than any color choice.

## Bugs to fix before the build copies these files

### 1. The box-sizing reset doesn't work, so everything is too big

`site.css` line 11 sets `box-sizing: border-box` on `:where(html)`, then line 12 sets `box-sizing: inherit` on `:where(*, ...)`. Both selectors have zero specificity and `*` also matches `html`, so the second rule wins and `html` inherits the initial value, `content-box`. Every element on the page is `content-box`. I confirmed this in the browser with `getComputedStyle`.

What that does on the page:

- Buttons are 72px tall, not the 44 to 49px the CSS intends. The small header button is 56px. That's why the buttons look chunky in `review-shots/buttons-and-status.jpg`.
- Form fields are 474px wide inside a 448px field, so they push past their container. On a phone they touch the demo box's edge (`review-shots/mobile-form.jpg`).
- `.wrap` is 1264px wide, not the 1200px `--page-max`, because the gutter padding is added on top.

Fix: give `html` real specificity inside the reset layer, for example `html { box-sizing: border-box; }` in place of `:where(html)`. Then look at the buttons again, because the whole page will tighten up, and some spacing choices may have been tuned against the oversized boxes.

### 2. Plan prices don't line up

The featured plan's badge pushes its title and price 39px lower than its neighbors (`review-shots/plan-cards.jpg`). On a pricing page, the three prices are what the buyer compares, so they should sit on one line. Use `grid-template-rows: subgrid` on the plans so badge, title, price, note, list and button each share a row across cards, and give the non-featured plans an empty badge row. The modern-web-guidance card guide recommends exactly this for cards in a row whose regions should line up.

### 3. Anchor links land under the sticky header

The 81px header covers the heading you jumped to. Clicking "Cards" puts the "Cards" heading behind the header (`review-shots/anchor-under-header.jpg`). Add `scroll-padding-block-start` on `html` set to the header's height plus a little room. After the box-sizing fix the header is shorter, so set this after that fix.

### 4. The footer divider stops halfway across

`.legal` is a `<p>`, and every `p` gets `max-inline-size: 66ch`, so its top border ends at 554px of a 1200px footer (`review-shots/footer.jpg`). Put the border on a wrapper, or set `max-inline-size: none` on `.legal`.

### 5. The email error is announced before there is an error

The email input's `aria-describedby` points to the error text from page load. Hiding it with `display: none` doesn't stop a screen reader from reading it, because `aria-describedby` reads hidden content. A screen reader user hears "Enter an email address like name@company.com" on an empty, untouched field, and `aria-invalid` is never set. The modern-web-guidance guide on accessible error announcement covers this. It starts every field at `aria-invalid="false"`, adds the error to `aria-describedby` only while `:user-invalid` matches, and uses a few lines of script to keep the two in sync. That breaks the "no JavaScript needed" note in the build section, so either accept a small form script or drop the error id from `aria-describedby`.

### 6. Smaller code issues

- `text-size-adjust: none` (line 10) can block text resizing in some mobile browsers. Use `100%`, which stops automatic text inflation without blocking the reader's own setting.
- `.card` sets `container-type: inline-size`, but no `@container` rule targets card children. The guide claims "cards adapt to their own width", and right now they don't. Either add a rule or drop the claim and the property.
- The forced-colors block sets `border: 1px solid CanvasText` on `.callout`, which wipes out the 4px left bar, the callout's only shape cue in high contrast mode. Set the other three sides only.
- `aria-current="page"` is fixed on "Color" in the nav. On this page it's always wrong, since the guide is one page. For the real site it's right. For the guide, drop it or move it as the reader scrolls.
- `#E6EAF0` (on-inverse text) and `#4A6684` (inverse border) are raw values in the semantic tier, and `index.html` repeats `#E6EAF0` inline. Give them palette names like everything else.
- The header's `backdrop-filter: blur(8px)` sits behind a 92% opaque background, so the blur is almost invisible. It costs paint time on scroll for an effect nobody will see. Either drop the blur or lower the opacity enough that it shows.

## Design weaknesses

### Amber mostly shows up as brown

The mood board review asked for amber to become the signature. In this guide, the true amber (`--beacon`) appears in four places: the badge, the featured plan, the nav underline and the `mark` underline. Everywhere else it's `--beacon-ink` (#8A5300): every kicker, the "working" status dot and text. At 14px, #8A5300 reads as brown, not amber. The kickers are the most frequent "amber" on the page, so the page's impression of amber is mostly brown.

Suggestions:

- Make kickers navy or slate, not beacon-ink. They're labels, not signals, and the "If everything is amber, nothing is" rule argues against them anyway.
- For the "working" status dot, use a `--beacon` fill with a 1px `--beacon-ink` ring. That way the dot reads as amber and still meets 3:1 against the page. Right now the brown "working" dot and the red "error" dot are hard to tell apart at 10px (`review-shots/buttons-and-status.jpg`).
- Keep `--beacon-ink` for the rare case where amber text truly carries meaning.

### The fix log is the smallest thing on the page

The signature element is set at 14px mono, with a wide empty right column at desktop width. Compared with the 76px hero right above it on a real home page, it will look like a footnote. Set it at `--text-base` on wide containers, keep 14px only under the 30rem container breakpoint, and cap its width (around 48rem) so it reads as an object instead of a strip. Consider giving the approval line a faint amber wash across the full row, not only an amber label, since "a person stepped in" is the point the reader most needs to see.

### The mobile header is three rows and 190px tall

At 375px the brand, five links on two lines, and the button on its own row take up almost a quarter of the screen (`review-shots/mobile-header.jpg`). The guide defers this to the wireframes step, but the header is a component, and the style guide is where it should be settled. The modern-web-guidance navbar guide's pattern fits: one `<nav>` with a "Menu" button that opens the links as a native popover on narrow screens, and inline links when they fit. Popover is Baseline newly available (January 2025), and the guide's fallback is to show the links inline.

### Cards don't look clickable

The three service cards are links, but at rest nothing says so: no underline, arrow or color on the heading. Only hover changes the shadow, and touch devices have no hover. Add a visible cue, for example a teal heading color or a small arrow after the heading text.

### Smaller visual points

- The disabled "Sending…" button at 55% opacity looks like a lighter teal variant rather than a disabled one. A muted fill (sand background, slate text) reads more clearly as unavailable.
- The radius and shadow tiles leave the last tile alone on its own row at desktop width. A guide page issue only, but it makes the system look unfinished. Use six fixed columns or split radius and shadow into two rows of three.
- The plan `.note` ("For teams with an IT person who wants backup") is 14px muted text right under the price. It's who the plan is for, which is decision-making copy. Set it at base size.

## What's missing for this audience

For a site that sells to 10 to 1,000 employee companies at published prices, these components will be needed soon and have no style yet:

- **Plan comparison table.** The footer links to "Compare plans", and the buyer with 300 employees will want feature-by-feature rows. The table styles in the guide's own `<style>` block are a good start and belong in `site.css`.
- **FAQ or disclosure.** Pricing and security pages need one. A native `<details>` style would cover it.
- **Proof.** A client quote, logo strip or stat tile. The "named engineer" promise needs a face or a name somewhere, and the guide has no style for a person.
- **Icons.** None are defined. Decide on a set and stroke weight before the wireframes, or say plainly that the site uses none.
- **An inverse band.** The footer is the only deep water section. A dark call-to-action or a band around the fix log would give long pages a midpoint.
- **The wordmark.** "Electric Dev" in Source Serif semibold works as a placeholder. Note it as one, so nobody ships it as the logo by default.

## Suggested order

1. Fix the box-sizing reset, then look at the page again before changing anything else.
2. Align the plan cards with subgrid, add scroll padding, and fix the footer divider.
3. Decide the amber question (kickers and the status dot).
4. Settle the mobile header and the form error script.
5. Add the comparison table, FAQ and proof components.

## Fixes applied

2026-11-22. I checked each one in the browser at 1440px and 375px wide.

### Fixed

- **Box-sizing reset.** `html` now has real specificity, so the whole page is `border-box`. Buttons went from 72px to 49px tall, the small button from 56px to 38px, and the header from 81px to 70px. Fields now fit their containers, and `.wrap` is 1200px wide.
- **`text-size-adjust`** is now `100%`, not `none`.
- **Plan cards** use `grid-template-rows: subgrid` across six rows, so names, prices and buttons line up even when only one plan has a badge or a name wraps.
- **Anchor links** get `scroll-padding-block-start: 5.5rem` on wide screens, where the header is sticky.
- **Footer divider** runs the full width (`.legal` has `max-inline-size: none`).
- **Email error.** The error id joins `aria-describedby` only while the error shows, `aria-invalid` follows `:user-invalid`, and a polite live region announces the error once when the reader leaves the field. This adds a short script, and the build notes now say so.
- **Card container query.** I removed the unused `container-type` and the "adapt to their own width" claim.
- **Card links** have teal headings, so they read as links without hover.
- **"Working" status dot** is amber with a beacon-ink ring, so it's clearly different from the red error dot.
- **Forced colors** keep the callout's 4px start bar.
- **Raw inverse colors** are now palette tokens (`--foam`, `--channel`), with swatches.
- **Button size rule.** The page said every button is at least 44px, but small buttons are 36px. The rule now says so.
- **Marketing copy** (added at the owner's request). Every headline, promise, statistic, price, plan name and feature on the page is now `[bracketed placeholder]` text. A highlight callout at the top says the copy isn't approved and shouldn't be reused. The voice section keeps its rules, but its examples now describe what a line should do instead of quoting sample copy.

### Skipped, and why

- **Kickers in beacon-ink.** A real point, but changing the kicker color is a taste call on how much amber the page carries. Worth deciding along with the rest of the amber question.
- **Fix log size and approval-row wash.** Design judgment, not a defect. It's better tested in the wireframes, next to a real hero.
- **Mobile header menu.** This needs a new popover pattern and a decision about phone navigation, so it belongs in the wireframes step.
- **`aria-current="page"` on the guide's nav.** This one is wrong only on the guide page itself. It's correct for the real site, and removing it would hide the current-page style demo.
- **Header `backdrop-filter`.** Nearly invisible, but harmless. Whether to keep it is a matter of taste.
- **Disabled button style, orphaned radius tile, plan note size.** These are matters of taste, or only affect the guide page.
- **Missing components** (comparison table, FAQ, proof, icons, inverse band, wordmark). Held back on purpose until later steps.

## Sources

- `design/style-guide/index.html`, `site.css` and `tokens.css`, rendered at 1440×900 and 375×812, with sizes and computed styles measured in the browser.
- modern-web-guidance guides: `card`, `navbar`, `accessible-error-announcement`, `visually-stable-font-fallbacks`, `respect-os-text-scale`, `state-aware-sticky-headers`.
