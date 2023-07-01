import fire

def hello(name="World"):
  return "Hello, glad to see you,  %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)