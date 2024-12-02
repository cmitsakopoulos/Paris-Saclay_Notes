class Foo:
    def __call__(self):
        def foo():
            return "foo"
        return foo
    
foo = Foo()
print(foo())