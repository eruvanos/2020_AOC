class CallStack:
    def __init__(self):
        self.stack = []

    def push(self, frame: "CallFrame"):
        self.stack.append(frame)

    def pop(self, check=...):
        if check is ...:
            if self.stack[-1] != check:
                raise Exception("Substack not closed")

        self.stack.pop()

    def frame(self, name):
        return CallFrame(self, name)

    def log(self, *args):
        print("/".join(map(str, self.stack)), *map(str, args))


class CallFrame:
    def __init__(self, stack: CallStack, name: str):
        self.stack = stack
        self.name = str(name)

    def __enter__(self):
        self.stack.push(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stack.pop(check=self)

    def __str__(self):
        return self.name


gs = CallStack()
