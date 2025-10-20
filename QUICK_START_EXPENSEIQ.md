# 🚀 Guia Rápido: Publicação do expenseiq-shared

Este documento contém os passos práticos para aplicar a estratégia de GitHub Packages no ExpenseIQ.

---

## 📋 Pré-requisitos

- [ ] Acesso de admin na organização Astracode no GitHub
- [ ] Permissão para criar repositórios privados
- [ ] Acesso ao Render para configurar variáveis de ambiente

---

## 🔧 Etapa 1: Criar Repositório expenseiq-shared

### 1.1. No GitHub (via Interface Web)
1. Acesse: https://github.com/organizations/astracodebr/repositories/new
2. Preencha:
   - **Nome**: `expenseiq-shared`
   - **Descrição**: `Shared library for ExpenseIQ microservices - authentication, database, middleware, and common utilities`
   - **Visibilidade**: ✅ **Private**
   - **Initialize**: ❌ Não marcar nenhuma opção
3. Clique em "Create repository"

### 1.2. Copiar Código Local para o Novo Repositório

```bash
# 1. Navegar para o diretório expenseiq-shared
cd /home/lucas-biason/Projetos/Trabalho/expenseiq/expenseiq-shared

# 2. Inicializar git (se ainda não estiver)
git init

# 3. Adicionar remote
git remote add origin https://github.com/astracodebr/expenseiq-shared.git

# 4. Criar branch main
git branch -M main

# 5. Adicionar todos os arquivos
git add .

# 6. Fazer primeiro commit
git commit -m "Initial commit: ExpenseIQ Shared Library v1.0.0

- Authentication system (JWT, cache)
- Database layer (SQLAlchemy, PostgreSQL)
- Middleware (Auth, Logging, Exceptions)
- Services (User, Documents, Receipt)
- Health check routers
- Centralized logging
- 150/150 tests passing
- Complete documentation"

# 7. Push
git push -u origin main

# 8. Criar tag da versão
git tag -a v1.0.0 -m "Release v1.0.0: Initial stable release"
git push origin v1.0.0
```

---

## 🔑 Etapa 2: Criar Personal Access Token (PAT)

### 2.1. Criar Token no GitHub

1. Acesse: https://github.com/settings/tokens/new
2. Preencha:
   - **Note**: `ExpenseIQ Render - GitHub Packages Access`
   - **Expiration**: `No expiration` (ou 1 ano)
   - **Scopes**: Marcar:
     - ✅ `read:packages` - Download packages from GitHub Packages
     - ✅ `repo` (se for repositório privado)
3. Clique em "Generate token"
4. **COPIE O TOKEN IMEDIATAMENTE** (só aparece uma vez!)

**Exemplo de token**: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 2.2. Testar Token Localmente

```bash
# Criar arquivo .netrc para autenticação
cat > ~/.netrc << EOF
machine github.com
login YOUR_GITHUB_USERNAME
password YOUR_GITHUB_TOKEN
EOF

chmod 600 ~/.netrc

# Testar instalação
pip install git+https://github.com/astracodebr/expenseiq-shared.git@v1.0.0
```

---

## 🌐 Etapa 3: Configurar Render

### 3.1. Adicionar Variável de Ambiente Global

1. Acesse: https://dashboard.render.com/
2. Vá em "Environment Groups" ou crie variável em cada serviço
3. Adicione:
   - **Key**: `GITHUB_TOKEN`
   - **Value**: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (seu token)
   - **Type**: Secret

### 3.2. Método Alternativo: Arquivo .netrc no Render

Adicionar no `Dockerfile` ou `entrypoint.sh`:

```dockerfile
# No Dockerfile, ANTES do pip install
ARG GITHUB_TOKEN
RUN echo "machine github.com\nlogin astracodebr\npassword ${GITHUB_TOKEN}" > /root/.netrc
RUN chmod 600 /root/.netrc
```

Ou no `entrypoint.sh`:

```bash
#!/bin/bash
# Configurar autenticação GitHub
if [ -n "$GITHUB_TOKEN" ]; then
    echo "machine github.com" > /root/.netrc
    echo "login astracodebr" >> /root/.netrc
    echo "password $GITHUB_TOKEN" >> /root/.netrc
    chmod 600 /root/.netrc
fi
```

---

## 📦 Etapa 4: Atualizar requirements.txt dos Serviços

### Arquivo Atual (Local):
```txt
# expenseiq/user-service/requirements.txt
-e ../expenseiq-shared
```

### Novo Arquivo (Produção):

**Opção 1: Git Direct (Recomendado)**
```txt
# expenseiq/user-service/requirements.txt
git+https://github.com/astracodebr/expenseiq-shared.git@v1.0.0
```

**Opção 2: Com variável de ambiente**
```txt
# expenseiq/user-service/requirements.txt
expenseiq-shared @ git+https://${GITHUB_TOKEN}@github.com/astracodebr/expenseiq-shared.git@v1.0.0
```

⚠️ **IMPORTANTE**: 
- Use a mesma linha em TODOS os serviços
- Substitua `v1.0.0` pela versão correta
- Certifique-se de que o `.netrc` está configurado ANTES do `pip install`

---

## 🧪 Etapa 5: Testar Localmente

### 5.1. Limpar Ambiente
```bash
cd /home/lucas-biason/Projetos/Trabalho/expenseiq

# Parar containers
docker compose -f configs/docker-compose.dev.wsl.yml down -v

# Limpar cache do pip
pip cache purge
```

### 5.2. Atualizar um Serviço (Teste)

```bash
# Escolher um serviço pequeno para teste (ex: documents-service)
cd documents-service

# Atualizar requirements.txt
vim requirements.txt
# Trocar: -e ../expenseiq-shared
# Por: git+https://github.com/astracodebr/expenseiq-shared.git@v1.0.0

# Rebuild do container
cd ..
docker compose -f configs/docker-compose.dev.wsl.yml build documents-service

# Testar
docker compose -f configs/docker-compose.dev.wsl.yml up documents-service
```

### 5.3. Verificar Logs
```bash
# Procurar por:
# ✅ "Successfully installed expenseiq-shared"
# ❌ "Could not find a version that satisfies..."
# ❌ "ERROR: Could not install packages..."

docker compose -f configs/docker-compose.dev.wsl.yml logs documents-service | grep expenseiq-shared
```

---

## 🚀 Etapa 6: Deploy no Render

### 6.1. Atualizar Todos os Serviços

```bash
cd /home/lucas-biason/Projetos/Trabalho/expenseiq

# Atualizar requirements.txt de todos os serviços
for service in user-service company-service advance-service receipt-service reports-service dashboard-service documents-service ocr-service; do
    sed -i 's|-e ../expenseiq-shared|git+https://github.com/astracodebr/expenseiq-shared.git@v1.0.0|g' $service/requirements.txt
done

# Verificar mudanças
git diff

# Commit
git add .
git commit -m "feat: Update all services to use published expenseiq-shared v1.0.0"
git push origin feat/expenseiq-shared-package
```

### 6.2. Fazer Merge para Developer

```bash
git checkout developer
git merge feat/expenseiq-shared-package
git push origin developer
```

### 6.3. Monitorar Deploy

1. Acesse: https://dashboard.render.com/
2. Verifique cada serviço
3. Procure por erros de instalação
4. Se tudo OK: ✅ Migração completa!

---

## 🔄 Etapa 7: Fluxo de Atualização da Lib

### Quando Precisar Atualizar expenseiq-shared:

```bash
# 1. Fazer mudanças no código
cd /home/lucas-biason/Projetos/Trabalho/expenseiq/expenseiq-shared

# 2. Testar localmente
pytest tests/

# 3. Atualizar versão em setup.py e pyproject.toml
# De: version="1.0.0"
# Para: version="1.0.1"

# 4. Commit e push
git add .
git commit -m "feat: Add new feature XYZ"
git push

# 5. Criar nova tag
git tag -a v1.0.1 -m "Release v1.0.1: Add feature XYZ"
git push origin v1.0.1

# 6. Atualizar serviços
# Trocar em requirements.txt de cada serviço:
# De: @v1.0.0
# Para: @v1.0.1
```

---

## 📊 Checklist de Validação

### ✅ Antes do Deploy
- [ ] expenseiq-shared possui tag versionada (ex: v1.0.0)
- [ ] Testes 150/150 passando
- [ ] Token GitHub criado e testado localmente
- [ ] `.netrc` configurado no Dockerfile/entrypoint
- [ ] requirements.txt atualizados em todos os serviços
- [ ] Build local de um serviço funcionou

### ✅ Durante o Deploy
- [ ] Token configurado no Render
- [ ] Logs não mostram erro de autenticação
- [ ] Logs mostram "Successfully installed expenseiq-shared"
- [ ] Serviços iniciam sem erro

### ✅ Após o Deploy
- [ ] Health checks retornam 200
- [ ] Login funciona
- [ ] Endpoints principais funcionam
- [ ] Nenhum erro no Sentry/logs

---

## 🆘 Troubleshooting

### Erro: "Could not find a version that satisfies..."
**Causa**: Token não configurado ou repositório privado não acessível  
**Solução**: 
1. Verificar se token tem permissão `repo`
2. Verificar se `.netrc` está configurado ANTES do `pip install`
3. Testar token localmente primeiro

### Erro: "SSL: CERTIFICATE_VERIFY_FAILED"
**Causa**: Problemas com SSL no Render  
**Solução**:
```bash
pip install --trusted-host github.com git+https://...
```

### Erro: "fatal: could not read Username"
**Causa**: `.netrc` não configurado ou com permissões erradas  
**Solução**:
```bash
chmod 600 ~/.netrc  # ou /root/.netrc no container
```

---

## 📞 Suporte

Se tiver problemas:
1. Verificar logs do Render: https://dashboard.render.com/
2. Testar instalação localmente primeiro
3. Verificar se token ainda está válido
4. Consultar templates em: `/home/lucas-biason/Projetos/Infraestrutura/python-package-templates/`

---

**Boa sorte com a migração! 🚀**

