# import json


# with open('us-10m.v1.json') as f:
#     data1 = json.load(f)

# with open('us-counties.v3.json') as f:
#     data2 = json.load(f)

# # for e in data2['features']:
# #     ID = e['id']
# #     if (len(ID) == 4):
# #         e['id'] = '0'+ ID
    


# for i in data1['objects']['counties']['geometries']:
#     for e in data2['objects']['collection']['geometries']:
#         if e['id'] == i['id']:
#             i['arcs'] = e['arcs']
#             break

# with open('us-10m.v3.json', 'w') as outfile:
#     json.dump(data1, outfile)

# # with open('us-counties.v4.json', 'w') as outfile:
# #     json.dump(data2, outfile)

import csv


def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )


out = []
with open('2016.2.csv', newline='') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for i in csv_reader:
        if len(i[0]) == 4:
            i[0] = '0' + i[0]
        out.append(i)
ids = [item[0] for item in out]

for row in list_duplicates(ids):
    print(row)

# with open('2016.2.csv', 'w', newline='') as outfile:
#     writer = csv.writer(outfile, delimiter=',')
#     for row in out:
#         writer.writerow(row)
