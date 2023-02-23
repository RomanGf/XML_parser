import re


def read_file(file_name: str) -> str:
   
    with open(f'{file_name}', 'r') as f:
        xml_data = f.read()

    return concatenate_to_one_row(xml_data)

def concatenate_to_one_row(file_content: str) -> str:
    
    file_content = ''.join(file_content.split('\n'))
    file_content = ''.join(file_content.split())
    
    return file_content

def parse_xml(xml_string: str) -> dict:
    
    xml_string = concatenate_to_one_row(xml_string)
    
    root = {}
    stack = [(root, xml_string)]
    
    while stack:
        parent, xml_string = stack.pop()
        for match in re.finditer(r"<(\w+)>(.*?)</\1>", xml_string):
            tag, data = match.groups()

            if data == '':
                continue
            
            if "<" in data:
                parent[tag] = child = {}
                stack.append((child, data))
            elif tag in parent:
                parent[tag] = [parent[tag]]
                parent[tag].append(data)

            else:
                parent[tag] = data
    return root


if __name__ == '__main__':
    print(parse_xml(read_file('file.xml')))
