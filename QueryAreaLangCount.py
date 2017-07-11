import riak
import time

start_time=time.time()


client=riak.RiakClient()


bucket=client.bucket('posts')


# # Query the indexes. The return value is a list of ``RiakLink`` objects.
resultsAll = client.index('posts', 'all_int', 1).run()

# results = client.index('posts', 'statuses_count_int', 400,500).run()


query = client.index("posts",'lang_bin','en')
query.map("""
    function(v, kd, args) {

        var obj = Riak.mapValuesJson(v)[0]["time_zone"];
        return [ {
            'key': v.key,
            'data': obj,

        } ];
    }"""
)
results = query.run()

count_for_lang={}
for i in results:
    # print i.get("key")
    if i.get("data") in count_for_lang:
        count_for_lang[i.get('data')]+=1
    else:
        count_for_lang[i.get('data')]=1
    # print bucket.get(i[1]).data["user_name"]

for i in count_for_lang:
    print str(i) +"="+ str(count_for_lang[i])

print "........................................................................."
print "Total:"+str(len(resultsAll))
print "Match: "+str(len(results))
print "Time: "+str((time.time()-start_time))
