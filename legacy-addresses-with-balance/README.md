# How to list ALL legacy addresses with balance

### Download
Download `blockchair_bitcoin_addresses_latest.tsv.gz` from Blockchair Database Dumps

### Query
- List all addresses starts with '1'
```
cat blockchair_bitcoin_addresses_latest.tsv | grep "^1" > legacy.txt
```
