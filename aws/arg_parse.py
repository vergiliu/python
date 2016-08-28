import argparse as ap
if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument("test", help="this is a test")
    args = parser.parse_args()
    # print(args.echo)
    print("test={}".format(args.test))