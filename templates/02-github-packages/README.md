# Template 2: GitHub Packages (Private)

This template demonstrates how to publish a private Python package using GitHub Packages with automated workflows.

## Features

- Private package distribution
- Integrated with GitHub
- Access control via GitHub teams
- Automated publishing with GitHub Actions
- Simple installation with authentication

## Prerequisites

- Python 3.8+
- GitHub account with Team/Pro plan ($4+/user/month)
- Git installed locally
- GitHub repository

## Cost

- GitHub Pro: $4/user/month (includes 2GB storage)
- GitHub Team: $4/user/month per user
- Additional storage: $0.25/GB/month (if over limit)

## Setup Instructions

### 1. Configure Package Name

Edit these files:
- `setup.py`: Update name, author, URL
- `pyproject.toml`: Update metadata

### 2. Create GitHub Repository

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/text-normalizer.git
git push -u origin main
```

### 3. Create GitHub Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions will automatically publish to GitHub Packages.

### 4. Installation

#### Generate Personal Access Token

1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Generate new token (classic)
3. Select scopes: `read:packages`, `write:packages`
4. Copy token

#### Install Package

```bash
pip install text-normalizer \
  --index-url https://USERNAME:TOKEN@github.com/yourusername/text-normalizer/
```

#### Using requirements.txt

```txt
--extra-index-url https://USERNAME:TOKEN@github.com/yourusername/
text-normalizer==1.0.0
```

#### In Docker

```dockerfile
FROM python:3.11-slim

ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=${GITHUB_TOKEN}

RUN pip install text-normalizer \
  --index-url https://oauth2:${GITHUB_TOKEN}@github.com/yourusername/
```

Build:
```bash
docker build --build-arg GITHUB_TOKEN=$GITHUB_TOKEN -t myapp .
```

## Security Best Practices

1. Never commit tokens to repository
2. Use environment variables for tokens
3. Rotate tokens regularly
4. Use minimum required permissions
5. Use build args in Docker (not ENV)

## Maintenance

1. Update version in `setup.py` and `pyproject.toml`
2. Create new release/tag
3. GitHub Actions publishes automatically
4. Users update with: `pip install --upgrade text-normalizer`

## Advantages

- Private code protection
- Access control via GitHub
- No additional services needed
- Integrated with GitHub workflow

## Disadvantages

- Requires paid GitHub plan
- More complex installation
- Token management required
- Storage limits
