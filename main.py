import argparse
from src.john_runner import crack_hash_with_john
from src.hydra_runner import run_hydra_ssh

def main():
    parser = argparse.ArgumentParser(description="Password Cracking Lab")
    parser.add_argument('--john', help='Crack hashes using John the Ripper')
    parser.add_argument('--wordlist', help='Path to the wordlist file')

    parser.add_argument('--hydra-host', help='Target host for Hydra (e.g. IP or domain)')
    parser.add_argument('--hydra-user', help='Username to brute-force (e.g. root)')

    args = parser.parse_args()

    if args.john and args.wordlist:
        print(crack_hash_with_john(args.john, args.wordlist))

    if args.hydra_host and args.hydra_user and args.wordlist:
        print(run_hydra_ssh(args.hydra_host, args.hydra_user, args.wordlist))

if __name__ == '__main__':
    main()
