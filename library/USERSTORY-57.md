---
input: GUID of resource, as well as the start date and end date of the time window of interest and elevated permissions to Commons
output: All relevant details from the ledger including the UIDs of the users who performed each activity and any updating entries to the activity records in the audit trail that contain risk assessment scores for particular activities
task: Search for data use trail across users
tags:
- !!python/object/new:textblob.blob.Word args: - risk assessment scores state:   string: risk assessment scores   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - start date state:   string: start date   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - particular activities state:   string: particular activities   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - audit trail state:   string: audit trail   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - guid state:   string: guid   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - uids state:   string: uids   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - time window state:   string: time window   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - commons state:   string: commons   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - activity records state:   string: activity records   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - relevant details state:   string: relevant details   pos_tag: null
---
