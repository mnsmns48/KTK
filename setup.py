from distutils.core import setup
import py2exe
setup(
    options = {"py2exe": {"typelibs": ['load_data.py'],
                          "bundle_files": 1
                          }},
    zipfile = None,
    windows=[{"script": 'window.py',
             "icon_resources": [(1, "ico2.ico")]
             }],
    data_files=[('files', ['C:/Users/cifrotech/PycharmProjects/KTK/ktk.json']), 
    ('files', ['C:/Users/cifrotech/PycharmProjects/KTK/font.jpg']), 
    ('files', ['arialmt.ttf']),
    ('files', ['ico.png'])

    ])
