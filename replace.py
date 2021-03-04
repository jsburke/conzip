import os
import yaml

def conzip_replace(replace_yaml, files):
  assert type(files) == list
  assert len(files)  >  0
  assert os.path.isfile(replace_yaml)

  replace_dict  = yaml.load(open(replace_yaml), Loader = yaml.FullLoader)

  for fn in files:
    with open(fn, "r") as f:
      fdata = f.read()

    for key, value in replace_dict.items():
      fdata = fdata.replace(key, value)

    with open(fn, "w") as f:
      f.write(fdata)
