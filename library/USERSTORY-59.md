---
input: UID of resource(s) within the Data Commons and the start date and end date of the time window of interest
output: All logged activity for the specified resources during the specified time window
task: Search for list of data use activity
tags:
- !!python/object/new:textblob.blob.Word args: - data commons state:   string: data commons   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - time window state:   string: time window   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - uid state:   string: uid   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - start date state:   string: start date   pos_tag: null
---
