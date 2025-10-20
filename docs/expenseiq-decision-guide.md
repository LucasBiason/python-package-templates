# 🎯 Guia de Decisão: Estratégia de Publicação para ExpenseIQ

Este documento ajuda a escolher a melhor estratégia de publicação para o `expenseiq-shared`.

---

## 📊 Comparação das Opções

| Critério | GitHub Packages | PyPI Privado | Git Direct | SSH |
|----------|----------------|--------------|------------|-----|
| **Privacidade** | ✅ Sim | ✅ Sim | ✅ Sim | ✅ Sim |
| **Custo** | ✅ Grátis | ❌ $7/mês | ✅ Grátis | ✅ Grátis |
| **Versionamento** | ✅ Completo | ✅ Completo | ⚠️ Manual | ⚠️ Manual |
| **CI/CD** | ✅ Automático | ✅ Automático | ❌ Manual | ❌ Manual |
| **Render** | ✅ Compatível | ✅ Compatível | ✅ Compatível | ❌ Não testado |
| **Setup** | ⚠️ Médio | ❌ Complexo | ✅ Simples | ❌ Complexo |
| **Manutenção** | ✅ Baixa | ✅ Baixa | ⚠️ Média | ⚠️ Média |

---

## 🏆 Recomendação: **GitHub Packages**

### Vantagens

1. **✅ Grátis para repositórios privados**
   - Sem custos mensais
   - Espaço ilimitado para artefatos

2. **✅ Versionamento automático**
   - Tags Git = Versões
   - Changelog automático
   - Fácil rollback

3. **✅ CI/CD integrado**
   - GitHub Actions
   - Deploy automático em cada release
   - Testes antes de publicar

4. **✅ Segurança**
   - Token pode ser revogado a qualquer momento
   - Logs de acesso
   - Controle fino de permissões

5. **✅ Compatível com Render**
   - Instalação via `pip` normal
   - Funciona com Docker builds
   - Sem configuração extra no Render

### Desvantagens

1. **⚠️ Requer token**
   - Precisa configurar PAT (Personal Access Token)
   - Token deve estar em variáveis de ambiente

2. **⚠️ Setup inicial**
   - Configurar `.netrc` no Dockerfile/entrypoint
   - Adicionar token no Render

---

## 🔧 Como Funciona (GitHub Packages)

### 1. Publicação

```bash
# Desenvolvedor faz mudanças
git commit -m "feat: Add new feature"
git push

# Cria release
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin v1.0.1

# GitHub Actions automaticamente:
# 1. Roda testes
# 2. Faz build
# 3. Publica no GitHub Packages
```

### 2. Instalação nos Serviços

```txt
# requirements.txt
git+https://github.com/astracodebr/expenseiq-shared.git@v1.0.1
```

### 3. Autenticação (One-time setup)

**Opção A: `.netrc` (Recomendado)**
```dockerfile
# Dockerfile
ARG GITHUB_TOKEN
RUN echo "machine github.com\nlogin astracodebr\npassword ${GITHUB_TOKEN}" > /root/.netrc
RUN chmod 600 /root/.netrc
```

**Opção B: URL com token**
```txt
# requirements.txt
git+https://${GITHUB_TOKEN}@github.com/astracodebr/expenseiq-shared.git@v1.0.1
```

---

## 📈 Cenários de Uso

### Cenário 1: Desenvolvimento Local
```bash
# Clone do repositório
git clone https://github.com/astracodebr/expenseiq-shared.git

# Instalar em modo editable
pip install -e ./expenseiq-shared

# Fazer mudanças e testar
# ...
```

### Cenário 2: Build no Render
```dockerfile
# Dockerfile
FROM python:3.11-slim

# Configurar autenticação GitHub
ARG GITHUB_TOKEN
RUN echo "machine github.com\nlogin astracodebr\npassword ${GITHUB_TOKEN}" > /root/.netrc
RUN chmod 600 /root/.netrc

# Instalar dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Limpar token
RUN rm /root/.netrc
```

### Cenário 3: Atualização de Versão
```bash
# Em expenseiq-shared
git tag -a v1.0.2 -m "Fix bug XYZ"
git push origin v1.0.2

# Em cada serviço (user-service, company-service, etc)
# Atualizar requirements.txt:
# De: @v1.0.1
# Para: @v1.0.2

# Commit e deploy
git commit -am "chore: Update expenseiq-shared to v1.0.2"
git push
```

---

## 🔐 Segurança

### Boas Práticas

1. **✅ Token com escopo mínimo**
   - Apenas `read:packages` e `repo`
   - Não dar permissões de `write` desnecessárias

2. **✅ Token como secret**
   - Nunca commitar token no código
   - Usar variáveis de ambiente
   - Remover `.netrc` após build

3. **✅ Rotação de token**
   - Renovar token a cada 6-12 meses
   - Usar tokens com expiração

4. **✅ Logs de acesso**
   - Monitorar quem acessa o pacote
   - Alertas de downloads suspeitos

---

## 💰 Custo Total de Propriedade (TCO)

### GitHub Packages
- **Setup**: 2-4 horas (one-time)
- **Manutenção**: 0 horas/mês
- **Custo financeiro**: $0/mês
- **TCO anual**: $0

### PyPI Privado (Gemfury)
- **Setup**: 4-6 horas (one-time)
- **Manutenção**: 0 horas/mês
- **Custo financeiro**: $7/mês = $84/ano
- **TCO anual**: $84

### Git Direct
- **Setup**: 1 hora (one-time)
- **Manutenção**: 2 horas/mês (versionamento manual)
- **Custo financeiro**: $0/mês
- **TCO anual**: 24 horas de trabalho

---

## 🚀 Roadmap Sugerido

### Fase 1: Publicação do expenseiq-shared (Semana 1-2)
- [ ] Criar repositório privado no GitHub
- [ ] Configurar GitHub Actions
- [ ] Primeira publicação (v1.0.0)
- [ ] Testar em 1 serviço (documents-service)

### Fase 2: Migração dos Serviços (Semana 3-4)
- [ ] Atualizar requirements.txt de todos os serviços
- [ ] Configurar token no Render
- [ ] Deploy e validação
- [ ] Documentação interna

### Fase 3: Separação dos Repositórios (Semana 5-12)
Seguir cronograma em `ESTRATEGIA_SEPARACAO_SERVICOS.md`:
1. OCR Service
2. Documents Service
3. Dashboard Service
4. Receipt Service
5. Advance Service
6. Reports Service
7. Company Service
8. User Service

### Fase 4: Monorepo com Submodules (Semana 13+)
- [ ] Criar repositório `expenseiq` (apenas configuração)
- [ ] Adicionar serviços como git submodules
- [ ] Atualizar CI/CD
- [ ] Documentação completa

---

## 📋 Checklist de Decisão

Marque os itens importantes para você:

### Requisitos Técnicos
- [ ] Precisa ser privado
- [ ] Precisa funcionar no Render
- [ ] Precisa de versionamento semântico
- [ ] Precisa de CI/CD automático
- [ ] Precisa ser fácil de instalar
- [ ] Precisa ter rollback fácil

### Requisitos de Negócio
- [ ] Orçamento limitado ($0/mês preferível)
- [ ] Equipe pequena (manutenção mínima)
- [ ] Segurança é crítica
- [ ] Escalabilidade futura

### Requisitos de Equipe
- [ ] Time confortável com Git
- [ ] Time confortável com GitHub Actions
- [ ] Time pode gerenciar tokens
- [ ] Time pode configurar .netrc

---

## ✅ Decisão Final

Se você marcou **4 ou mais itens** em cada seção acima, **GitHub Packages é a escolha certa**.

Se você tem **orçamento disponível** e quer **zero configuração**, considere PyPI Privado.

Se você tem uma **equipe DevOps experiente**, Git Direct pode funcionar.

---

## 📚 Recursos

- **Templates**: `/Infraestrutura/python-package-templates/`
- **Documentação validada**: `VALIDATION_REPORT.md`
- **Guia prático**: `QUICK_START_EXPENSEIQ.md`
- **Estratégia completa**: `/Trabalho/Documentações/ESTRATEGIA_SEPARACAO_SERVICOS.md`

---

**Recomendação Final**: GitHub Packages ✅

- ✅ Grátis
- ✅ Seguro
- ✅ Versionado
- ✅ Automatizado
- ✅ Validado e testado
- ✅ Compatível com Render

