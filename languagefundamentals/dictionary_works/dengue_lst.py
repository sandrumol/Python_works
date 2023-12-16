dengue_lst=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]

dist_count={}
for dist in dengue_lst:
    if dist in dist_count:
        dist_count[dist]+=1
    else:
        dist_count[dist]=1
print(dist_count)
srt_dist_count=sorted(dist_count,key=lambda k:dist_count.get(k),reverse=True)
print(srt_dist_count)
