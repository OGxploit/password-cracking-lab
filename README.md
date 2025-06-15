# 🔐 Password Cracking Lab

A collection of scripts and labs to automate password cracking using:
- **John the Ripper**
- **Hydra**
- (Coming soon: Hashcat)

Created by [OGxploit](https://github.com/OGxploit) — an ethical hacker building a professional toolkit.

---

## 🚀 Features

| Tool                | Function                         |
|---------------------|----------------------------------|
| 🔓 John the Ripper  | Offline hash cracking            |
| 🐍 Hydra            | Online brute-force (e.g., SSH)   |

---

## 📁 Project Structure
```
password-cracking-lab/
├── main.py
├── src/
│ ├── john_runner.py
│ ├── hydra_runner.py
│ └── init.py
├── hashes/
│ └── sample_hashes.txt
├── wordlists/
│ └── README.md
└── README.md
```

---

## 🧪 Usage

### 🔓 John (Offline Hash Cracking)
```bash
python main.py --john hashes/sample_hashes.txt --wordlist wordlists/rockyou.txt
```

### 🐍 Hydra (SSH Brute Force)
```bash
python main.py --hydra-host 192.168.1.10 --hydra-user root --wordlist wordlists/rockyou.txt
```

> ⚠️ Use Hydra only in legal test environments (e.g., TryHackMe, Hack The Box, or your own lab)

---

## ⚙️ Requirements

- Python 3

### 🧰 Tools (Linux)
```
sudo apt install john
sudo apt install hydra
```

---

## 📚 Wordlists

Place your wordlists in the `wordlists/` folder.

Recommended:
- rockyou.txt (pre-installed in Kali at `/usr/share/wordlists/rockyou.txt`)
- Or download manually from:  
  https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

---

## 👨‍💻 Author

**OGxploit**  
Ethical hacker & cybersecurity specialist in training  
- GitHub: [https://github.com/OGxploit](https://github.com/OGxploit)  
- TryHackMe: [https://tryhackme.com/p/OGxploit](https://tryhackme.com/p/OGxploit)

---

## ⚖️ License

MIT — crack ethically and responsibly. 🧠🔓
