# Sitemap design

This document lays out the structure for a site that launches with about 65 pages and can grow to about 200. It names the sections, the URL pattern for each, the key pages at launch, and where future pages will go. It isn't the full sitemap of the finished site. Page titles here are working labels, not copy.

It builds on the approved content outlines (`design/content-outlines/`) and the wireframes (`design/wireframes/`). The site is a traditional managed IT services site, with the AI-enhanced service desk explained inside How we work and Security, so the sitemap gives AI no section of its own.

## Structure at a glance

```
/                                   Home
├── /services/                      Services hub
│   ├── /services/managed-it/       ...one page per service (9 at launch)
│   └── /services/<service>/<topic>/   room for sub-pages later
├── /pricing/                       Pricing
├── /industries/                    Industries hub
│   └── /industries/<industry>/     (6 at launch)
├── /solutions/                     Situations hub
│   └── /solutions/<situation>/     (5 at launch)
├── /locations/                     Service area hub
│   └── /locations/<city>/          (5 at launch, depends on Q8)
├── /how-we-work/                   How we work (onboarding, support, our tools)
├── /coverage/                      Support hours, out-of-hours, on-site area
├── /security/                      Security and data handling
├── /about/                         About
├── /customers/                     Customer stories hub (stories added as they exist)
├── /compare/<topic>/               Comparisons
├── /resources/                     Guides hub
│   └── /resources/<guide>/
├── /faq/                           FAQ hub
├── /blog/                          Blog
│   ├── /blog/<post>/
│   └── /blog/topics/<topic>/       topic lists (generated)
├── /proposal/                      Get a proposal
└── /privacy/ /terms/ /accessibility/ /thank-you/ /404
```

## Sections

Each row is one Hugo content section. "Template" points at the outline and wireframe the pages use.

| Section | URL pattern | Template | Launch | Room to grow to | What grows |
|---|---|---|---|---|---|
| Core pages | `/<slug>/` | Own outlines | 9 | 10 | Careers, when hiring |
| Services | `/services/<slug>/` | Service page | 10 | 25 | Sub-pages under the big services |
| Industries | `/industries/<slug>/` | Industry page | 7 | 17 | More industries as research and customers show demand |
| Situations | `/solutions/<slug>/` | Industry page | 6 | 12 | More buyer situations |
| Locations | `/locations/<slug>/` | Location page (new, see below) | 6 | 21 | More towns and neighborhoods in the service area |
| Customer stories | `/customers/<slug>/` | Story page (new) | 1 | 11 | One page per approved story |
| Comparisons | `/compare/<slug>/` | Blog post layout | 3 | 13 | Pricing models, sourcing options, plan comparisons |
| Resources | `/resources/<slug>/` | Blog post layout | 6 | 31 | Guides, checklists, templates |
| FAQ | `/faq/` | FAQ page (new) | 1 | 1 | Questions are added to the one page |
| Blog | `/blog/<slug>/` | Blog post | 10 | 55 | Steady publishing |
| Legal and utility | `/<slug>/` | Plain page | 5 | 5 | None |
| **Total** | | | **64** | **201** | |

Launch counts include each section's hub page.

## Key pages at launch

Names are working labels. Pages marked *candidate* are placeholders for a choice the research step makes.

### Core (9)

1. Home: `/`
2. Pricing: `/pricing/`
3. How we work: `/how-we-work/`. Covers onboarding, getting support, our tools and how AI fits in, reporting, and leaving.
4. Coverage: `/coverage/`. Covers support hours (8am to 6pm, Monday to Friday), out-of-hours service, response times (Q7) and the on-site area (Q8).
5. Security and data handling: `/security/`
6. About: `/about/`
7. Get a proposal: `/proposal/`
8. Thank you: `/thank-you/` (noindex)
9. Contact details live in the footer and on Get a proposal, so there is no separate contact page. Careers waits until there's hiring.

> Count note: 8 indexable core pages plus Thank you. The table counts 9.

### Services (10)

Hub `/services/`, plus:

1. Managed IT: `/services/managed-it/`
2. Help desk and user support: `/services/help-desk/`
3. Cybersecurity: `/services/cybersecurity/`
4. Microsoft 365 and Google Workspace: `/services/microsoft-365-google-workspace/`
5. Cloud and servers: `/services/cloud-servers/`
6. Backup and disaster recovery: `/services/backup-disaster-recovery/`
7. Device setup, onboarding and offboarding: `/services/device-management/`
8. Network and Wi-Fi: `/services/network/`
9. IT strategy and planning: `/services/it-strategy/`

**Room to grow.** Sub-pages sit one level down, only under services big enough to need them, such as `/services/cybersecurity/email-security/` or `/services/microsoft-365-google-workspace/migrations/`. About 15 slots. Projects (one-off work like office moves) could become its own service later.

### Industries (7)

Hub `/industries/`, plus six *candidates*: professional services (law, accounting, architecture), healthcare clinics, financial services, nonprofits, manufacturing, construction and engineering. The research step picks the final list (Q6). Room for about 10 more.

### Situations (6)

Hub `/solutions/`, plus five *candidates*:

1. Switching IT providers: `/solutions/switching-it-providers/`
2. No IT person on staff: `/solutions/no-it-staff/`
3. Your IT team needs backup (co-managed): `/solutions/co-managed-it/`
4. Growing or opening a new office: `/solutions/growing-company/`
5. Compliance, audit or cyber insurance deadline: `/solutions/compliance-deadline/`

Room for about 6 more.

### Locations (6)

Hub `/locations/`, plus five *candidates* in the Portland metro area: Portland, Beaverton, Hillsboro, Lake Oswego and Tigard, and Vancouver, WA. Which towns to list depends on the service area and on-site decision (Q8). Each location page needs real local detail, such as on-site coverage and local customers, or it shouldn't exist. Room for about 15 more as the service area grows.

The location page is a new template: a short hero, services available there, on-site terms, local proof, and a link to Pricing. It is a cut-down industry page, so it needs no new wireframe.

### Customer stories (1)

Hub `/customers/` only, hidden from the nav until it holds at least one real story told with permission. About 10 slots.

### Comparisons (3)

1. In-house IT staff vs outsourced IT: `/compare/in-house-vs-outsourced-it/`
2. Co-managed vs fully managed IT: `/compare/co-managed-vs-fully-managed/`
3. Per-user vs per-device vs hourly pricing: `/compare/it-pricing-models/`

### Resources (6)

Hub `/resources/` plus five *candidate* guides: what managed IT costs, how to switch IT providers, questions to ask before you sign, cyber insurance controls checklist, and an IT onboarding and offboarding checklist. The research step picks the topics by what answer engines cite.

### FAQ (1)

`/faq/`: one page that gathers the questions from the other pages' FAQ sections, grouped by topic. It's built for answer engines (FAQ schema).

### Blog (10)

Hub `/blog/` plus about nine launch posts. Topics come from research. Topic list pages (`/blog/topics/<topic>/`) are generated by Hugo and aren't counted.

### Legal and utility (5)

Privacy `/privacy/`, Terms `/terms/`, Accessibility `/accessibility/`, the 404 page, and `/sitemap.xml` (generated).

## Navigation

- **Header** (from the wireframes): Services, Pricing, Industries, How we work, About, plus the Get a proposal button. On phones these go behind the Menu button. Services and Industries can open a short list of their pages later. The wireframes keep them as plain links for now.
- **Footer**: Services, Pricing, Company (About, How we work, Coverage, Industries, Situations, Locations, Customers, Blog, Contact), Resources (Guides, Comparisons, FAQ), and Trust (Security and data handling, Privacy, Terms, Accessibility).
- **Not in the header**: Situations, Locations, Resources, Compare, FAQ and Blog. They're reached from the footer, the hubs and links inside pages.

## Rules for adding pages

These keep the structure intact as the site grows from 65 to 200 pages.

1. **Every page lives in a section.** No new top-level URLs except core and legal pages.
2. **Hubs link to every page in their section,** and each page links back to its hub and to two or three related pages in other sections. For example, a service links to the industries and situations it serves.
3. **URLs are short, lowercase and permanent.** If one must change, add a redirect in Cloudflare Pages `_redirects`.
4. **Two levels deep at most,** apart from service sub-pages, which are the only third level.
5. **A page needs a reason to exist:** a search term or answer-engine question from the research (Q1), and real content. No near-duplicate location or industry pages.
6. **Indexing:** Thank you and topic lists are noindex. Everything else goes in `sitemap.xml`.

## Open questions

- **Q1.** The search term for each page, from the research.
- **Q2.** The final service list.
- **Q6.** The final industries and situations.
- **Q7.** Response times, which go on Coverage.
- **Q8.** Service area and on-site visits, which decide the Locations section.
- Whether Coverage stays a page of its own or folds into How we work and Pricing.
- When Customers goes into the nav (once there are real stories).
