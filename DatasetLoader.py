import json
import riak

client=riak.RiakClient()

bucket=client.bucket('posts')



with open('FixedDataset.json') as f:
    data=json.load(f);
    # print type(data[0])
    # print data[3000]["user"]["lang"],
    for i in range(0,3850):
        # print data[i]["id_str"]
        print i
        if("delete" in data[i]):
            print "delete" in data[i]
            continue
        post=bucket.new(
                data[i]["id_str"],{
                'id':data[i]["id"],
                'id_str':data[i]["id_str"],
                'text':data[i]["text"],
                'retweet_count':data[i]["retweet_count"],
                'user_id':data[i]["user"]["id"],
                'user_id_str':data[i]["user"]["id_str"],
                'user_name':data[i]["user"]["name"],
                'location':data[i]["user"]["location"],
                'description':data[i]["user"]["description"],
                'friends_count':data[i]["user"]["friends_count"],
                'favourites_count':data[i]["user"]["favourites_count"],
                'time_zone':data[i]["user"]["time_zone"],
                'statuses_count':data[i]["user"]["statuses_count"],
                'lang':data[i]["user"]["lang"],


        }
    )
        post.add_index('all_int',1);
        post.add_index('friends_count_int',data[i]["user"]["friends_count"]);
        post.add_index('statuses_count_int',data[i]["user"]["statuses_count"]);
        post.add_index('lang_bin',data[i]["user"]["lang"]);


        post.store()
