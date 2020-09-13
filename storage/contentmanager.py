import zlib
from storage.blob import GitBlob
import hashlib
from repository import GitRepository
import utils

def object_hash(fd, fmt, repo=None):
  data = fd.read()
  obj = object_from(fmt, repo, data)
  return content_hash(obj, repo)
  
def content_hash(obj, actually_write=True):
  data = obj.serialize()
  result = obj.fmt + b' ' + str(len(data)).encode() + b'\x00' + data
  return hashlib.sha1(result).hexdigest()

def content_read(file_path, type):
  with open(file_path, "rb") as fd:
    sha = object_hash(fd, type.encode())
  return sha

def content_write(file_path, type, repo):
  with open(file_path, "rb") as fd:
    data = fd.read()
  obj = object_from(type.encode(), repo, data)
  value = obj.serialize()
  result = obj.fmt + b' ' + str(len(value)).encode() + b'\x00' + value
  sha = hashlib.sha1(result).hexdigest()

  path=utils.repo_file(obj.repo, "objects", sha[0:2], sha[2:], mkdir=True)
  with open(path, 'wb') as f:
    #compress and write
    f.write(zlib.compress(result))
  return sha

def object_from(fmt, repo, data):
  if fmt==b'blob' : obj = GitBlob(repo, data)
  else:
    raise Exception("Unknown type %s!" % fmt)
  return obj

def object_write(fd, fmt, repo):
  sha = object_hash()
