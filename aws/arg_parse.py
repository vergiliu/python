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


import argparse

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--action", type=str, default="list-all", choices=["list-all", "list-running"], help="legume")
    my_args = ap.parse_args()

    print(my_args.action)

    # todo below
    # list-all is default
    # start / stop - can take optional pem
    # key - can take optional filename
    # default filename needs to be set
    #
    # create - can take # of instances (not yet)