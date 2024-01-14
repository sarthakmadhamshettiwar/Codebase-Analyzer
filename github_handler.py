# Extracts code from github, with a given username, repository name and filename.
def codeExtractor(oAuth_token, userName, repoName, fileName):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {oAuth_token}',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    response = requests.get(f'https://api.github.com/repos/{userName}/{repoName}/contents/{fileName}', headers=headers)
    encoded_code = response.json()['content'] # in 64 bit encoding
    decoded_code = base64.b64decode(encoded_code).decode('utf-8')
    
    return decoded_code


# get_SHA will get SHA of the file mentioned.
def get_SHA(oAuth_token, ownerName, repoName, fileName):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + oAuth_token,
        'X-GitHub-Api-Version': '2022-11-28',
    }

    response = requests.get(f'https://api.github.com/repos/{ownerName}/{repoName}/contents/{fileName}', headers=headers)
    my_dict = literal_eval(response.content.decode('utf-8'))
    return my_dict['sha']



# SHA of a file always changes after the commit.
# Will commit the code to the github account, assumes that the updated code is present in base64 encoding.
def code_commiter(updated_code, oAuth_token, ownerName, repoName, fileName):
    url = f"https://api.github.com/repos/{ownerName}/{repoName}/contents/{fileName}"
    
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/vnd.github+json"
    headers["Authorization"] = f"Bearer {oAuth_token}"
    headers["X-GitHub-Api-Version"] = "2022-11-28"
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    # Extract SHA when downloading the file for the first time itself.
    # Remember to update the SHA.
    sha = get_SHA(oAuth_token, ownerName, repoName, fileName)
    
    # print(sha)
    
    data = """
    {"message":"Simple Commit For trying REST API.",
      "committer":{"name":"Sarthak Madhamshettiwar","email":"sarthakmadhamshettiwar@gmail.com"},
      "sha":""" + f'"{sha}"' + """, 
      "content":"aGVsbG8gd29ybGQ="}
    """
    # print(data)
    resp = requests.put(url, headers=headers, data=data)
    if(resp.status_code == 200):
        print('Code updated !')
    
    else:
        print(f'Error {resp.status_code}')

  
