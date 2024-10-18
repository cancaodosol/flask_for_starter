import sys

def hello(name):
    try:
        return { "message": "hello, ${name}" }
    except Exception as e:
        print(e)
        return { "is_success": False }

def main(args = []):
    if(len(args) == 0):
        return

    if(args[0] == 'hello'):
        print("hi!")
        return

if __name__ == "__main__":
    args = sys.argv
    main(args[1:])