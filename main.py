import whois

def whois_lookup(domain):
    try:
        # Perform WHOIS lookup
        w = whois.whois(domain)
        return f"""
Domain Name: {w.domain_name}
Registrar: {w.registrar}
Whois Server: {w.whois_server}
Creation Date: {w.creation_date}
Expiration Date: {w.expiration_date}
Updated Date: {w.updated_date}
Name Servers: {w.name_servers}
Status: {w.status}
"""
    except Exception as e:
        return f"An error occurred for {domain}: {e}\n"

def main():
    input_file = 'domain.txt'
    output_file = 'output.txt'

    with open(input_file, 'r') as f:
        domains = f.read().splitlines()

    with open(output_file, 'w') as f:
        for domain in domains:
            if domain:  # Check if the line is not empty
                output = whois_lookup(domain)
                f.write(output)
                f.write("\n" + "="*50 + "\n")  # Separator for each domain entry

    print(f"WHOIS information saved to {output_file}")

if __name__ == "__main__":
    main()
