import yaml

def top_tex_gen(guide, outfile):
  top_dict  = yaml.load(open(guide), Loader = yaml.FullLoader)

  top_lines = preamble_gen(top_dict)
  top_lines = top_lines + ["\\begin{document}"]
  top_lines = top_lines + body_gen(top_dict)
  top_lines = top_lines + ["\\end{document}"]

  with open(outfile, "w+") as top:
    for line in top_lines:
      top.write(line + "\n")

def preamble_gen(top_dict):
  font     = top_dict["font"]
  doc_type = top_dict["doc_type"]

  # format the top line

  doc_class = "\\documentclass[" + font + ",letterpaper]"
  doc_class = doc_class + "{" + doc_type + "}"

  # add to file

  pre_lines = [doc_class, ""]

  # collect other tex to inclue and add

  for inc in top_dict["includes"]:
    pre_lines.append("\\input{" + inc + "}")

  pre_lines.append("")

  # add title and attribution

  pre_lines.append("\\title{" + top_dict["title"] + "}")
  pre_lines.append("\\date{" + top_dict["date"] + "}")
  pre_lines.append("\\author{" + top_dict["author"] + "}")

  pre_lines.append("")

  return pre_lines

def body_gen(top_dict):
  body_lines = ["\\maketitle", "\\tableofcontents", "\\pagebreak", ""]

  for chapter in top_dict["chapters"]:
    body_lines.append("\\addchapter{" + chapter + "}")

  body_lines.append("")
  return body_lines
