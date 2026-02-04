import re

def text_preproc(txt):
  return ' '.join(re.sub(r'[^а-яА-Яa-zA-Z ]', '', txt).lower().strip().split())

def get_ngramm(n,txt):
  txt = txt.lower()
  res_text = []
  for w in list(txt.split()):
    for ng in range(len(w) - n + 1):
      res_text.append(w[ng:ng+n])
  return ' '.join(res_text)