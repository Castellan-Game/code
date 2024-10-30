import cx_Freeze

executables = [cx_Freeze.Executable('app.py')]

cx_Freeze.setup(
    name="dino game",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['./imgs', './charsprite' , './audio']}},

    executables = executables
    
)