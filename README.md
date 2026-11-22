# Electric Dev website

The marketing site for [Electric Dev](https://electricdev.net), a managed IT company in Portland, Oregon. Built with [Hugo](https://gohugo.io).

## Run and build

```bash
npm install     # installs Hugo locally
npm run dev     # http://localhost:1313
npm run build   # production build into public/
```

Pages live in `content/`, templates in `layouts/`, styles in `assets/css/`. Design work (style guide, wireframes, sitemap) is in `design/`.

## Deploy (Cloudflare Pages)

- Build command: `npm run build`
- Output directory: `public`
- Environment variables: `NODE_VERSION=22`, `HUGO_VERSION=0.170.0`

## License

Code is licensed under the [GNU GPL v3.0](LICENSE). The fonts (Source Serif 4, IBM Plex Sans, IBM Plex Mono) are under the SIL Open Font License, and other third-party assets keep their own licenses. The Electric Dev name and logo are not covered by the GPL.
