document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('tracker-form');
  const input = document.getElementById('trackingCode');
  const result = document.getElementById('tracker-result');

  function validateCode(code) {
    // Exemplo de validação simples: formato ABC-123456 ou ajuste conforme seu padrão
    return /^[A-Z]{3}-\d{6}$/.test(code.trim());
  }

  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const code = input.value || '';
    result.textContent = '';

    if (!validateCode(code)) {
      result.textContent = 'Código inválido. Verifique o formato.';
      result.style.color = 'crimson';
      return;
    }

    // Se quiser, faça fetch para validar no servidor:
    // const resp = await fetch(`/api/track/validate?code=${encodeURIComponent(code)}`);
    // const json = await resp.json();
    // if (json.valid) { ... }

    result.textContent = 'Código reconhecido. Você pode prosseguir.';
    result.style.color = 'green';
  });
});