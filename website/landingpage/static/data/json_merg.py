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


