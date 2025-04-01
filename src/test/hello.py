hello = type("", (), {"world": {"!": "Hello, World!"}})()

print(hello.world["!"])
