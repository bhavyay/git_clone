import repository
import storage.contentmanager
from repository import GitRepository

def cmd_init(args):
  repo = repository.repo_create(args.path)
  print("Intialized git repository in the path %s" % args.path)

def cmd_hash_object(args):
  sha = storage.contentmanager.content_read(args.path, args.type)
  print(sha)

def cmd_add(args):
  repo = GitRepository(".")
  print("cmd_add function for the file %s" % args.path)
  storage.contentmanager.content_write(args.path, "blob", repo)