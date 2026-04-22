from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta'

usuarios = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            flash("Preencha todos os campos!", "warning")
            return redirect(url_for('cadastro'))

        for user in usuarios:
            if user['email'] == email:
                flash("Email já cadastrado!", "danger")
                return redirect(url_for('cadastro'))

        usuarios.append({
            'nome': nome,
            'email': email,
            'senha': senha
        })

        return redirect(url_for('lista'))
    return render_template('cadastro.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)