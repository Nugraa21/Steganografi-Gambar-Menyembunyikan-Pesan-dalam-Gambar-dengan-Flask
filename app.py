from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Fungsi menyisipkan pesan ke gambar
def encode_image(file_path, message, output_path):
    img = Image.open(file_path)
    img = img.convert('RGB')
    pixels = img.getdata()

    # Mengubah pesan menjadi binary
    binary_message = ''.join(format(ord(i), '08b') for i in message) + '00000000'  # Menambahkan delimiter
    binary_index = 0

    new_pixels = []

    for pixel in pixels:
        if binary_index < len(binary_message):
            # Menyisipkan bit pesan ke dalam kanal R
            r = (pixel[0] & ~1) | int(binary_message[binary_index])
            binary_index += 1
        else:
            r = pixel[0]

        # Membuat pixel baru (RGB)
        new_pixels.append((r, pixel[1], pixel[2]))

    img.putdata(new_pixels)
    img.save(output_path)

# Fungsi membaca pesan dari gambar
def decode_image(file_path):
    img = Image.open(file_path)
    img = img.convert('RGB')
    pixel_data = img.getdata()

    binary_data = ''

    for pixel in pixel_data:
        # Mengambil bit terakhir dari kanal R untuk mengembalikan pesan
        binary_data += str(pixel[0] & 1)

    # Membagi data biner menjadi byte
    bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    decoded_message = ''
    for byte in bytes_data:
        if byte == '00000000':  # End of message
            break
        decoded_message += chr(int(byte, 2))

    return decoded_message

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    uploaded_file = request.files['image']
    message = request.form['message']

    if uploaded_file.filename != '':
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(file_path)

        output_path = os.path.join(UPLOAD_FOLDER, 'encoded_' + uploaded_file.filename)
        encode_image(file_path, message, output_path)

        return render_template('index.html', encoded_image=output_path)

    return redirect(url_for('index'))

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        uploaded_file = request.files['image']

        if uploaded_file.filename != '':
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            message = decode_image(file_path)

            return render_template('decode.html', decoded_message=message)

    return render_template('decode.html')

if __name__ == '__main__':
    app.run(debug=True)
