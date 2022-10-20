import sys
import pathlib
import configparser

Base_dir = pathlib.Path(sys.argv[0]).parent
# print(Base_dir)
cf = configparser.ConfigParser()
cf.read(pathlib.Path(Base_dir).joinpath('settings.ini'))
src = cf.get('Default', 'src')
dsts = cf.get('Default', 'dst').split(',')
file_type = cf.get('Default', 'file_type')
