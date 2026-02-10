list_names = ["Max", "Nazar", "Ira", "Olexandr"]
list_names_filt = [name for name in list_names if "r" in name]
list_names_filt_1 = filter(lambda name: "r" in name, list_names)
list_names_sorted = sorted(list_names_filt, key=lambda x: len(x))
print(list_names_sorted)