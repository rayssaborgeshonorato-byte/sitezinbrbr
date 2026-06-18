document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  if (!loginForm) {
    console.warn('⚠️  Formulário de login não encontrado');
    return;
  }

  loginForm.addEventListener('submit', (ev) => {
    ev.preventDefault();
    const user = document.getElementById('user').value.trim();
    const pass = document.getElementById('pass').value.trim();

    if (!user || !pass) {
      alert('✓ Preencha usuário e senha.');
      return;
    }

    console.log('✓ Login attempt:', { user });
    // Aqui você pode adicionar autenticação real
    alert('✓ Login realizado com sucesso! Bem-vindo, ' + user);
    // window.location.href = 'telaPrincipal.html';
  });

  // Debug: verificar se o sistema de atalho está funcionando
  console.log('%c✓ Sistema de Login Carregado', 'color: #FF8F00; font-weight: bold; font-size: 14px;');
  console.log('%cPressione ALT + SHIFT + 4 para revelar o painel secreto de login', 'color: #666; font-size: 12px;');
});

