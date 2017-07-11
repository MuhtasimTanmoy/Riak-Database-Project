import riak
import time

start_time=time.time()


client=riak.RiakClient()


bucket=client.bucket('posts')


# # Query the indexes. The return value is a list of ``RiakLink`` objects.
resultsAll = client.index('posts', 'all_int', 1).run()

# results = client.index('posts', 'statuses_count_int', 400,500).run()


query = client.index("posts",'statuses_count_int', 400,500)
query.map("""
    function(v, kd, args) {

        var obj = Riak.mapValuesJson(v)[0]["user_name"];
        return [ {
            'key': v.key,
            'data': obj,

        } ];
    }"""
)
results = query.run()


for i in results:

    print i.get("key")
    print i.get("data")
    # print bucket.get(i[1]).data["user_name"]

print "........................................................................."
print "Total:"+str(len(resultsAll))
print "Match: "+str(len(results))
print "Time: "+str((time.time()-start_time))
