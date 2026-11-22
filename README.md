# Electric Dev website

The marketing site for [Electric Dev](https://electricdev.net), a managed IT company in Portland, Oregon. Built with [Hugo](https://gohugo.io).

## Run and build

```bash
npm install     # installs Hugo locally
npm run dev     # http://localhost:1313
npm run build   # production build into public/
```

Pages live in `content/`, templates in `layouts/`, styles in `assets/css/`. Design work (style guide, wireframes, sitemap) is in `design/`.

## Deploy (Cloudflare Workers)

Connect the repo in Cloudflare Workers (Git integration). Settings live in `wrangler.jsonc`.

- Build command: `npm run build`
- Deploy command: `npx wrangler deploy`
- Environment variable: `NODE_VERSION=22`

## License

Code is licensed under the [GNU GPL v3.0](LICENSE). The fonts (Source Serif 4, IBM Plex Sans, IBM Plex Mono) are under the SIL Open Font License, and other third-party assets keep their own licenses. The Electric Dev name and logo are not covered by the GPL.
