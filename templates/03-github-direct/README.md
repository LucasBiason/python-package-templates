# Template 3: GitHub Direct Installation

This template demonstrates how to install Python packages directly from GitHub repositories using git+https or git+ssh URLs.

## Features

- No external package registry needed
- Works with public and private repositories
- Version control via Git tags/branches
- Simple setup
- Free for public repositories

## Prerequisites

- Python 3.8+
- Git installed locally
- GitHub account
- For private repos: GitHub token or SSH key

## Cost

- Public repositories: Free
- Private repositories: GitHub plan cost only

## Installation Methods

### Public Repository

```bash
# Install from main branch
pip install git+https://github.com/yourusername/text-normalizer.git

# Install specific version (tag)
pip install git+https://github.com/yourusername/text-normalizer.git@v1.0.0

# Install specific branch
pip install git+https://github.com/yourusername/text-normalizer.git@develop
```

### Private Repository (HTTPS)

```bash
# With token
pip install git+https://TOKEN@github.com/yourusername/text-normalizer.git

# Interactive (will prompt for credentials)
pip install git+https://github.com/yourusername/text-normalizer.git
```

### Private Repository (SSH)

```bash
# Requires SSH key configured
pip install git+ssh://git@github.com/yourusername/text-normalizer.git
```

## Usage in requirements.txt

### Public Repository

```txt
git+https://github.com/yourusername/text-normalizer.git@v1.0.0
django>=4.2.0
```

### Private Repository

```txt
# Option 1: Use token from environment
git+https://${GITHUB_TOKEN}@github.com/yourusername/text-normalizer.git@v1.0.0

# Option 2: SSH
git+ssh://git@github.com/yourusername/text-normalizer.git@v1.0.0
```

## Docker Usage

### Public Repository

```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN pip install git+https://github.com/yourusername/text-normalizer.git@v1.0.0

COPY . .
```

### Private Repository (Token)

```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

ARG GITHUB_TOKEN

RUN pip install git+https://${GITHUB_TOKEN}@github.com/yourusername/text-normalizer.git@v1.0.0

COPY . .
```

Build:
```bash
docker build --build-arg GITHUB_TOKEN=$GITHUB_TOKEN -t myapp .
```

### Private Repository (SSH)

```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y git openssh-client && rm -rf /var/lib/apt/lists/*

RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN --mount=type=ssh pip install git+ssh://git@github.com/yourusername/text-normalizer.git@v1.0.0

COPY . .
```

Build:
```bash
docker build --ssh default -t myapp .
```

## Versioning

Use Git tags for versioning:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Users install specific versions:
```bash
pip install git+https://github.com/yourusername/text-normalizer.git@v1.0.0
```

## Advantages

- No package registry setup needed
- Direct from source control
- Works with any Git hosting
- Version control via tags
- Free for public repos

## Disadvantages

- Requires Git during installation
- Slower installation (clones repo)
- No package discovery
- Manual version management
- Requires build tools

## Best Practices

1. Always use tags for production dependencies
2. Use SSH for private repos when possible
3. Keep build requirements in pyproject.toml
4. Document installation in README
5. Test installation in clean environment

## Security

For private repositories:
- Use tokens with minimum permissions (read-only)
- Never commit tokens to repository
- Rotate tokens regularly
- Prefer SSH keys for better security
