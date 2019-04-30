import subprocess
import os
import click
from functools import partial
from pathlib import Path

if __name__ == '__main__':
    path = Path('../../requirements/')

    for file in os.listdir(path):
        with open("../../requirements/" + file, "r") as text:
            old_dependencies = text.read().split('\n')
            new_dependencies = []

            for line in old_dependencies:
                if line.find('=') and line != '' and line[:1] != '{' and line[:1] != '-' and line.find('git') == -1:
                    if line.find('[') > 0:
                        tool = line[0:line.find('[')]
                    else:
                        tool = line[0:line.find('=')]

                    try:
                        fresh_version = subprocess.check_output(
                            "pip list -o | grep -i " + tool,
                            shell=True).decode("utf-8")
                        fresh_version = fresh_version[31:fresh_version.
                                                      find(' ', 31)]
                        result = tool + '==' + fresh_version
                        fresh_version = []
                        fresh_version.append(result)
                    except subprocess.CalledProcessError:
                        try:
                            fresh_version = subprocess.check_output(
                                "pip list --format=freeze | grep " + tool,
                                shell=True).decode("utf-8").split(
                                    '\n')[:-1]
                        except:
                            pass
                    new_dependencies += fresh_version[:1]

        with open("../../requirements/" + file, "w") as text:
            for old_line in old_dependencies:
                if old_line == '':
                    text.write('\n')
                elif old_line[:1] != '{' and old_line[:1] != '-' and old_line.find('jinja2') == -1 and old_line.find('git') == -1:
                    old_tool = old_line[0:old_line.find('[')] if old_line.find('[') > 0 else old_line[0:old_line.find('=')]
                    for new_line in new_dependencies:
                        new_tool = new_line[0:new_line.find('=')]
                        if old_tool == new_tool:
                            text.write("%s\n" % new_line)
                            break
                else:
                    text.write("%s\n" % old_line)

    if old_dependencies is not new_dependencies:
        echo = partial(click.echo, err=True)
        echo(
            click.style(
                "Please rebuild your docker container with ",
                fg='bright_green') +
            click.style("'docker-compose up --build'", fg='bright_blue'))
