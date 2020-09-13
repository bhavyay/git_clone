import zlib
from storage.blob import GitBlob
import hashlib

def object_hash(fd, fmt, repo=None):
  data = fd.read()
  
  if fmt==b'blob' : obj=GitBlob(repo, data)
  else:
    raise Exception("Unknown type %s!" % fmt)

  return content_hash(obj, repo)
  
def content_hash(obj, actually_write=True):
  data = obj.serialize()
  result = obj.fmt + b' ' + str(len(data)).encode() + b'\x00' + data
  return hashlib.sha1(result).hexdigest()

def content_read(file_path, type):
  with open(file_path, "rb") as fd:
    sha = object_hash(fd, type.encode())
  return sha