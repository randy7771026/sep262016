import json

ndata = []
mintime = 0
maxtime = 0
count = 0

print 'started'

def my_add(jd,mintime, maxtime, ndata):
        count = 0
        for i in range(len (jd)):
            if jd[i]['attributes']['Time_Begun'] < mintime:
                mintime = json_data[i]['attributes']['Time_Begun']
            if jd[i]['attributes']['Time_Begun'] > maxtime:
                maxtime = json_data[i]['attributes']['Time_Begun']
                ndata.append(jd[i])
                count = count + 1
        print i
        print mintime, maxtime, count
        return jd, mintime, maxtime, ndata

with open("db.json") as db:
    json_data = json.load(db)
    mintime = json_data[0]['attributes']['Time_Begun']
    maxtime = json_data[0]['attributes']['Time_Begun']
    ndata.append(json_data[0])
    my_add(json_data, mintime, maxtime, ndata)

print 'b'

with open("d.json") as d:
    json_data = json.load(d)
    my_add(json_data, mintime, maxtime, ndata)

print 'd'

with open("dl.json") as dl:
    json_data = json.load(dl)
    my_add(json_data, mintime, maxtime, ndata)

print 'l'

with open("do.json") as do:
    json_data = json.load(do)
    my_add(json_data, mintime, maxtime, ndata)

print 'o'

with open('all3.json', 'w') as outfile:
     json.dump(json_data, outfile, sort_keys = True, indent = 4,
     ensure_ascii=False)

print mintime, maxtime, count
    
