
import sys
import ruamel.yaml

def main():
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.indent(sequence=3, offset=1)

    with open("docker-compose.yml", 'r') as ymlfile:
        data = yaml.load(ymlfile)
        print(len(data))
    yaml.dump(data, sys.stdout)

if __name__ == "__main__":
    main()