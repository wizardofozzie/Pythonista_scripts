# coding: utf-8
## Convert a json file into a pyui file and vice versa

import editor, os

extensions = ('json', 'pyui')

def pyui2json2pyui():
    target_file = editor.get_path()
    filename = os.path.basename(target_file)
    fname = os.path.splitext(filename)[0]
    rootpath, extension = os.path.splitext(target_file)
    assert extension.lstrip(".") in extensions, "'{}' must be in {}".format(extension.lstrip("."), extensions)
    other_extension = [ext for ext in extensions if ext != extension.lstrip(".")][0]
    destination_file = rootpath + "." + other_extension
    os.rename(target_file, destination_file)
    fmt = '{} was renamed to {}'
    print fmt.format(filename, os.path.basename(destination_file))

pyui2json2pyui()
