# brainwallet
Turn a phrase into a bitcoin wallet address

### Example brain.txt
```
satoshi
```

### brain2priv.py
```
$ cat brain.txt | python brain2priv.py
da2876b3eb31edb4436fa4650673fc6f01f90de2f1793c4ec332b2387b09726f
```

### priv2addru.py
```
$ cat priv.txt | python priv2addru.py
1ADJqstUMBB5zFquWg19UqZ7Zc6ePCpzLE
```

### Or combine both
```
$ cat brain.txt | python brain2priv.py | python priv2addru.py
1ADJqstUMBB5zFquWg19UqZ7Zc6ePCpzLE
```
