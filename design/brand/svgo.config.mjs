// SVGO settings for the brand SVGs. Keeps the viewBox, the <title> and the
// accessible name, and uses 2-decimal precision (enough at any print size).
export default {
  multipass: true,
  floatPrecision: 2,
  plugins: [
    {
      name: "preset-default",
      params: { overrides: { removeViewBox: false, removeTitle: false, cleanupIds: false, removeUnknownsAndDefaults: { keepRoleAttr: true, keepAriaAttrs: true } } },
    },
  ],
};
