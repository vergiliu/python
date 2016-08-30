import argparse as ap
if __name__ == "__main__":
    parser = ap.ArgumentParser()
    # parser.add_argument("test", help="this is a test")
    parser.add_argument("-v", help="run with debug logging", action="store_true")  # optional
    parser.add_argument("-action", help="specify action to take on EC2 instance: create, stop, start, delete, list, list-running",
                        default="list")
    args = parser.parse_args()
    # print(args.echo)
    print("all arguments={}".format(args))