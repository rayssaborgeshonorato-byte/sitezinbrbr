# Nova Estrutura - Sistema de Rastreamento

## 📁 Estrutura de Diretórios

```
src/
├── pages/                    # Páginas HTML
│   ├── index.html           # Redireciona para login.html
│   ├── login.html           # ✨ Reconhecimento de código + Login (Alt+Shift+4)
│   ├── telaPrincipal.html   # Tela principal após login
│   └── criadorDeCodigoDeRastreio.html  # Gerador de códigos
├── assets/
│   ├── css/
│   │   └── styles.css       # Estilos centralizados
│   ├── js/
│   │   ├── tracking-code.js # Validação de código de rastreio
│   │   └── login.js         # Lógica de login
│   └── img/                 # Imagens
```

## 🎯 Funcionalidades Principais

### 1. **Reconhecimento de Código de Rastreio**
- Primeira aba visível ao carregar `/login.html`
- Valida formato: `ABC-123456`
- Exibe mensagem de sucesso/erro

### 2. **Painel de Login Secreto** 
- **Atalho:** `Alt + Shift + 4`
- Inicialmente escondido
- Pressione novamente para esconder

### 3. **Caminhos Corretos**
- Todos os HTMLs referenciam CSS/JS com caminhos relativos
- Exemplo: `../assets/css/styles.css`

## 🚀 Como Usar

### ✅ **Opção Recomendada: Script Automático**
```bash
cd /workspaces/sitezinbrbr
bash start-server.sh
# Abra automaticamente: http://localhost:8080/pages/login.html
```

### Opção 2: Iniciar Manualmente (Python)
```bash
cd /workspaces/sitezinbrbr/src
python3 -m http.server 8080
# Abra no navegador: http://localhost:8080/pages/login.html
```

### Opção 3: Abrir Arquivo Direto (sem servidor)
- Abra no navegador: `/workspaces/sitezinbrbr/src/pages/login.html`
- ⚠️ Recursos podem não carregar perfeitamente sem servidor

## 🔑 Atalho Secreto

Pressione **Alt + Shift + 4** para revelar/esconder o painel de login.

## 📝 Notas

- CSS e JS são totalmente separados para fácil manutenção
- Validação de código feita no cliente (`tracking-code.js`)
- Login pode ser integrado a um servidor backend
