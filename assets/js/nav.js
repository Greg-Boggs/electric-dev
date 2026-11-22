// Responsive site navigation: one <nav>, a native popover when the links
// don't fit, inline links when they do. No fixed breakpoint: the header is
// measured, so more links or larger text move the switch point.
const header = document.querySelector('.site-header');
const inner = header?.querySelector('.header-inner');
const menu = document.getElementById('site-menu');

if (header && inner && menu && Object.hasOwn(HTMLElement.prototype, 'popover')) {
  let lastWidth = 0;

  const layout = () => {
    const width = header.clientWidth;
    const isWide = header.classList.contains('is-wide');
    // While collapsed, only re-measure when the header got wider.
    if (!isWide && width <= lastWidth) { lastWidth = width; return; }
    lastWidth = width;

    const wasOpen = menu.hasAttribute('popover') && menu.matches(':popover-open');
    header.classList.add('is-measuring', 'is-wide');
    menu.removeAttribute('popover');
    const fits = inner.scrollWidth <= inner.clientWidth;
    if (!fits) {
      header.classList.remove('is-wide');
      menu.setAttribute('popover', 'auto');
      if (wasOpen) menu.showPopover();
    }
    requestAnimationFrame(() => header.classList.remove('is-measuring'));
  };

  const observer = new ResizeObserver(layout);
  observer.observe(header);
  observer.observe(menu);
  layout();

  // Close the menu after following an in-page link.
  menu.addEventListener('click', (event) => {
    if (event.target.closest('a') && menu.matches(':popover-open')) menu.hidePopover();
  });
}
