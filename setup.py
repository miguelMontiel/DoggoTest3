import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "DoggoTest",
    options = {"build.exe": {"packages":["pygame"],
                             "include_files":["map.txt", "settings.py", "sprites.py"]}},
    description = "Prueba para Doggo",
    executables = executables
)