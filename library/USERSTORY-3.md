---
input: dbGaP approvals for specific study-consent groups
output: Authorized access to files
task: Access dbGaP data files (genotypes, phenotypes, metadata)
tags:
- !!python/object/new:textblob.blob.Word args: - specific study-consent groups state:   string: specific study-consent groups   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - dbgap approvals state:   string: dbgap approvals   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - authorized state:   string: authorized   pos_tag: null
---
