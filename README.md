Just a simple REST API parser tool
==================================

```
usage: python index.py <filename.csv>
```

A test csv file with OpenData.org sources is provided, syntax as follows:
```
0: source's label (will be flatted to lowercase, underscored string to provide a valid export file name)
1: source's url
2: (optional) source type, currently available: csv|json
```

A standalone executable can be bundled with [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html) running:
```
sh tools.sh build
```

---

Copyright © 2021 Bertozzi Matteo