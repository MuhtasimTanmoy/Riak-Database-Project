import riak
import time

start_time=time.time()


client=riak.RiakClient()


bucket=client.bucket('posts')


# # Query the indexes. The return value is a list of ``RiakLink`` objects.
resultsAll = client.index('posts', 'all_int', 1).run()

results = client.index('posts', 'friends_count_int', 400,250).run()


count=0
for i in results:
    count+=1
    print bucket.get(i[1]).data["user_name"]

print "........................................................................."
print "Total:"+str(len(resultsAll))
print "Match: "+str(len(results))
print "Time: "+str((time.time()-start_time))
