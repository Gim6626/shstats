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
Total history records: 10000
Most common commands:
1. git: 4738 (47.4%)
2. ssh: 602 (6.0%)
3. cd: 425 (4.2%)
4. ls: 361 (3.6%)
5. vim: 335 (3.4%)
6. python3: 291 (2.9%)
7. scp: 203 (2.0%)
8. black: 192 (1.9%)
9. cat: 179 (1.8%)
10. docker: 179 (1.8%)
Least common commands count: 2492 (24.9%)
```

To see some customization options:

```shell
$ python3 shstats.py --help
```
