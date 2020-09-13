import repository
import storage.contentmanager

def cmd_init(args):
  repo = repository.repo_create(args.path)
  print("Intialized git repository in the path %s" % args.path)

def cmd_hash_object(args):
  with open(args.path, "rb") as fd:
    sha = storage.contentmanager.object_hash(fd, args.type.encode())
    print(sha)