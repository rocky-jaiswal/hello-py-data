import hello


def test_greeting():
    greeting = hello.greeting()
    assert greeting == "Hello"
