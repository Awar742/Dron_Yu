def authors(au):
    
    r = au.strip().split(", ")
    if len(r) == 2:
        lastname, firstname = r
        initials = "".join([name[0] + "." for name in firstname.split()])
        return f"{lastname} {initials}"
    return au.strip()

def convert(ris_text):
    title = ""
    journal = ""
    year = ""
    volume = ""
    sp = ""
    doi = ""
    AU = []

    for i in ris_text.splitlines():
        if "  - " not in i:
            continue  
        k, v = i.split("  - ", 1)
        v = v.strip()
        if k == "T1" or k == "TI":
            title = v
        elif k == "JO" or k == "SO":
            journal = v
        elif k == "PY":
            year = v
        elif k == "VL":
            volume = v
        elif k == "SP":
            sp = v
        elif k == "DO":
            doi = v
        elif k == "AU":
            AU.append(authors(v))

    
    parts = []
    if AU:
        parts.append(", ".join(AU))
    if title:
        parts.append(title)
    if journal:
        parts.append("// " + journal)
    if year:
        parts.append(year)
    if volume:
        parts.append("Т." + volume)
    if sp:
        parts.append("С." + sp)
    if doi:
        parts.append("DOI: " + doi)

    return ". ".join(parts) + "."

# Основна частина
with open("S2666165925000286.ris", "r", encoding="utf-8") as f1:
    s = f1.read()

r = convert(s)
print(r)
