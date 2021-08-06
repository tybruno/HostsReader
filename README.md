# hosts_reader
Read a list of hosts from a .txt file or a string.
#### Key Features:
* **Easy**: Designed to easily retrieve a list of hosts from a file or string.
* **There is More!!!**: 
    * [commands_reader](https://github.com/tybruno/commands_reader): Read commands from a file or string.
    * [text_file_reader](https://github.com/tybruno/text_file_reader): Library that makes reading text files easy.
    * [file_reader](https://github.com/tybruno/file_reader): Created an abstraction for reading multiple types of files that hosts_reader, commands_reader, and text_file_reader inherit from.
### Usage
#### File example
hosts.txt
```text
host1, host2 , host3
```
hosts2.txt
```text
host1
host2
host3
```

```python
from hosts_reader import HostsFileReader

hosts_file = "hosts2.txt"

read_hosts_file = HostsFileReader()

hosts = read_hosts_file(hosts_file)

print(tuple(hosts)) # ('host1', 'host2', 'host3')
```
#### String Example
```python
from hosts_reader import HostsParser

hosts_str = "host1, host2, host3"

parse_hosts = HostsParser()

hosts = parse_hosts(hosts_str)

print(list(hosts)) # ['host1', 'host2', 'host3']
```

### Road Map
* Add support for excel files
* Add support for csv files
