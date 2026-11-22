---
title: Security and data handling
description: How Electric Dev accesses your systems, approves changes, uses AI tools and handles your data.
hero:
  heading: How we protect your systems and data
  lede: What we can access, who approves changes, and what happens to your data.
  primary:
    label: Get a proposal
    url: /proposal/
  secondary:
    label: Ask for our security details
    url: /proposal/
blocks:
- type: checklist
  heading: In short
  items:
  - We access your computers through a remote monitoring and management (RMM) platform, with multi-factor authentication.
  - Changes to your systems are approved by a person on our team.
  - Every action on your systems is logged.
  - You can revoke our access at any time.
- type: text
  tone: tint
  heading: How we access your systems
  body: We use remote management software installed on each computer. Only our technicians can use it, each with their own account and multi-factor authentication. Access is logged, and we review who has it every quarter.
  art: Secure remote access
- type: text
  heading: Changes and approvals
  body: Routine maintenance, like patching, runs on a schedule we agree with you. Other changes are approved by a technician before they're made, and changes with business impact are agreed with you first. Every action is recorded.
- type: table
  id: data
  tone: tint
  heading: Your data
  columns:
  - What we store
  - Where
  - How long
  rows:
  - - Ticket history and notes
    - Our ticketing system, US data centers
    - Your agreement, plus one year
  - - Device and account inventory
    - Our RMM platform, US data centers
    - Your agreement, plus 90 days
  - - Backups (Business and Secure)
    - Encrypted cloud storage, US regions
    - 30 days of versions
- type: text
  id: ai
  heading: AI tools in our service desk
  body: 'We use AI tools to help diagnose problems on the computers we support. They read logs and settings on the affected machine and suggest a fix. A technician reviews the suggestion and approves any change.


    We use a business AI service whose terms don''t allow your data to be used to train its models. The tools only see the device they''re working on.'
- type: cards
  tone: tint
  heading: Our own security practices
  min: 14rem
  items:
  - title: Multi-factor authentication
    text: On every account our team uses.
  - title: Least privilege
    text: Technicians get only the access their work needs.
  - title: Managed devices
    text: Every technician laptop is encrypted, patched and monitored.
- type: text
  heading: If something goes wrong
  body: If we find a security incident on your systems, we contain it, tell you within 24 hours, and give you a written account of what happened and what we changed.
- type: table
  tone: tint
  heading: Vendors we rely on
  columns:
  - Vendor
  - What it does
  - Data it handles
  rows:
  - - Remote monitoring and management platform
    - Remote access, monitoring and patching
    - Device names, settings and logs
  - - Endpoint protection provider
    - Malware detection and response
    - Security events from your devices
  - - Backup provider
    - Encrypted backup storage
    - Backed-up files and mailboxes
  - - AI service provider
    - Helps diagnose problems
    - Logs and settings from the affected device
- type: text
  heading: Compliance
  body: The Secure plan includes documentation support for frameworks such as HIPAA. We help you document your controls and answer auditor and insurer questions.
- type: text
  tone: tint
  heading: Report a security issue
  body: Email security@electricdev.net with the details. We'll reply within one business day.
- type: cta
  heading: Ready to see what your IT would cost?
  text: Tell us about your company and we'll send a written proposal with a price.
---
