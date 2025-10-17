# Template 4: SSH Installation

This template demonstrates secure Python package installation using SSH keys for authentication.

## Features

- Maximum security with SSH keys
- No tokens exposed in code or CI/CD
- Revocable access control
- Works with any Git hosting
- Free (uses existing Git infrastructure)

## Prerequisites

- Python 3.8+
- Git installed locally
- SSH key pair configured
- SSH key added to GitHub account

## Cost

Free - uses your existing Git infrastructure

## SSH Key Setup

### 1. Generate SSH Key (if needed)

```bash
ssh-keygen -t ed25519 -C "your.email@example.com" -f ~/.ssh/github_packages
```

### 2. Add SSH Key to GitHub

```bash
cat ~/.ssh/github_packages.pub
```

Copy output and add to GitHub:
- Settings > SSH and GPG keys > New SSH key

### 3. Configure SSH

Add to `~/.ssh/config`:

```
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/github_packages
  IdentitiesOnly yes
```

## Installation

### Basic Installation

```bash
pip install git+ssh://git@github.com/yourusername/text-normalizer.git
```

### Specific Version

```bash
pip install git+ssh://git@github.com/yourusername/text-normalizer.git@v1.0.0
```

### In requirements.txt

```txt
git+ssh://git@github.com/yourusername/text-normalizer.git@v1.0.0
django>=4.2.0
```

## Docker Usage

### Dockerfile with SSH

```dockerfile
# syntax=docker/dockerfile:1.4

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y git openssh-client && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p -m 0700 ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN --mount=type=ssh \
    pip install git+ssh://git@github.com/yourusername/text-normalizer.git@v1.0.0

COPY . .
```

### Build with SSH Agent

```bash
# Start SSH agent
eval $(ssh-agent)
ssh-add ~/.ssh/github_packages

# Build with SSH forwarding
docker build --ssh default -t myapp .
```

### Build with Specific Key

```bash
docker build --ssh default=$SSH_AUTH_SOCK -t myapp .
```

## CI/CD Setup

### GitHub Actions

```yaml
name: Build and Test

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up SSH
        uses: webfactory/ssh-agent@v0.8.0
        with:
          ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests
        run: pytest
```

Add SSH private key to repository secrets:
- Settings > Secrets > Actions > New repository secret
- Name: `SSH_PRIVATE_KEY`
- Value: Contents of `~/.ssh/github_packages` (private key)

### GitLab CI

```yaml
build:
  image: python:3.11-slim
  before_script:
    - apt-get update && apt-get install -y git openssh-client
    - eval $(ssh-agent -s)
    - echo "$SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -
    - mkdir -p ~/.ssh
    - ssh-keyscan github.com >> ~/.ssh/known_hosts
  script:
    - pip install -r requirements.txt
    - pytest
```

## Advantages

- Strongest security model
- No tokens to manage or rotate
- Keys can be revoked instantly
- No secrets in code
- SSH agent forwarding support
- Works with all Git providers

## Disadvantages

- Requires SSH key management
- More complex setup
- Requires SSH client
- Not suitable for public packages

## Security Best Practices

1. Use dedicated SSH keys for package installation
2. Protect private keys with passphrase
3. Use different keys for different purposes
4. Regularly rotate keys
5. Revoke compromised keys immediately
6. Never commit private keys
7. Use ssh-agent for key management
8. Limit key permissions (read-only if possible)

## Key Management

### Generate Deploy Key (Read-only)

```bash
ssh-keygen -t ed25519 -C "deploy-key" -f ~/.ssh/deploy_key
```

Add to GitHub repository:
- Settings > Deploy keys > Add deploy key
- Title: "Package Installation"
- Key: Contents of deploy_key.pub
- ✓ Allow read access
- ✗ Allow write access

### Revoke Access

Simply remove the SSH key from GitHub:
- Settings > SSH and GPG keys
- Find the key
- Click "Delete"

## Troubleshooting

### Permission denied

```bash
# Test SSH connection
ssh -T git@github.com

# Check SSH agent
ssh-add -l

# Add key if needed
ssh-add ~/.ssh/github_packages
```

### Host key verification failed

```bash
# Add GitHub to known hosts
ssh-keyscan github.com >> ~/.ssh/known_hosts
```

### Docker build fails

```bash
# Ensure SSH agent is running
eval $(ssh-agent)
ssh-add ~/.ssh/github_packages

# Build with correct SSH mounting
DOCKER_BUILDKIT=1 docker build --ssh default -t myapp .
```

## Best Use Cases

- High security requirements
- Enterprise deployments
- Private organizational packages
- When token management is problematic
- Regulated industries
- When you want revocable access

## Not Recommended For

- Public open-source packages (use PyPI)
- Simple projects (overhead not justified)
- Teams unfamiliar with SSH
- Environments without SSH support
