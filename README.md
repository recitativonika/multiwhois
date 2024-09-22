# Multiple domain lookup in WHOIS

perform multiple domain lookup in WHOIS using Python.

## Installation & how to run?

## • Install

```bash
git clone https://github.com/recitativonika/multiwhois.git
cd multiwhois 
pip install -r requirements.txt
```
edit domain.txt and list the domains you want to check, one per line. For example:
```bash
example.com
google.com
openai.com
github.com
```
## • run the script
```bash
python main.py
```
The script will read the domains from domain.txt, perform WHOIS lookups for each domain, and save the results in a file named output.txt.

## Disclamer
Be cautious of rate limiting, as querying WHOIS servers repeatedly may result in temporary bans.
WHOIS data accuracy can vary based on registrar policies and privacy settings.
The script includes basic error handling to skip domains that cannot be queried.
