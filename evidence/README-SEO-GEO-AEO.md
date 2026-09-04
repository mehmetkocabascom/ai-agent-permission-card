# README SEO, GEO, and AEO Gate

Audit date: 2026-09-04

These reports cover the exact Markdown files and hashes listed below. The intended public platform is the GitHub repository README. The GitHub repository is the canonical destination for the permission-card asset; the linked MehmetKocabas.com articles provide longer background and are not duplicate copies of these files.

## English README

- Status: **PASS**
- Artifact: `README.md`
- SHA-256: `7d6cd9578753ba6a36b03dd1a5593228d19647a1ac16175655fecf64cfd6f26a`
- Platform and language: GitHub README, English
- Main intent: help a reader define an AI agent's task and authority boundary with a six-field permission card

| Dimension | Score | Applicable points | Status |
| --- | ---: | ---: | --- |
| SEO | 94/100 | 80/85 | pass |
| GEO | 96/100 | 86/90 | pass |
| AEO | 91/100 | 91/100 | pass |

## Turkish README

- Status: **PASS**
- Artifact: `README.tr.md`
- SHA-256: `bee8ea2d8462ff00d38f9f1bea0a302fad675a2f24e7ebf3bf4b232a5da88ea7`
- Platform and language: GitHub README, Turkish
- Main intent: explain how to limit an AI agent's task and authority with a six-field permission slip

| Dimension | Score | Applicable points | Status |
| --- | ---: | ---: | --- |
| SEO | 94/100 | 80/85 | pass |
| GEO | 96/100 | 86/90 | pass |
| AEO | 95/100 | 95/100 | pass |

## Hard-fail checks

- Central answer: passed. Each README defines the six fields in the opening and explains how to use them.
- Intent alignment: passed. The H1, opening, examples, validation steps, and limitations address the same permission-card task.
- Placeholder or fabricated data: passed. No placeholders remain; the price-check sample is explicitly fictional.
- Duplicate/canonical strategy: passed. GitHub is the canonical home of the asset; each language links to its corresponding first-party background article.
- Exact-final content compliance: passed. The matching file hashes scored 7% in English and 9% in Turkish on AiDetector.com.

## Findings

- LOW: GitHub README pages do not provide author/date front matter, Article schema, or a configurable canonical tag. These items are platform-controlled and excluded from the applicable score. This does not change the frozen text.
- LOW: The READMEs contain no screenshots because the asset documents a file format and command-line validation, not a third-party interface. The copyable templates and validated fictional example are the primary evidence. This does not change the frozen text.

## Claim ledger

| Claim | Type | Supporting source | Verified on | Result |
| --- | --- | --- | --- | --- |
| The repository contains Markdown, JSON, and YAML cards plus a JSON Schema validator. | repository feature | local files and 4/4 unit tests | 2026-09-04 | SUPPORTED |
| The card records intent but does not enforce runtime access control. | scope limitation | `SECURITY.md`, schema, and validator source | 2026-09-04 | SUPPORTED |
| The price-check example is fictional and uses `example.com`. | example disclosure | `examples/price-check.md` and `examples/price-check.json` | 2026-09-04 | SUPPORTED |
| The author first used the pattern to narrow an ecommerce automation pilot. | author-owned experience | first-person disclosure in both READMEs | 2026-09-04 | SUPPORTED |

## Platform checks

- H1 and opening answer: pass.
- Heading hierarchy: pass; one H1 followed by logical H2/H3 sections.
- Copyable asset links: pass; all nine local targets exist.
- Background source links: pass in the Codex in-app browser for both language versions.
- GitHub-controlled metadata, canonical tag, Article schema, and server rendering: N/A for the pre-publication content score; verify the public repository after push.
- Images and alt text: N/A; no interface or visual workflow is being claimed.

## Release evidence

- English humanizer: applied to `README.md`; exact-final AiDetector result 7%, report `a00cb526-3161-4a7f-afd5-0ba02d5a6349`.
- Turkish humanizer: applied to `README.tr.md`; exact-final AiDetector result 9%, report `d0050b03-3e9b-4db8-95ca-7cabdc9b0368`.
- Deterministic extraction: one H1 and no placeholders in either file; English has nine local links and one external link; Turkish has nine local links and one external link.
- Ordered fix list needed for PASS: none.

These scores are publication-readiness checks, not ranking, traffic, citation, or answer-engine guarantees.
