```markdown
# 🔐 Tailored Wordlist Generator

A customizable Python-based password wordlist generator designed for *brute-force attacks* in ethical hacking and penetration testing. Create powerful, personalized password lists using names, dates, personal info — with optional 1337-style character replacement and special character placement.

---

## 🚀 Features

- 🧩 Combines personal data: names, birthdays, pets, hobbies, etc.
- 🔁 Permutates up to 3 components (`name + year + pet`, etc.)
- 🔣 Adds special characters at start, end, or inside words
- 🧠 Replaces letters with lookalike symbols (leet mode)
- ↩️ Reverses strings, capitalizes, and appends `123`
- 📏 Max length filter + combo count limiter
- 💾 Outputs to `wordlist.txt`

---
 Preview:
<img width="716" height="762" alt="image" src="https://github.com/user-attachments/assets/224eb7ef-642a-44cf-8fea-36fa421ebf73">


## 🧪 Example Output

If inputs include:



Name: john
Surname: doe
Birthdate: 1980-08-08
Pet's Name: leo
Love: \[your location]
Other: \[your keyword]

```

With special/leet options enabled, you’ll get samples like:

```

j0hn
d0e!
L30
!john123
d0e1980
le0\_08

````

---

## ⚙️ Character Replacements (Leet Mode)

| Letter | Replacements      |
|--------|-------------------|
| a/A    | @, 4              |
| s/S    | $, 5              |
| i/I    | 1, !              |
| o/O    | 0                 |
| e/E    | 3                 |
| g/G    | 6                 |
| z/Z    | 2                 |

---

## 🛠 Usage

### 📦 Requirements

- Python 3.x
- [`colorama`](https://pypi.org/project/colorama/)  
  Install via:  
  ```bash
  pip install colorama
````

---

### ▶️ Run It

```bash
python tailoredwordlist.py
```

Follow the prompts to:

* Input names, dates, hobbies, etc.
* Enable or disable special character and leet-mode features
* Set optional max length or limit the number of combos

Your final wordlist will be saved to:

```
wordlist.txt
```

---

## 📄 License

MIT License

```
MIT License

Copyright (c) 2025 GH0STH4CKER

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

---

## ⚠️ Disclaimer

This tool is intended for **educational and legal penetration testing** purposes only.
The author **assumes no liability** for any misuse or damage caused by this software.  
Use it responsibly and at your own risk.

---
