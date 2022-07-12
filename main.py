
import sys
import ruamel.yaml
from akashpose.helper import traverse
from akashpose.compose2akash import transform


def main():
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.indent(sequence=3, offset=1)

    with open("docker-compose.yml", 'r') as ymlfile:
        data = yaml.load(ymlfile)
        #for p, v in traverse(data, []):
            #print(p,v, type(v))
        akash = transform(data)
    yaml.dump(akash, sys.stdout)

if __name__ == "__main__":
    main()