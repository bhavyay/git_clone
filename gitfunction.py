import repository

def cmd_init(args):
  repo = repository.repo_create(args.path)
  print("Intialized git repository in the path %s" % args.path)