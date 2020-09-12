import configparser
import utils
import os

class GitRepository(object):
  """A git repository"""

  worktree = None
  gitdir = None
  config = None

  def __init__(self, path, force=False):
    self.worktree = path
    self.gitdir = os.path.join(path, ".git")
    
    if not (force or os.path.isdir(self.gitdir)):
      raise Exception("Not a Git repository %s" % path)

    self.conf = configparser.ConfigParser()
    cf = utils.repo_file(self, "config")

    if cf and os.path.exists(cf):
      self.conf.read([cf])
    elif not force:
      raise Exception("Configuration file missing")

    if not force:
      vers = int(self.conf.get("core", "repositoryformatversion"))
      if vers != 0:
        raise Exception("Unsupported repositoryformatversion %s" % vers)


def repo_create(path):
  """Create a new repository at path."""

  repo = GitRepository(path, True)

  if os.path.exists(repo.worktree):
    if not os.path.isdir(repo.worktree):
      raise Exception ("%s is not a directory!" % path)
    if os.listdir(repo.worktree):
      raise Exception("%s is not empty!" % path)
  else:
    os.makedirs(repo.worktree)

  assert(utils.repo_dir(repo, "branches", mkdir=True))
  assert(utils.repo_dir(repo, "objects", mkdir=True))
  assert(utils.repo_dir(repo, "refs", "tags", mkdir=True))
  assert(utils.repo_dir(repo, "refs", "heads", mkdir=True))

  with open(utils.repo_file(repo, "description"), "w") as f:
    f.write("Unnamed repository; edit this file 'description' to name the repository.\n")

  with open(utils.repo_file(repo, "HEAD"), "w") as f:
    f.write("ref: refs/heads/master\n")

  with open(utils.repo_file(repo, "config"), "w") as f:
    config = repo_default_config()
    config.write(f)

  return repo

def repo_default_config():
  ret = configparser.ConfigParser()

  ret.add_section("core")
  ret.set("core", "repositoryformatversion", "0")
  ret.set("core", "filemode", "false")
  ret.set("core", "bare", "false")

  return ret


    
