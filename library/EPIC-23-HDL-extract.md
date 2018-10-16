---
title: Extract HDL measurements from each individual study data.
blurb: Data harmonization high density lipoproteins (HDL) user narrative.
user-stories:
- USERSTORY-2
tags:
- !!python/object/new:textblob.blob.Word args: - harmonization high density lipoproteins state:   string: harmonization high density lipoproteins   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - individual study data state:   string: individual study data   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - extract hdl state:   string: extract hdl   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - user narrative state:   string: user narrative   pos_tag: null
---
This is a messy data extraction problem. For example, some studies may measure HDL at a single point in time, while others may measure across multiple visits, and some may have used different measurement techniques; this becomes both a data extraction problem (how is the data stored in the relevant CSV files?) and also a data harmonization problem (see below). Some studies may measure using method A, while others may measure using method B; this should be part of the extraction, because it is important for batch correction later on. The question of how a study measures HDL is public metadata on the dbGaP study; the actual HDL values are access-restricted.