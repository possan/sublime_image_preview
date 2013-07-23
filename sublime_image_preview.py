#
# Sublime image preview plugin - Requires ImageMagick
#
# http://github.com/possan/sublime_image_preview
# 

import sublime
import sublime_plugin
import re
import math
import os
import tempfile
import subprocess

# lookup generated 2013-07-24 00:40:45.387942
resolution = 5
charmap = ' __,j_,,,j,,,vj/,vvyccvyy::;jj;;,jj//vvj//vvyrvvyy"=>jj//>jj//vjj//vvyrvpyy=)]jj/)]jj//3jj/JJJjrJJwy=]]jj7]3jj7J33jJJJJjJJJJJ\'-;>j-;,\\j/cvvyccvvyccxyy"=>>j=<>>j//vvyrcvvyrrpyy==)jj=>)]j//+njrrvwyrrpwy=)]]j=)]3j7733j7JJJwrJJww=]]3j7]333773337JJJJJJJJQ\'\'\\\\\\\'<\\\\\\cc\\\\\\ccsuyccuuy^=>\\\\=<\\\\\\r(snorrxayrrupy^=)]]=<)]3r(+iir2zawrepwq=)]]377]337773372JJQffdmQ7]]9977999779997JJJQfJdWW\'\'\\\\\\C\\\\\\\\CL\\\\\\LLLb6LLLuq^^\\\\\\C(\\\\5CCt55CCb6mFek6q^??55((555P[t55PfGGmPfemm??9997??997??Y4PfOHQPfdWQ!!999!!!99!!!44PfT44PddWW^\\\\\\\\CC\\\\\\LLLbbLLLb6LLkk6^\\\\\\5Ct\\55CCbbbFFb66Fkkk6^?555Pt555PPt55FFE6QFEE#Q!!!99!!!44P!!44PPRBQPKK&W!!!99!!!44!!T44PTTN4PXX&W'

class ImageAsTextCommand(sublime_plugin.TextCommand):

  def bestcharacter1(self, shade):
    chars = " .+#%"
    sh = (shade * 5) / (256)
    sh = math.floor(sh)
    return chars[sh]

  def bestcharacter2(self, c0,c1,c2,c3):
    # sh = corners[0] + corners[1] + corners[2] + corners[3]
    # charmap
    c0 = math.floor(resolution * c0 / 256)
    c1 = math.floor(resolution * c1 / 256)
    c2 = math.floor(resolution * c2 / 256)
    c3 = math.floor(resolution * c3 / 256)
    o = (c0 * resolution * resolution * resolution) +\
      (c1 * resolution * resolution) +\
      (c2 * resolution) +\
      (c3)
    if o < len(charmap):
      return charmap[o]
    return ' '

  def convert(self, inputpath, width, height, outputpath):
    callargs = [
      "convert",
      inputpath,
      "-resize", "%dx%d!" % (width, height),
      "-sharpen", "1",
      "-colorspace", "gray",
      "-depth", "8",
      outputpath]
    # print("convert", callargs)
    x = subprocess.call(callargs)
    # print(x)
    return os.path.exists(outputpath)

  def getimagesize(self, path):
    callargs = [
      "identify",
      path]
    # print("getimagesize", callargs)
    o = subprocess.check_output(callargs)
    # print("identify output", o)
    # 'filename PNG 1460x769 1460x769+0+0 8-bit sRGB 78.3KB 0.000u 0:00.000\n'
    a = str(o).split()
    # print("args", a)
    s = a[2].split(sep="x")
    # print("size", s)
    return {'width': int(s[0]), 'height': int(s[1])}

  def run(self, edit, **args):
    if not 'path' in args:
      return
    fn = args['path']
    # print("ImageAsTextCommand::run %s", fn)
    size = self.getimagesize(fn)
    # print("Image size", size)
    ch = self.view.line_height()
    cw = self.view.em_width()
    ca = cw / ch
    # print("Character size: %f x %f (aspect %f)" % (cw, ch, ca))
    ex = self.view.viewport_extent()
    # print("Extents", ex)
    cols = math.floor(ex[0] / cw)
    rows = math.floor(ex[1] / ch)
    # print("Viewport: %d x %d characters." % (cols, rows))
    temp = tempfile.NamedTemporaryFile(delete=True, suffix=".rgb")
    # print("Converting to %s" % temp.name)
    thumbwidth = cols * 2
    imageaspect = size['width'] / size['height']
    thumbheight = math.floor(thumbwidth * ca / imageaspect)
    # print("Resizing to %d x %d" % (thumbwidth, thumbheight))
    if thumbwidth > 600 or thumbheight > 600:
      self.view.insert(edit, 0, "Viewport to big for image preview.")
      return
    if not self.convert(fn, thumbwidth, thumbheight, temp.name):
      self.view.insert(edit, 0, "Failed to convert image for preview.")
      return
    pixels = open(temp.name, "rb").read()
    # print(pixeldata)
    # self.view.insert(edit, self.view.sel()[0].end(), "foot\n\n")
    for y in range(0, thumbheight-1, 2):
      for x in range(0, thumbwidth-1, 2):
        o = (y * thumbwidth + x) * 3
        c0 = pixels[o+0]
        c1 = pixels[o+3]
        c2 = pixels[o+(thumbwidth*3)+0]
        c3 = pixels[o+(thumbwidth*3)+3]
        # ch = self.bestcharacter1(pixels[o])
        ch = self.bestcharacter2(c0,c1,c2,c3)
        self.view.insert(edit, self.view.sel()[0].end(), ch)
      self.view.insert(edit, self.view.sel()[0].end(), "\n")


class ImageTest(sublime_plugin.EventListener):

  def checkmagick(self):
    try:
      callargs = ["convert", "-help"]
      callargs2 = ["identify", "-help"]
      o = subprocess.check_output(callargs)
      o2 = subprocess.check_output(callargs2)
      return o != "" and o2 != ""
    except (Exception, e):
      pass
    return False

  def __init__(self):
    self.magick = None
    # check that imagemagick is available
    self.imageregex = re.compile(r".*\.(png|jpe?g|gif|bmp|tiff?|psd)$", re.I)

  def might_be_image(self, filename):
    m = self.imageregex.match(filename)
    return True if m else False

  def on_load_async(self, view):
    fn = view.file_name()
    if not self.might_be_image(fn):
      return
    # print("Load async; filename=%s" % fn)
    if self.magick == None:
      self.magick = self.checkmagick()
    if self.magick == False:
      print("Can't find ImageMagick (convert and identify)")
      return
    # print("Try to load image.")
    w = view.window()
    n = w.new_file()
    n.set_name(fn + '.imagepreview')
    n.run_command('image_as_text', {'path': fn})
    n.set_scratch(True)
    n.set_read_only(True)
    n.settings().set('word_wrap', False)
    w.focus_view(n)
    view.close()
