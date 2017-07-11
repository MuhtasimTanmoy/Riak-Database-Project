import riak
import re
import time

start_time=time.time()

client=riak.RiakClient()


bucket=client.bucket('posts')


# # Query the indexes. The return value is a list of ``RiakLink`` objects.
results = client.index('posts', 'all_int', 1).run()



word="day"

# for i in results:
#     if word in bucket.get(i[1]).data["text"]:
#         print bucket.get(i[1]).data["text"]

count_for_keyword={}
count=0

for i in results:
    # print i
    currentLine=bucket.get(i[1]).data["text"]
    if re.search(r'\b' + word + r'\b', currentLine):
            area=bucket.get(i[1]).data["time_zone"]
            count+=1
            # print area
            if area in count_for_keyword:
                count_for_keyword[area]+=1
            else:
                count_for_keyword[area]=1
for i in count_for_keyword:
    print str(i) +"="+ str(count_for_keyword[i])
print "................................................................"
print "Total:"+str(len(results))
print "Matched:"+str(count)
print "Time:"+str(time.time()-start_time)
