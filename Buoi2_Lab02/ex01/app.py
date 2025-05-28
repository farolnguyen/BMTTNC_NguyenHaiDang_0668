from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher  
from cipher.vigenere import VigenereCipher  
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayFairCipher
app = Flask(__name__)

# Router: Trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Router: Trang Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


# Router: Mã hóa Caesar
@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template('caesar.html', encrypted_text=encrypted_text, key_plain=key)

# Router: Giải mã Caesar
@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return render_template('caesar.html', decrypted_text=decrypted_text, key_cipher=key)
# Router: Trang Vigenere Cipher
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return render_template("vigenere.html", encrypted_text=encrypted_text, key_plain=key)

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return render_template("vigenere.html", decrypted_text=decrypted_text, key_cipher=key)
@app.route("/railfence")
def raifence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def raifence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = RailFenceCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_template("railfence.html", encrypted_text=encrypted_text, key_plain=key)

@app.route("/railfence/decrypt", methods=["POST"])
def raifence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = RailFenceCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_template("railfence.html", decrypted_text=decrypted_text, key_cipher=key)
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = TranspositionCipher()
    encrypted_text = cipher.encrypt(text, key)
    return render_template("transposition.html", encrypted_text=encrypted_text, key_plain=key)

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = TranspositionCipher()
    decrypted_text = cipher.decrypt(text, key)
    return render_template("transposition.html", decrypted_text=decrypted_text, key_cipher=key)


@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted_text = cipher.playfair_encrypt(text, matrix)
    return render_template("playfair.html", encrypted_text=encrypted_text, key_plain=key, matrix=matrix)

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted_text = cipher.playfair_decrypt(text, matrix)
    return render_template("playfair.html", decrypted_text=decrypted_text, key_cipher=key, matrix=matrix)
# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
