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


count_match=0
for i in results:
    if re.search(r'\b' + word + r'\b', bucket.get(i[1]).data["text"]):
            print bucket.get(i[1]).data["text"]
            count_match+=1
print ".................................................................."
print len(results)

print "Total :"+ str(count_match)

print "Time: "+ str(time.time()-start_time)
