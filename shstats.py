import argparse
import os
import re
from pathlib import Path
from collections import Counter

SHELL = os.environ["SHELL"].split("/")[-1]


def parse_command_line_args():
    parser = argparse.ArgumentParser(description="Shell history statistics")
    parser.add_argument(
        "-n",
        "--top-count",
        type=int,
        default=10,
        help="Number of top counts to display",
    )
    parser.add_argument(
        "-s",
        "--keep-sudo",
        action="store_true",
        help='Keep `sudo` command in statistics, if not set actual "sudo-ed" commands will be counted in statistics',
    )
    args = parser.parse_args()
    return args


def history_file_path():
    match SHELL:
        case "bash":
            path = Path.home() / ".bash_history"
            if not path.exists():
                raise Exception(f'No bash history file found at "{path}"')
        case "zsh":
            path_1 = Path.home() / ".histfile"
            path_2 = Path.home() / ".zsh_history"
            if not path_1.exists() and not path_2.exists():
                raise Exception(f'No zsh history file found at "{path_1}" or "{path_2}"')
            path = path_1 or path_2
        case _:
            raise NotImplementedError(f'Unknown shell "{SHELL}"')
    return path


def get_history():
    with open(history_file_path(), "r") as fin:
        for line in fin:
            yield line


def get_history_count():
    with open(history_file_path(), "r") as fin:
        return sum(1 for _ in fin)


def strip_timestamp(history_record):
    match SHELL:
        case "bash":
            history_record = re.sub(r"^[ \d:\-/]+", "", history_record)
        case "zsh":
            history_record = re.sub(r"^: \d+:\d;", "", history_record)
        case _:
            raise NotImplementedError(f'Unknown shell "{SHELL}"')
    return history_record


def parse_commands(history, keep_sudo):
    for line in history:
        if not line.strip():
            continue
        line = strip_timestamp(line)
        if not keep_sudo:
            line = line.replace("sudo", "")
        command = line.strip().split()[0]
        yield command


def get_most_common_commands(commands, n=20):
    command_counts = Counter(commands)
    most_common = command_counts.most_common(n)
    most_common_commands = [record[0] for record in most_common]
    least_common_count = 0
    for command, count in command_counts.items():
        if command not in most_common_commands:
            least_common_count += command_counts[command]
    return most_common, least_common_count


def main():
    print(f'"{SHELL}" shell found')
    args = parse_command_line_args()

    history = get_history()
    total_count = get_history_count()
    commands = parse_commands(history, args.keep_sudo)
    most_common_commands, least_common_count = get_most_common_commands(
        commands, n=args.top_count
    )

    print(f"Total history records: {total_count}")
    print("Most common commands:")
    for i, (command, count) in enumerate(most_common_commands):
        print(f"{i + 1}. {command}: {count} ({count / total_count:.1%})")
    print(
        f"Least common commands count: {least_common_count} ({least_common_count / total_count:.1%})"
    )


if __name__ == "__main__":
    main()
