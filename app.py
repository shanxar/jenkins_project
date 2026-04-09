import argparse

def greet(name, times):
    for i in range(times):
        print(f"Hello, {name}! ({i+1})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--times", type=int, default=1)
    
    args = parser.parse_args()
    greet(args.name, args.times)