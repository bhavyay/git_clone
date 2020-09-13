import repository
import storage.contentmanager

def cmd_init(args):
  repo = repository.repo_create(args.path)
  print("Intialized git repository in the path %s" % args.path)

def cmd_hash_object(args):
  sha = storage.contentmanager.content_read(args.path, args.type)
  print(sha)
