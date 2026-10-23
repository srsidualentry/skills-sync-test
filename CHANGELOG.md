# Changelog

All notable changes to this catalog are documented here. This project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Skill names now start with `dualentry-` so they do not collide with other vendors' skills when installed.

### Added

- README with install instructions, a generated skill catalog table, and an overview of the repository.
- MIT license, this changelog, `PRODUCT.md`, and a `docs/` folder.
- CI now fails if the README catalog table is out of date.

## [0.1.0]

### Added

- Initial set of 10 read-only skills across payables, receivables, revenue, and close.
- `scripts/build_catalog.py` and `scripts/validate.py`, plus a GitHub Action that runs both.
