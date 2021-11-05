import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

registry = input("What is the FQDN of your docker registry?: ")

url1 = f'https://{registry}:30500/v2/_catalog'

r1 = requests.get(url1, verify=False).text

repos = json.loads(r1)

repo_list = repos['repositories']

print("\n Available respositories: \n")
print('\n'.join(map(str, repo_list)))

repo = input("Enter repo from the list above: ")

def repo_data(repo):
    if repo in repo_list:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        url2 = f'https://{registry}:30500/v2/{repo}/tags/list'
        r2 = requests.get(url2, verify=False).text
        repo_data = json.loads(r2)
        print("Image Name: " + str(repo_data['name']))
        print("Tag: " + str(repo_data['tags']))
    else:
        print("repo not found. Please try a different device")

repo_data(repo)
