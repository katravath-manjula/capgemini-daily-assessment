users = [
     {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
     {"email": "charlie@example.com", "verified": True},
     {"email": "daisy@example.com", "verified": False} ]

verification = filter(lambda x: x["verified"], users)
print(list(verification))