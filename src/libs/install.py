from pip._internal.cli.main import main
import subprocess
import json


def install(package):
    okay = main(['install', package])
    if okay == 0:
        cmd = f"pip freeze | grep {package}"
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        version = result.stdout.read().decode().replace('\n', '')
        with open('pyposer.json', 'r+') as f:
            data = json.load(f)
            data['dependencies'].update({package: version.split("==")[-1]})
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()