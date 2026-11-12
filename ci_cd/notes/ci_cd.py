"""
CI/CD Tooling Overview

- git & github -> host our repo provides infrastructure for automation
- pyproject.toml -> project configuration file, configure tools and define project metadata
- black -> code formatter, enforces a consistent style
- ruff -> linter, static analysis for style violations
- mypy -> static type checker, checks for inconsistencies in defined and provided types
- bandit -> security scanner, common security vulnerabilities
- pytest -> test automation
- build -> package builder, reads pyproject.toml, creates standard distributable packages files
- twine -> packager uploader, ensure secure upload of our package files
- python-semantic-release -> versioning and relase, automatically bumps package version and creates GitHub Release based on commit history and messages


CI/CD Workflow

- push (done in parallel):
-> linting checks, formatting checks, typing checks, security checks
-> automated tests, for different python versions as well

- release:
-> SemVer
-> Github Release
-> Download/rebuild artifacts

- Publish to TestPyPi
-> Auth via OIDC
-> Publish package

-> Publish to PyPI
-> Auth via OIDC
-> public Package
"""

"""
1. Implement project
2. Add a simple GHA workflow and make sure it runs to completion
3. Add linting and format checks
4. Add typing and security checks
5. Add test automation
6. Build our Python Project
7. Publish the project to both TestPyPi and PyPi when a new tag is pushed

"""
