import os

def repo_file(repo, *path, mkdir=False):
  if (repo_dir(repo, *path[:-1], mkdir=mkdir)):
    return repo_path(repo, *path)


def repo_path(repo, *path):
  """Compute path under repo's gitdir."""
  return os.path.join(repo.gitdir, *path)

def repo_dir(repo, *path, mkdir=False):
  """Same as repo_path, but mkdir *path if absent if mkdir."""

  path = repo_path(repo, *path)

  if os.path.exists(path):
    if (os.path.isdir(path)):
      return path
    else :
      raise Exception("Not a directory %s" % path)

  if mkdir:
    os.makedirs(path)
    return path
  else:
    return None