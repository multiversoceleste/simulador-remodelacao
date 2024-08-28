from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_preco_base(tipo_obra):
    if tipo_obra == 'residencial':
        return 750
    elif tipo_obra == 'comercial':
        return 800
    elif tipo_obra == 'industrial':
        return 900
    else:
        return 800

def calcular_ajuste_localizacao(localizacao):
    if localizacao == 'centro':
        return 1.2
    elif localizacao == 'periferia':
        return 0.8
    else:
        return 1.0

def calcular_ajuste_material(material):
    if material == 'luxo':
        return 1.5
    elif material == 'padrão':
        return 1.0
    elif material == 'econômico':
        return 0.7
    else:
        return 1.0

def calcular_preco_final(tipo_obra, localizacao, material, tamanho):
    preco_base = calcular_preco_base(tipo_obra)
    ajuste_localizacao = calcular_ajuste_localizacao(localizacao)
    ajuste_material = calcular_ajuste_material(material)
    preco_por_m2 = preco_base * ajuste_localizacao * ajuste_material
    preco_final = preco_por_m2 * tamanho
    return preco_final

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tipo_obra = request.form['tipo_obra']
        localizacao = request.form['localizacao']
        material = request.form['material']
        tamanho = float(request.form['tamanho'])
        preco_final = calcular_preco_final(tipo_obra, localizacao, material, tamanho)
        return render_template('index.html', preco_final=preco_final)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)