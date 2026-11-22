// Keep screen readers in step with :user-invalid (style guide form script).
// The error joins aria-describedby only while it shows, and is announced once
// when the reader leaves the field.
const announcer = document.getElementById('form-announcer');
for (const field of document.querySelectorAll('.field')) {
  const control = field.querySelector('input, select, textarea');
  const error = field.querySelector('.error-text');
  if (!control || !error) continue;
  const base = control.getAttribute('aria-describedby') || '';
  control.setAttribute('aria-invalid', 'false');
  const sync = (event) => {
    let invalid;
    try { invalid = control.matches(':user-invalid'); } catch { invalid = !control.validity.valid && event.type !== 'input'; }
    const wasInvalid = control.getAttribute('aria-invalid') === 'true';
    control.setAttribute('aria-invalid', String(invalid));
    control.setAttribute('aria-describedby', invalid ? `${base} ${error.id}`.trim() : base);
    if (invalid && !wasInvalid && event.type !== 'input' && announcer) announcer.textContent = error.textContent;
    if (!invalid && announcer) announcer.textContent = '';
  };
  for (const type of ['blur', 'change', 'input', 'invalid']) control.addEventListener(type, sync);
}

// "Call me" makes the phone number required.
const call = document.getElementById('f-call');
const phone = document.getElementById('f-phone');
const optional = document.getElementById('f-phone-opt');
if (call && phone) {
  const syncCall = () => {
    phone.required = call.checked;
    if (optional) optional.hidden = call.checked;
  };
  call.addEventListener('change', syncCall);
  syncCall();
}
