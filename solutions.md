# Lab 2: Url Count

Softwares used: Hadoop, Python and GCP dataproc

I created two files UrlMapper.py and UrlReducer.py. The Mapper first extracts urls using Regex pattern matching.
Then the reducer counts the occurances and applies the filter required (more than 5)
Using Streaming Hadoop jar, executed the code with python.

## Results:

```
#                                    20
/wiki/Doi_(identifier)              18
/wiki/Google_File_System             6
/wiki/ISBN_(identifier)             18
/wiki/MapReduce                      7
/wiki/S2CID_(identifier)            14
mw-data:TemplateStyles:r1129693374   7
mw-data:TemplateStyles:r1238218222  121
mw-data:TemplateStyles:r1295599781  33
mw-data:TemplateStyles:r886049734   12
```

### 2-Worker Cluster Results
real    1m35.265s
user    0m14.381s
sys     0m1.118s


#### 4-Worker Cluster Results  
real    1m14.774s
user    0m14.232s
sys     0m0.905s

Python is significantly faster with 4 workers (from 1m 35s on 2 worker cluster to 1m 14s)
