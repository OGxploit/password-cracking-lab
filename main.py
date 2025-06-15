import argparse
from src.john_runner import crack_hash_with_john

def main():
    parser = argparse.ArgumentParser(description="Password Cracking Lab")
    parser.add_argument('--john', help='Crack hashes using John the Ripper')
    parser.add_argument('--wordlist', help='Path to the wordlist file')

    args = parser.parse_args()

    if args.john and args.wordlist:
        result = crack_hash_with_john(args.john, args.wordlist)
        print(result)
    else:
        print("[!] Usage: --john <hashfile> --wordlist <wordlist>")

if __name__ == '__main__':
    main()
