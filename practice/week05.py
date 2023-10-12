

b = "10 20-30 40-50,60"
print("10" in b)
print("11" in b)
print("12" not in b)

b = "10 20-30 40-50,60"
c = b.split()
print(c)
print("=" * 30)


a = "       Hello PYthon!        "

print(a.find("o"))
print(a.find("O"))
print(a.rfind("o"))
print()

print(a.strip())
print(f"[{a.strip()}]")
print(f"[{a.lstrip()}]")
print(f"[{a.rstrip()}]")
print()

print(a.upper())    # HELLO PYTHON!
print(a.lower())    # hello python!
print(a.title())    # Hello Python!