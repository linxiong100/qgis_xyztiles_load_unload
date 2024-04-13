qs = QSettings()

for k in qs.allKeys():
    #print(k)
    if 'connections/xyz/items/' in k:
        print(k)
        qs.remove(k)
        
iface.reloadConnections()
