import os

# TODO: Convert to variable
GITHUB_REPOS_LINKS = {
    'seaborn': 'https://github.com/mwaskom/seaborn',
    'vscode': 'https://github.com/microsoft/vscode',
    'cloc': 'https://github.com/AlDanial/cloc',
    'nocodb': 'https://github.com/nocodb/nocodb',
    'final-db-proj': 'https://github.com/ghazalrafiei/Final-DB-Project',
    'tgdesktop': 'https://github.com/telegramdesktop/tdesktop',
    'htop': 'https://github.com/htop-dev/htop',
    'k8s': 'https://github.com/kubernetes/kubernetes',
    'numpy': 'https://github.com/numpy/numpy',
    'matplotlib': 'https://github.com/matplotlib/matplotlib',
    'pytorch': 'https://github.com/pytorch/pytorch',
    'name-dataset': 'https://github.com/philipperemy/name-dataset',
    'amn4j': 'https://github.com/Aatmaj-Zephyr/ANN4j',
    'libzmq': 'https://github.com/zeromq/libzmq',
    'pyzmq': 'https://github.com/zeromq/pyzmq',
    'ohmyzsh': 'https://github.com/ohmyzsh/ohmyzsh',
    'huggingface': 'https://github.com/huggingface/transformers',
    'mongodb': 'https://github.com/mongodb/mongo',
    'bazel': 'https://github.com/bazelbuild/bazel',
    'llama.cpp': 'https://github.com/ggerganov/llama.cpp',
    'charts': 'https://github.com/danielgindi/Charts',
    'pyart': 'https://github.com/sepandhaghighi/art',
    'vim': 'https://github.com/vim/vim',
    'neovim': 'https://github.com/neovim/neovim',
    'localsend': 'https://github.com/localsend/localsend',
    'pyrandwalk': 'https://github.com/sadrasabouri/pyrandwalk',
    'cowsay': 'https://github.com/piuccio/cowsay',
    'scc': 'https://github.com/boyter/scc',
    'Jikjik': 'https://github.com/ghazalrafiei/Jikjik',
}

REPO_DOCUMENTS = {
    'seaborn': 'doc/',
    'tgdesktop': 'docs/',
    'cloc': 'README.md',
    'final-db-proj': 'README.md',
    'htop': ['README.md', 'docs/'],
    # requires data scraping
    'vscode': 'https://code.visualstudio.com/docs',
    'nocodb': 'https://docs.nocodb.com/',
}

# TODO: covert to variables
REPOS_STATS_COLUMNS = [
    'name',
    'tag',  # version
    'SLOC',
    'release_date',
    'top_languages_in_order',
]

REPO_SIZE_LABELS = {
    'small': (0, 1000),
    'medium': (1000, 50_000),
    'large': (50_000, 100_000),
    'very large': (100_000, 1_000_000),
    'huge': (1_000_000, 99_000_000)
}

NOT_CODE_FILE_FORMATS = [
    'Markdown',
    'License',
    'gitignore',
    'Makefile',
    'SVG',
    'XCode Config',
    'ReStructuredText',
    'YAML',
    'Plain Text',
    'Vim Script',
    'Autoconf',
    'CloudFormation (YAML)',
    'JSON',
    'AsciiDoc', #documentation?
    'CMake',
    'CSV'
]

DOC_FILE_FORMATS = ['.md', '.rst']

# From ChatGPT TODO: Can be automated using chatgpt: asking the name of each folder from it.
DOC_FOLDER_NAMES = ['docs/', 'doc/', 'documentation/','docstring/', 'docstrings/','manual/','guide/','help/','wiki/','tutorials/','resources/']

DATA_DIR = './data/datasets/'
DOCS_DIR = 'data/documentations/'
STATS_FILE_DIR = './stats.csv'
GH_TOKEN_DIR = './token.txt'
