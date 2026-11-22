// Pricing calculator: users × per-user price, with the plan minimum applied.
for (const form of document.querySelectorAll('[data-estimate]')) {
  const users = form.elements.users;
  const plan = form.elements.plan;
  const out = form.querySelector('output');
  const minimum = Number(form.dataset.minimum) || 1;
  const fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  const update = () => {
    const n = Math.max(1, Math.floor(Number(users.value) || 0));
    const billed = Math.max(n, minimum);
    const price = Number(plan.value);
    const from = plan.selectedOptions[0]?.dataset.from === 'true';
    const note = billed > n ? ` (billed at the ${minimum}-user minimum)` : '';
    out.textContent = `${billed} users × ${fmt.format(price)} = ${from ? 'from ' : ''}${fmt.format(billed * price)} per month${note}`;
  };
  form.addEventListener('input', update);
  form.addEventListener('submit', (e) => e.preventDefault());
  update();
}
