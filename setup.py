'''import cx_Freeze

executables = [cx_Freeze.Executable("Teste.py")]
cx_Freeze.setup(
    name = "K.A.Z.",
    options={"build_exe":{'packages':["pygame","fases","inimigos","constantes"]}},

    description = "As aventuras de KAZ",
    executables = executables
    )'''

from cx_Freeze import setup, Executable
 
setup(
    name='nome-do-arquivo',
    version='1.0',
    description='K.A.Z.',
    options={'build_exe': {'packages': ['pygame','Teste','inimigos','fases','constantes']}},
    executables = [Executable(
                   script='Teste.py',
                   base=None
                   )]
)
