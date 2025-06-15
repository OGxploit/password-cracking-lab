import subprocess

def crack_hash_with_john(hash_file, wordlist):
    try:
        cmd = ['john', '--wordlist=' + wordlist, hash_file]
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
        return output
    except FileNotFoundError:
        return "[!] John the Ripper is not installed or not found in PATH."
    except Exception as e:
        return f"[!] Error: {e}"
