import cx_Freeze
import os

executables = [cx_Freeze.Executable("car_game_T.py")]
os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tk8.6'
cx_Freeze.setup(
    name="A Great Race Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )