ns =set()
ns.add("pen")
ns.add("pencil")
ns.add("eraser")
ns.add("sharpener")
ns.add("tool box")
print(ns)

if "pencil" in ns:
    ns.remove("pencil")
    ns.add("scale")
print(ns)

ns.discard("pen")
ns.discard("eraser")
print(ns)
