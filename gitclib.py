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

argsp = argsubparsers.add_parser("hash-object", help="Compute object ID from the content of the file")
argsp.add_argument("-t",
                   metavar="type",
                   dest="type",
                   choices=["blob", "commit", "tag", "tree"],
                   default="blob",
                   help="Specify the type")

argsp.add_argument("path",
                   help="Read object from <file>")

def main(argv=sys.argv[1:]):
  args = argparser.parse_args(argv)

  if args.command == "init" : gitfunction.cmd_init(args)
  elif args.command == "hash-object" : gitfunction.cmd_hash_object(args)