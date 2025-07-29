import itertools
import threading
from colorama import Fore, Style, init

init(autoreset=True)

leet_map = {
    'a': ['@', '4'],
    's': ['$', '5'],
    'i': ['1', '!'],
    'o': ['0'],
    'e': ['3'],
    'g': ['6'],
    'z': ['2'],
    'A': ['@', '4'],
    'S': ['$', '5'],
    'I': ['1', '!'],
    'O': ['0'],
    'E': ['3'],
    'G': ['6'],
    'Z': ['2'],
}

def show_banner():
    print(Fore.RED + Style.BRIGHT + r"""
                                                             
 _____     _ _               _ _ _ _           _ _ _     _   
|_   _|___|_| |___ ___ ___ _| | | | |___ ___ _| | |_|___| |_ 
  | | | .'| | | . |  _| -_| . | | | | . |  _| . | | |_ -|  _|
  |_| |__,|_|_|___|_| |___|___|_____|___|_| |___|_|_|___|_|  
""")
    print(Fore.MAGENTA + "-" * 60)
    print(Fore.GREEN + Style.BRIGHT + "                [+] Coded by GH0STH4CKER")
    print(Fore.MAGENTA + "_" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "+----------------------------------------------------------+")
    print(Fore.CYAN + Style.BRIGHT + "|             Because “123456” ain’t enough.               |")
    print(Fore.CYAN + Style.BRIGHT + "|      Tailored strikes when passwords get tough.          |")
    print(Fore.YELLOW + Style.BRIGHT + "+----------------------------------------------------------+")
    print()

def gather_inputs():
    print(Fore.BLUE + Style.BRIGHT + "🔐 Input Required Details of Victim to make the wordlist\n")
    firstname = input("First name: ")
    lastname = input("Last name: ")
    birthdate_input = input("Enter victims birthdate (YYYY-MM-DD): ")
    birth_yyyy, birth_mm, birth_dd = birthdate_input.split('-')
    pet = input("Pet's Name: ")
    love = input("Person/Object victim love: ")
    other = input("Other info (City, Hobby, etc.): ")
    add_specials = input("Add special characters at start/end? (yes/no): ").lower()
    advanced_specials = input("Add special chars inside words? (yes/no): ").lower()
    replace_leet = input("Replace letters with symbols? (yes/no): ").lower()
    max_length = int(input("Max word length (default = 12): ") or 12)
    combo_limit = int(input("Number of combinations to generate (0 = all): ") or 0)

    components = [firstname, lastname, birth_dd, birth_mm, birth_yyyy, pet, love, other]
    specials = ['!', '@', '#', '$', '%', '&'] if 'yes' in add_specials else []
    middle_specials = specials if 'yes' in advanced_specials else []
    enable_leet = True if 'yes' in replace_leet else False

    return components, specials, middle_specials, enable_leet, max_length, combo_limit

def generate_leet_variants(word):
    def recurse(index, current):
        if index == len(word):
            return [''.join(current)]
        char = word[index]
        substitutions = leet_map.get(char, [char])
        results = []
        for sub in substitutions:
            results += recurse(index + 1, current + [sub])
        return results

    return set(recurse(0, []))

def insert_specials(word, specials, middle_specials):
    variants = set()
    variants.add(word)

    for s in specials:
        variants.add(s + word)
        variants.add(word + s)

    for s in middle_specials:
        for i in range(1, len(word)):
            variants.add(word[:i] + s + word[i:])

    return variants

def format_combos(raw_combos, specials, middle_specials, leet_mode, max_length):
    final_set = set()

    for combo in raw_combos:
        base_variants = {combo}

        if leet_mode:
            base_variants |= generate_leet_variants(combo)

        for word in base_variants:
            if 0 < len(word) <= max_length:
                final_set.add(word)
                final_set |= insert_specials(word, specials, middle_specials)

    return sorted(final_set)

def generate_combos_threaded(parts, specials, middle_specials, leet_mode, max_length, combo_limit):
    combos = set()

    def worker():
        nonlocal combos
        for r in range(1, 4):
            for perm in itertools.permutations(parts, r):
                variants = set()
                plain = ''.join(perm)
                underscore = '_'.join(perm)
                caps = ''.join(p.capitalize() for p in perm)
                reversed_all = ''.join(p[::-1] for p in perm)

                variants.update([plain, underscore, caps, reversed_all])
                variants.update([v + "123" for v in variants])
                variants.update([v.upper() for v in variants])
                variants.update([v.lower() for v in variants])

                for v in variants:
                    if 0 < len(v) <= max_length:
                        combos.add(v)

                    if combo_limit and len(combos) >= combo_limit:
                        return

        for item in parts:
            variations = {
                item,
                item + "123",
                item[::-1],
                item.upper(),
                item.capitalize(),
                "_" + item,
                item + "_"
            }
            for v in variations:
                if 0 < len(v) <= max_length:
                    combos.add(v)

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()

    return format_combos(combos, specials, middle_specials, leet_mode, max_length)

def write_to_file(wordlist):
    filename = "wordlist.txt"
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print(Fore.GREEN + f"\n✅ Wordlist saved to {filename} with {len(wordlist)} entries.")

if __name__ == "__main__":
    show_banner()
    parts, specials, middle_specials, leet_mode, max_length, combo_limit = gather_inputs()
    wordlist = generate_combos_threaded(parts, specials, middle_specials, leet_mode, max_length, combo_limit)
    write_to_file(wordlist)
