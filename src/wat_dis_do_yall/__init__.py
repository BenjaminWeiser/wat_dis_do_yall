# wat_dis_do_yall

A tiny example Python package that demonstrates how to publish/import
from a GitHub repo. It provides one function, \what_does_this_do()\, which
prints a message.

## Usage

\\\ash
git clone https://github.com/yourusername/wat_dis_do_yall.git
cd wat_dis_do_yall
poetry install
poetry run python example.py
\\\

You should see:

\\\
Hello from what_does_this_do()!
\\\
"@ | Out-File -Encoding UTF8 README.md

# 6. Package __init__.py
@"
def what_does_this_do():
    """
    Print a simple message to stdout.
    """
    print("Hello from what_does_this_do()!")
