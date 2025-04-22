def create_vcard(name, phone, email):
    with open(f"{name}.vcf", "w") as f:
        f.write("BEGIN:VCARD\n")
        f.write("VERSION:3.0\n")
        f.write(f"N:{name}\n")
        f.write(f"TEL;TYPE=CELL:{phone}\n")
        f.write(f"EMAIL:{email}\n")
        f.write("END:VCARD\n")
    print(f"vCard for {name} created successfully!")

# Example
create_vcard("John Doe", "+911234567890", "john@example.com")
