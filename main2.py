
import sys
import ruamel.yaml
from ruamel.yaml.comments import CommentedMap

def add_yaml():
    data = CommentedMap()
    data['a'] = 1
    data['b'] = 2
    data.yaml_set_start_comment('Hello\nWorld\n')
    return data


def main():
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.indent(sequence=3, offset=1)

    with open("docker-compose.yml", 'r') as ymlfile:
        data = yaml.load(ymlfile)
        print(len(data))
        print(data.mlget(['services']))
        print(data.mlget(['version']))
        a = CommentedMap()
        data["services"]["new"] = a
        data["services"]["new2"] = add_yaml()
        a.yaml_add_eol_comment('this is the name', 'boby', 11)
        a['age'] = 10
        a['age2'] = 10
        a.yaml_set_comment_before_after_key("age")
        a.yaml_add_eol_comment('in years', 'age', 11)
    yaml.dump(data, sys.stdout)

if __name__ == "__main__":
    main()