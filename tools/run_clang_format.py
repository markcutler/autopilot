#!/usr/bin/python3

import click
import os
import tempfile
import filecmp
import shutil
import difflib
import sys

import git

import shell_utils

SOURCE_EXTENSIONS = [".cpp", ".c", ".cxx", ".cc", ".h", ".hxx", ".hpp"]


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Symbols:
    PASS = u'\u2714'
    FAIL = u'\u2718'


def get_source_files_in_dir(directory):
    source_files = [os.path.join(d, f)
                    for d, dirs, files in os.walk(directory)
                    for f in files if f.lower().endswith(tuple(SOURCE_EXTENSIONS))]
    return source_files


@click.command()
@click.option('-f', '--fix-in-place', default=False, is_flag=True, help='Fix the issues found.')
@click.option('-m', '--modified-files', default=False, is_flag=True, help='Check modified files (according to git) '
                                                                          'only.')
@click.option('-v', '--verbose', default=False, is_flag=True, help="Print all the errors found.")
def main(fix_in_place, modified_files, verbose):
    # change directory to the root of the git project
    repo = git.Repo('.', search_parent_directories=True)
    os.chdir(repo.working_tree_dir)

    if modified_files:
        # TODO: fill in
        pass
    else:
        sources_to_check = get_source_files_in_dir(repo.working_tree_dir)

    num_failed_files = 0

    for file in sources_to_check:
        # format the file with clang-format and save the output to a temporary file
        output = shell_utils.run_output_list("clang-format -style=file -fallback-style=none " + file)
        formatted_file = tempfile.NamedTemporaryFile()
        formatted_file.write(output)
        formatted_file.seek(0)

        # check if the formatted file is different from the original
        file_changed = not filecmp.cmp(formatted_file.name, file)

        # Only need to handle those files that were changed by clang-format. Files that weren't changed are good to go.
        if file_changed:
            num_failed_files += 1
            print(Colors.RED + Symbols.FAIL + Colors.END + " " + str(file))
            if verbose:
                # get and display the diff between the original and formatted files
                original_file = open(file, 'r')
                new_file = open(formatted_file.name, 'r')
                diff = difflib.unified_diff(original_file.readlines(), new_file.readlines())
                print(Colors.CYAN)
                for line in diff:
                    sys.stdout.write(line)
                print(Colors.END)
            if fix_in_place:
                # if we are fixing in place, just replace the original file with the changed contents
                print(Colors.YELLOW + "WARNING: Fixing in place. Original file will be changed." + Colors.END)
                shutil.move(formatted_file.name, file)
        else:
            print(Colors.GREEN + Symbols.PASS + Colors.END + " " + str(file))

        # clean up
        try:
            formatted_file.close()
        except FileNotFoundError as _:
            # Do nothing. We must have moved the file above
            pass

    if num_failed_files:
        print(Colors.RED + 3*Symbols.FAIL + " " + str(num_failed_files) + " files have formatting errors." + Colors.END)
        if fix_in_place:
            print("The formatting errors have been automatically fixed.")
        sys.exit(1)

    print(Colors.GREEN + 3*Symbols.PASS + Colors.END + " No files have formatting errors!")
    sys.exit(0)


if __name__ == '__main__':
    main()
