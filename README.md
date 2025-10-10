# ShStats command line tool

## About

ShStats (**sh**ell **stat**istic**s**) - simple command line tool to
display various statistics about your shell (currently only from shell
history file).

## Requirements

1. UNIX like operating system (GNU/Linux, macOS etc)
2. BASH shell (other shells will be supported later)
3. Python 3.12+ (lower versions possibly fine, but not tested)

## Usage

To print statistics about most popular shell commands from your history:

```shell
$ python3 shstats.py
```

Example output:
```
"bash" shell found
Total history records: 11158
Total history records, including subcommands: 12346
Most common commands:
1. git: 4972 (44.6%)
2. grep: 967 (8.7%)
3. ssh: 659 (5.9%)
4. cd: 481 (4.3%)
5. ls: 411 (3.7%)
6. vim: 400 (3.6%)
7. python3: 399 (3.6%)
8. cat: 278 (2.5%)
9. black: 238 (2.1%)
10. scp: 197 (1.8%)
Least common commands count: 3344 (30.0%)
```

To see some customization options:

```shell
$ python3 shstats.py --help
```
