import yaml

def top_tex_gen(fname):
  top_info  = yaml.load(open(fname), Loader = yaml.FullLoader)

