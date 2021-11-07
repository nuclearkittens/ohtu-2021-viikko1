def hello(name):
    print(f'hello {name} (--:')

def who_dis():
    name = input('who dis? ')
    hello(name)

if __name__ == '__main__':
    who_dis()