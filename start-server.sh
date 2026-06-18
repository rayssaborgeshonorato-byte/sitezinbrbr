#!/bin/bash

# Script para iniciar servidor local do Sistema de Rastreamento

PORT=${1:-8080}
WORKDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$WORKDIR/src"

echo "================================================================"
echo "🚀 SERVIDOR INICIANDO..."
echo "================================================================"
echo ""
echo "📍 URL DE ACESSO:"
echo "   http://localhost:$PORT/pages/login.html"
echo ""
echo "📁 Serv indo de: $SRC_DIR"
echo ""
echo "⌨️  Atalho secreto: Alt + Shift + 4 (revelar login)"
echo ""
echo "⛔ Parar servidor: Tecle CTRL+C"
echo ""
echo "================================================================"
echo ""

# Verifica se Python está disponível
if command -v python3 &> /dev/null; then
    cd "$SRC_DIR"
    python3 -m http.server $PORT
elif command -v python &> /dev/null; then
    cd "$SRC_DIR"
    python -m SimpleHTTPServer $PORT
elif command -v node &> /dev/null; then
    cd "$SRC_DIR"
    npx http-server -p $PORT
else
    echo "❌ Erro: Python ou Node.js não encontrado"
    exit 1
fi
