import click
import os
import glob
import tempfile

import git

import shell_utils

SOURCE_EXTENSIONS = [".cpp", ".c", ".cxx", ".cc", ".h", ".hxx", ".hpp"]



# output = shell_utils.run_shell_command("ls -l")
# print(output)


def get_source_files_in_dir(directory):

    source_files = [os.path.join(d, f)
                    for d, dirs, files in os.walk(directory)
                    for f in files if f.lower().endswith(tuple(SOURCE_EXTENSIONS))]
    return source_files


@click.command()
@click.option('-f', '--fix-in-place', default=False, help='Fix the issues found.')
@click.option('-m', '--modified-files', default=False, help='Check modified files (according to git) only.')
@click.option('-v', '--verbose', default=False, help="Print all the errors found.")
def main(fix_in_place, modified_files, verbose):
    # change directory to the root of the git project
    repo = git.Repo('.', search_parent_directories=True)
    os.chdir(repo.working_tree_dir)

    if modified_files:
        pass
    else:
        sources_to_check = get_source_files_in_dir(repo.working_tree_dir)

    print(sources_to_check)


    for file in sources_to_check:
        print("checking: " + file)

        output = shell_utils.run_output_list("clang-format -style=file -fallback-style=none " + file)
        fp = tempfile.TemporaryFile()
        fp.write(output)

        fp.seek(0)
        print(fp.read())

        fp.close()

        # print(output.decode('utf-8'))

        print("done checking")


        # save the output as a new file
        # compare the new file to the original
        # if they are the same, good. no errors.
        # if they are different, save the difference for printing
        # if we are fixing in place, replace the old file with the new file


if __name__ == '__main__':
    main()