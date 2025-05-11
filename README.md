
# 🔐 Encryting-file

A simple Python script for encrypting and decrypting files using symmetric key encryption. This tool is intended for educational purposes and demonstrates basic file encryption techniques.

---

## 📁 Repository Contents

- `encryption.py`: Main script for encryption and decryption operations.
- `filekey.key`: The generated symmetric key used for encryption/decryption.
- `test.txt`: Sample plaintext file to demonstrate encryption.

---

## ⚙️ Requirements

- Python 3.x
- `cryptography` library

Install the required library using pip:

```bash
pip install cryptography
````

---

## 🚀 Usage

### 1. Generate a Key

Before encrypting files, generate a symmetric key:

```bash
python encryption.py --generate-key
```

This will create a `filekey.key` file in the current directory.

### 2. Encrypt a File

To encrypt a file (e.g., `test.txt`):

```bash
python encryption.py --encrypt test.txt
```

This will produce an encrypted file named `test.txt.encrypted`.

### 3. Decrypt a File

To decrypt the previously encrypted file:

```bash
python encryption.py --decrypt test.txt.encrypted
```

This will restore the original `test.txt` file.

---

## 🛡️ Security Note

* The symmetric key (`filekey.key`) is stored in plaintext. For enhanced security, consider implementing key protection mechanisms.
* Ensure the key file is stored securely and not shared or exposed publicly.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Adeline Eminian**

* GitHub: [@Adel2k](https://github.com/Adel2k)
* LinkedIn: [Adeline Eminian](https://www.linkedin.com/in/adeline-eminian-24adel)

---

## 📌 Disclaimer

This tool is intended for educational and testing purposes only. Use it responsibly and ensure compliance with all applicable laws and regulations.

