import hashlib
s = 'AGVSCF?TZV?WBGVHC?U'
for i in range(-50,150):
    for j in range(-50,150):
        for k in range(-50,150):
            newstr = list(s)

            newstr[6] = chr(i+ord('A'))
            newstr[10] = chr(j+ord('A'))
            newstr[17] = chr(k+ord('A'))

            ns = ''.join(newstr)

            md = hashlib.md5()
            md.update(ns.encode('utf-8'))
            nns = md.hexdigest()
            if nns[0]=='a' and nns[1]=='8' and nns[2]=='f' and nns[3]=='7' and nns[4] =='3' and nns[5] == '8':
                print(nns)
                print(ns)

#a8f738??????5ea5??????80865???af