import argparse
import sys
import zlib
import gitfunction

argparser = argparse.ArgumentParser(description="My version control system")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")

def main(argv=sys.argv[1:]):
  args = argparser.parse_args(argv)

  if args.command == "init" : gitfunction.cmd_init(args)