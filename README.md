# Proxy

Now, it only supports HTTP protocol.

Tested only on Firefox and cURL.

## Use example with cURL

Usage:
```sh
curl -x "{proxy address}" "{website_address}"
```

Example:
```sh
curl -x "http://127.0.0.1:1024" "jest.bieda.it"
```

Real use:
```sh
$ curl -x "http://127.0.0.1:1024" "jest.bieda.it"

<head>
	<title>Bieda Ni</title>
</head>
<body>
	<h3>Hello</h3>
	Hello
</body>
```