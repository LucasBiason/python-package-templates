# Template 1: PyPI Public Package

This template demonstrates how to publish a Python package to PyPI (Python Package Index) for free, public distribution.

## Features

- Free forever
- Global CDN distribution
- Trusted by millions of developers
- Simple installation: `pip install package-name`

## Prerequisites

- Python 3.8+
- PyPI account (https://pypi.org/account/register/)
- GitHub account
- Git installed locally

## Setup Instructions

### 1. Create PyPI Account

Visit https://pypi.org/account/register/ and create an account.

### 2. Enable Trusted Publishing

1. Go to your PyPI account settings
2. Navigate to "Publishing"
3. Add a new "pending publisher":
   - PyPI Project Name: `text-normalizer` (or your package name)
   - Owner: your-github-username
   - Repository name: text-normalizer
   - Workflow name: publish-pypi.yml
   - Environment name: (leave blank)

### 3. Customize Package

Edit these files with your information:
- `setup.py`: Update name, author, email, URL
- `pyproject.toml`: Update metadata
- `text_normalizer/__init__.py`: Update author info

### 4. Create GitHub Repository

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/text-normalizer.git
git push -u origin main
```

### 5. Create a Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

Or use GitHub UI:
1. Go to "Releases"
2. Click "Create a new release"
3. Enter tag: `v1.0.0`
4. Enter title and description
5. Click "Publish release"

The GitHub Action will automatically build and publish to PyPI.

## Usage

After publishing, users can install with:

```bash
pip install text-normalizer
```

## Cost

Completely free. No hidden costs.

## Maintenance

- Update version in `setup.py` and `pyproject.toml`
- Create new release/tag
- GitHub Actions handles the rest

## Best Practices

1. Follow semantic versioning
2. Keep CHANGELOG.md updated
3. Write comprehensive tests
4. Document all changes
5. Use pre-releases for testing (v1.0.0-alpha, v1.0.0-beta)
