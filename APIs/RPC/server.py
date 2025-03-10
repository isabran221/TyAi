from jsonrpcserver import method, serve

@method
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    serve("localhost", 5000)
