from flask import Flask, render_template, request, redirect, url_for, flash, session
from correio import registrar_novo_pacote, rastrear

app = Flask(__name__)
app.secret_key = 'chave-super-secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rastrear', methods=['POST'])
def rastrear_pacote():
    codigo = request.form['codigo'].strip().upper()
    pacote = rastrear(codigo)
    if pacote:
        return render_template('resultado.html', codigo=codigo, pacote=pacote)
    else:
        flash('Código não encontrado.')
        return redirect(url_for('index'))

@app.route('/operador', methods=['GET', 'POST'])
def operador():
    if request.method == 'POST':
        senha = request.form.get('senha')
        if senha == '1234':
            session['autenticado'] = True
            return redirect(url_for('painel_operador'))
        else:
            flash('Senha incorreta.')
            return redirect(url_for('operador'))
    return render_template('login.html')

@app.route('/painel-operador')
def painel_operador():
    if not session.get('autenticado'):
        return redirect(url_for('operador'))
    return render_template('operador.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    if not session.get('autenticado'):
        return redirect(url_for('operador'))
    codigo = registrar_novo_pacote()
    flash(f'Código gerado: {codigo}')
    return redirect(url_for('painel_operador'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
