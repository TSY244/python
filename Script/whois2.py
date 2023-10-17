import whois

domain = input("input domain: ")
data = whois.whois(domain)

print(f"Domain: {data.name}")
print(f"Email: {data.emails}")
print(f"Registrant: {data.registrar}")
print(f"Creation_date: {data.creation_date}")
print(f"Update_time: {data.updated_date}")