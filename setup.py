from cx_Freeze import setup, Executable

base = None

executables = [Executable("wr-stats.py", base=base)]

packages = ["csv", "re"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name = "wr-stats",
    options = options,
    version = "3",
    description = 'Reads stats.txt and outputs a table with world records beat and target.',
    executables = executables
)