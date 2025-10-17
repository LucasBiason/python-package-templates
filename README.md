# 📦 Python Package Templates

A comprehensive collection of templates and tutorials for publishing Python packages using different distribution methods. This repository serves as a practical guide for developers looking to understand and implement various Python package publishing strategies.

## 🎯 Overview

This repository contains four complete, working templates demonstrating different approaches to Python package distribution:

1. **PyPI Public** - Traditional public package distribution
2. **GitHub Packages** - Private packages with GitHub integration
3. **GitHub Direct** - Direct installation from Git repositories
4. **SSH Installation** - Secure installation using SSH keys

Each template includes:
- Complete working code
- Automated CI/CD workflows
- Comprehensive documentation
- Cost analysis
- Best practices

## 📚 What's Inside

### Templates

Each template is a fully functional Python package with a simple use case (text normalization). The focus is on the packaging and distribution mechanisms rather than complex functionality.

```
templates/
├── 01-pypi-public/          # Traditional PyPI publishing
├── 02-github-packages/      # GitHub Packages (private)
├── 03-github-direct/        # Git-based installation
└── 04-ssh-installation/     # SSH-based installation
```

### Documentation

```
docs/
├── cost-comparison.md       # Detailed cost analysis
├── security-best-practices.md
├── workflow-comparison.md
└── troubleshooting.md
```

## 🚀 Quick Start

### Choose Your Distribution Method

**Need a public package?**
→ Use Template 1 (PyPI Public) - Free, simple, widely adopted

**Need a private package with GitHub integration?**
→ Use Template 2 (GitHub Packages) - $4/user/month, seamless GitHub integration

**Need flexibility without external services?**
→ Use Template 3 (GitHub Direct) - Free for public repos, simple setup

**Need maximum security?**
→ Use Template 4 (SSH) - Free, requires SSH key management

## 📖 Template Details

### Template 1: PyPI Public

**Best for:** Open source projects, public libraries

**Pros:**
- Free forever
- Global CDN
- Trusted ecosystem
- Simple installation: `pip install package-name`

**Cost:** $0/month

[View Template →](templates/01-pypi-public/)

### Template 2: GitHub Packages

**Best for:** Private corporate packages, teams using GitHub

**Pros:**
- Integrated with GitHub
- Access control via GitHub teams
- Automated publishing with GitHub Actions

**Cost:** Starting at $4/user/month (GitHub Pro)

[View Template →](templates/02-github-packages/)

### Template 3: GitHub Direct

**Best for:** Simple private packages, quick prototypes

**Pros:**
- No additional services needed
- Works with public and private repositories
- Version control via Git tags

**Cost:** $0 for public repos, GitHub pricing for private repos

[View Template →](templates/03-github-direct/)

### Template 4: SSH Installation

**Best for:** High security requirements, enterprise deployments

**Pros:**
- Maximum security with SSH keys
- No tokens exposed in CI/CD
- Revocable access

**Cost:** $0 (uses your existing Git infrastructure)

[View Template →](templates/04-ssh-installation/)

## 💰 Cost Comparison

| Method | Initial Cost | Monthly Cost | Storage | Bandwidth |
|--------|-------------|--------------|---------|-----------|
| PyPI Public | $0 | $0 | Unlimited | Unlimited |
| GitHub Packages | $0 | $4+/user | 500MB-50GB | Varies |
| GitHub Direct | $0 | $0-$4/user | N/A | Varies |
| SSH Installation | $0 | $0 | N/A | Your infrastructure |

Detailed cost analysis: [docs/cost-comparison.md](docs/cost-comparison.md)

## 🔒 Security Comparison

All templates include security best practices, but they differ in implementation:

- **PyPI Public:** Code is public, standard PyPI security
- **GitHub Packages:** Access control via GitHub, token-based
- **GitHub Direct:** Token or SSH authentication required
- **SSH Installation:** Strongest security with SSH keys

Read more: [docs/security-best-practices.md](docs/security-best-practices.md)

## 📦 Example Package: Text Normalizer

All templates use the same example package (`text-normalizer`) to demonstrate packaging concepts. The package provides simple text normalization utilities:

```python
from text_normalizer import normalize_text, remove_accents

text = "  Héllo   Wörld!  "
normalized = normalize_text(text)
print(normalized)  # "hello world!"
```

The simplicity of the example allows you to focus on the packaging and distribution mechanisms.

## 🛠️ Prerequisites

- Python 3.8+
- Git
- GitHub account (for templates 2, 3, 4)
- Basic understanding of Python packaging

## 📖 Getting Started

1. Choose a template based on your needs
2. Read the template's README
3. Follow the step-by-step tutorial
4. Adapt the template for your own package

Each template includes:
- Complete source code
- CI/CD configuration
- Installation instructions
- Usage examples
- Testing guidelines

## 🤝 Contributing

This is a reference repository. Feel free to:
- Report issues if you find errors in documentation
- Suggest improvements to examples
- Share your experience with these templates

## 📄 License

MIT License - Feel free to use these templates in your projects.

## 🔗 Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [GitHub Packages Documentation](https://docs.github.com/packages)
- [PyPI Help](https://pypi.org/help/)
- [setuptools Documentation](https://setuptools.pypa.io/)

## 📮 Support

Found this helpful? Star the repository and share with others!

Have questions? Check the documentation in each template directory.

---

**Last Updated:** October 2025  
**Maintained by:** Independent Developer  
**Purpose:** Educational reference for Python package distribution

