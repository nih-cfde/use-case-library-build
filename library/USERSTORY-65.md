---
input: Public interface access and ID of dataset
output: Summary of how many users and/or analysis projects have utilized data
task: Search for uses of specific dataset
tags:
- !!python/object/new:textblob.blob.Word args: - id state:   string: id   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - summary state:   string: summary   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - public interface access state:   string: public interface access   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - users and/or analysis projects state:   string: users and/or analysis projects   pos_tag: null
---
