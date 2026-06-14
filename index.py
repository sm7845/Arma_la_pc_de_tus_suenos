from flask import Flask, request, send_file, render_template
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/generar_ticket', methods=['POST'])
def generar_ticket():
    data = request.get_json()

    cliente = data.get("cliente", {})
    carrito = data.get("carrito", [])
    metodo_pago = data.get("metodo_pago", "No especificado")

    #  Validación básica
    if not carrito:
        return {"error": "Carrito vacío"}, 400

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elementos = []

    #  Nombre tienda
    elementos.append(Paragraph(" Arma tu PC", styles['Title']))
    elementos.append(Spacer(1, 10))

    #  Ticket info
    ticket_id = random.randint(1000, 9999)
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    elementos.append(Paragraph(f"<b>Ticket #{ticket_id}</b>", styles['Normal']))
    elementos.append(Paragraph(f"Fecha: {fecha}", styles['Normal']))
    elementos.append(Spacer(1, 10))

    #  Cliente
    elementos.append(Paragraph("<b>Datos del cliente:</b>", styles['Heading2']))
    elementos.append(Paragraph(f"Nombre: {cliente.get('nombre','')}", styles['Normal']))
    elementos.append(Paragraph(f"Dirección: {cliente.get('direccion','')}", styles['Normal']))
    elementos.append(Paragraph(f"Teléfono: {cliente.get('telefono','')}", styles['Normal']))
    elementos.append(Spacer(1, 10))

    #  Método de pago
    if metodo_pago == "tarjeta":
        metodo_texto = "Tarjeta 💳"
    elif metodo_pago == "efectivo":
        metodo_texto = "Efectivo contra entrega 💵"
    else:
        metodo_texto = metodo_pago

    elementos.append(Paragraph("<b>Método de pago:</b>", styles['Heading2']))
    elementos.append(Paragraph(metodo_texto, styles['Normal']))
    elementos.append(Spacer(1, 10))

    #Productos
    elementos.append(Paragraph("<b>Productos:</b>", styles['Heading2']))
    total = 0

    for producto in carrito:
        nombre = producto.get("nombre", "Producto")
        precio = float(producto.get("precio", 0))

        elementos.append(Paragraph(f"{nombre} - ${precio:.2f}", styles['Normal']))
        total += precio

    elementos.append(Spacer(1, 10))
    elementos.append(Paragraph(f"<b>Total: ${total:.2f}</b>", styles['Heading2']))

    elementos.append(Spacer(1, 20))
    elementos.append(Paragraph("¡Gracias por tu compra! 🙌", styles['Normal']))

    # 🎯 Mensaje extra según pago
    if metodo_pago == "efectivo":
        elementos.append(Paragraph("Paga al recibir tu producto.", styles['Normal']))
    elif metodo_pago == "tarjeta":
        elementos.append(Paragraph("Pago procesado correctamente.", styles['Normal']))

    doc.build(elementos)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="ticket.pdf",
        mimetype='application/pdf'
    )


@app.route("/")
def inicio():
    return render_template('index.html', titulo="Mi página")


@app.route("/para_que.html")
def para_que():
    return render_template('para_que.html')

@app.route("/componentes.html")
def componentes():
    return render_template('componentes.html')

@app.route("/grafica.html")
def grafica():
    return render_template('grafica.html')

@app.route("/carrito.html")
def carrito():
    return render_template('carrito.html')

@app.route('/pasarela.html')
def pasarela():
    return render_template('pasarela.html')

@app.route('/caja.html')
def caja():
    return render_template('caja.html')

@app.route('/fuente.html')
def fuente():
    return render_template('fuente.html')

@app.route('/monitor.html')
def monitor():
    return render_template('monitor.html')

@app.route('/procesador.html')
def procesador():
    return render_template('procesador.html')

@app.route('/ram.html')
def ram():
    return render_template('ram.html')

@app.route('/raton.html')
def raton():
    return render_template('raton.html')

@app.route('/teclado.html')
def teclado():
    return render_template('teclado.html')

@app.route('/ssd.html')
def ssd():
    return render_template('ssd.html')

@app.route('/tarjetamadre.html')
def tarjetamadre():
    return render_template('tarjetamadre.html')

@app.route('/estudio.html')
def estudio():
    return render_template('estudio.html')

@app.route('/diario.html')
def diario():
    return render_template('diario.html')

@app.route('/gama_baja.html')
def gama_baja():
    return render_template('gama_baja.html')

@app.route('/gama_media.html')
def gama_media():
    return render_template('gama_media.html')

@app.route('/gama_alta.html')
def gama_alta():
    return render_template('gama_alta.html')

if __name__ == "__main__":
    app.run(debug=True)