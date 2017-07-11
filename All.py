import riak

client=riak.RiakClient()


bucket=client.bucket('posts')


# # Query the indexes. The return value is a list of ``RiakLink`` objects.
results = client.index('posts', 'all_int', 1).run()
print len(results)
# for i in results:
    #print bucket.get(i[1]).data["text"]
