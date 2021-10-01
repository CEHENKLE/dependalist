from github import Github
import os
import yaml

token = os.getenv('GITHUB_TOKEN', '...')
g = Github(token)

#overwrite this to whatever org you care about

my_org = "OpenSearch-project"
org = g.get_organization(my_org)

dict = {'updates': [], 'version': 2}

repo = org.get_repo("cross-cluster-replication")
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    elif (file_content.name == "build.gradle" and file_content.name =='build.gradle'):
        if (file_content.name == "build.gradle" and file_content.name =='build.gradle'):
            dict['updates'].append({'directory': '/', 'open-pull-request-limit':0, 'package-ecosytem': 'gradle', 'schedule':{'interval': 'weekly'}})
        else:
            dict['updates'].append({'directory': file_content.path, 'open-pull-request-limit':0, 'package-ecosytem': 'gradle', 'schedule':{'interval': 'weekly'}})

with open('dependabot.yml', 'w') as f:
    data = yaml.dump(dict, f, sort_keys=False, default_flow_style=False)
