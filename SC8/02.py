def WhoisOlder(**data):
    if data == {}:
        print('None is older.')
        return -1
    
    oldestAge = max(data.values())   # list of all values
    # find corresponding key
    name = [nm for nm in data.keys() if data[nm] == oldestAge]
    print(f"{', '.join(name)} is oldest.")
    return oldestAge

WhoisOlder(Chianti = 20, Mamo = 36, Hua = 30, Grannie = 70)