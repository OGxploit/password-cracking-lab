import subprocess

def run_hydra_ssh(host, username, wordlist):
    try:
        cmd = ['hydra', '-l', username, '-P', wordlist, host, 'ssh']
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
        return output
    except FileNotFoundError:
        return "[!] Hydra is not installed or not found in PATH."
    except Exception as e:
        return f"[!] Error: {e}"
