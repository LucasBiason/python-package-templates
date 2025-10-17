# Cost Comparison - Python Package Distribution Methods

Last Updated: October 2025

## Summary Table

| Method | Initial Setup | Monthly Cost | Storage | Bandwidth | Best For |
|--------|--------------|--------------|---------|-----------|----------|
| PyPI Public | Free | $0 | Unlimited | Unlimited | Open source |
| GitHub Packages | Free | $4-21/user | 500MB-50GB | Varies | Private teams |
| GitHub Direct | Free | $0-21/user | N/A | Varies | Quick projects |
| SSH Installation | Free | $0 | N/A | Your infra | High security |

## Detailed Breakdown

### 1. PyPI Public

**Initial Costs:**
- Account creation: Free
- Domain/hosting: Not required
- Setup time: 30 minutes

**Recurring Costs:**
- Monthly: $0
- Storage: Unlimited (reasonable use)
- Bandwidth: Unlimited
- Downloads: Unlimited

**Hidden Costs:**
- None

**Total Cost (Year 1):** $0
**Total Cost (Year 5):** $0

**ROI:** Infinite (free forever)

---

### 2. GitHub Packages

**Initial Costs:**
- Account creation: Free
- GitHub Team upgrade: $4/user/month
- Setup time: 1 hour

**Recurring Costs (per user):**

| Plan | Monthly | Storage Included | Bandwidth | Extra Storage |
|------|---------|------------------|-----------|---------------|
| Free | $0 | 500 MB | 1 GB/month | $0.25/GB |
| Pro | $4 | 2 GB | 10 GB/month | $0.25/GB |
| Team | $4 | 2 GB | 10 GB/month | $0.25/GB |
| Enterprise | $21 | 50 GB | 100 GB/month | $0.25/GB |

**Example Scenarios:**

Scenario A: 4 developers, Pro plan, 1GB package
- Plan: 4 × $4 = $16/month
- Storage: Included (under 2GB)
- **Total: $16/month = $192/year**

Scenario B: 10 developers, Team plan, 5GB package
- Plan: 10 × $4 = $40/month
- Extra storage: 3GB × $0.25 = $0.75/month
- **Total: $40.75/month = $489/year**

**Total Cost (Year 1, 4 devs):** $192
**Total Cost (Year 5, 4 devs):** $960

---

### 3. GitHub Direct

**Initial Costs:**
- Account creation: Free
- Repository: Free (public) or GitHub plan (private)
- Setup time: 15 minutes

**Recurring Costs:**

For Public Repositories:
- Monthly: $0
- Storage: GitHub free tier (1GB)
- Bandwidth: Included

For Private Repositories:
- Monthly: GitHub plan cost ($4-21/user)
- Storage: Same as GitHub plan
- Bandwidth: Included

**Example Scenarios:**

Scenario A: Public repository
- **Total: $0/month**

Scenario B: Private repo, 4 developers, Pro plan
- Plan: 4 × $4 = $16/month
- **Total: $16/month = $192/year**

**Total Cost (Year 1, private):** $192
**Total Cost (Year 5, private):** $960

---

### 4. SSH Installation

**Initial Costs:**
- SSH key generation: Free
- Account creation: Free
- Setup time: 30 minutes

**Recurring Costs:**
- Monthly: $0 (uses existing Git hosting)
- Storage: Included in Git hosting plan
- Bandwidth: Included

**Infrastructure Costs:**
- Git hosting: $0 (if using existing GitHub/GitLab)
- Key management: Negligible

**Total Cost (Year 1):** $0
**Total Cost (Year 5):** $0

---

## Cost Comparison Chart

### Startup (4 developers, Year 1)

```
PyPI Public:          $0    ████
GitHub Packages:      $192  ████████████
GitHub Direct (pub):  $0    ████
GitHub Direct (priv): $192  ████████████
SSH:                  $0    ████
```

### Established (4 developers, Year 5)

```
PyPI Public:          $0    ████
GitHub Packages:      $960  ████████████████
GitHub Direct (pub):  $0    ████
GitHub Direct (priv): $960  ████████████████
SSH:                  $0    ████
```

### Enterprise (20 developers, Year 5)

```
PyPI Public:          $0      ████
GitHub Packages:      $4,800  ████████████████████
GitHub Direct (pub):  $0      ████
GitHub Direct (priv): $4,800  ████████████████████
SSH:                  $0      ████
```

## Hidden Costs

### Development Time

| Method | Initial Setup | Maintenance (monthly) | Learning Curve |
|--------|--------------|----------------------|----------------|
| PyPI Public | 2 hours | 30 minutes | Low |
| GitHub Packages | 4 hours | 1 hour | Medium |
| GitHub Direct | 1 hour | 15 minutes | Low |
| SSH | 3 hours | 1 hour | High |

### Complexity Cost

| Method | Code Changes | CI/CD Setup | Documentation |
|--------|--------------|-------------|---------------|
| PyPI Public | None | Simple | Standard |
| GitHub Packages | Token mgmt | Moderate | Extended |
| GitHub Direct | Minimal | Simple | Minimal |
| SSH | Key mgmt | Complex | Extensive |

## Break-Even Analysis

### When does PyPI Private make sense vs GitHub Packages?

PyPI doesn't offer private packages, but if comparing similar services:

- **Small team (1-5):** GitHub Packages ($4-20/month)
- **Medium team (6-15):** Consider dedicated solution ($50-100/month)
- **Large team (16+):** Enterprise solutions ($200+/month)

### When to use each method?

**Use PyPI Public when:**
- Package is open source
- Zero cost requirement
- Maximum accessibility needed
- Standard Python ecosystem integration

**Use GitHub Packages when:**
- Code must be private
- Team already uses GitHub
- Integration with GitHub workflows desired
- Cost is acceptable ($4+/user/month)

**Use GitHub Direct when:**
- Quick prototype or internal tool
- Public repository (free)
- Don't need package registry features
- Flexibility over convenience

**Use SSH when:**
- Maximum security required
- Token management not acceptable
- Regulated industry requirements
- Have SSH infrastructure already

## Total Cost of Ownership (TCO) - 5 Years

### Scenario: 10 Developers, Private Package

| Component | PyPI (N/A) | GitHub Packages | GitHub Direct | SSH |
|-----------|-----------|-----------------|---------------|-----|
| Platform | N/A | $2,400 | $2,400 | $0 |
| Storage | N/A | $150 | Included | Included |
| Developer Time | N/A | $3,000 | $1,000 | $2,000 |
| **Total** | **N/A** | **$5,550** | **$3,400** | **$2,000** |

**Winner:** SSH Installation (for private packages with security requirements)

### Scenario: Open Source Package

| Component | PyPI | GitHub Packages | GitHub Direct | SSH |
|-----------|------|-----------------|---------------|-----|
| Platform | $0 | N/A | $0 | $0 |
| Storage | $0 | N/A | $0 | $0 |
| Developer Time | $1,000 | N/A | $500 | $1,500 |
| **Total** | **$1,000** | **N/A** | **$500** | **$1,500** |

**Winner:** PyPI Public (best ecosystem integration)

## Recommendations by Use Case

### Startup/Bootstrap
→ **PyPI Public** (if open source)  
→ **GitHub Direct** (if private, already using GitHub)

### Small Team (2-10)
→ **GitHub Packages** (good balance)  
→ **SSH** (if security-first)

### Medium Company (10-50)
→ **GitHub Packages** (if budget allows)  
→ **Self-hosted PyPI** (like devpi)

### Enterprise (50+)
→ **Self-hosted solution** (JFrog Artifactory, etc.)  
→ **GitHub Enterprise** with Packages

## Cost Optimization Tips

1. **Use public repositories when possible** - Always free
2. **Consolidate packages** - Reduce storage costs
3. **Clean old versions** - Free up storage
4. **Use SSH for high-security needs** - Zero cost
5. **Monitor usage** - Avoid overages

## Conclusion

**Best Value:**
- Open source: PyPI Public ($0)
- Private, small team: GitHub Packages ($192/year)
- Private, security focus: SSH ($0)

**Most Cost-Effective:**
SSH and PyPI Public (both free)

**Best ROI:**
Depends on team size, security needs, and existing infrastructure.
