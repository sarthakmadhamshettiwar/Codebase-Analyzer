import base64
'''
1. encoder(): takes English text as input and returns base64 encoded output in string format, instead of byte format.
Similar to https://www.base64encode.org/

2. Github_Operator: takes a Github OAuthToken, Username, Repository Name, filename which you want to analyze while creating object.
extract() method returns the data present in filename in English (automatically decoded from base64 encoding).
commit(code): will update the the contents of 'filename' with 'code', expect 'code' to be already encoded in base64 encoding. For doing that encoder() method
will be used.
'''

def encoder(text):
    my_bytes = code.encode('utf-8')
    updated_string = base64.b64encode(my_bytes)
    s = str(updated_string)
    return s[2:-1]
      
       
class Github_Operator:
    def __init__(self, token, userName, repoName, fileName):
        self.token = token
        self.user = userName
        self.repo = repoName
        self.file = fileName
        self.sha = 'NULL'
    def extract(self):
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {self.token}',
            'X-GitHub-Api-Version': '2022-11-28',
        }
        response = requests.get(
            f'https://api.github.com/repos/{self.user}/{self.repo}/contents/{self.file}',
            headers=headers)

        encoded_code = response.json()['content']  # in 64 bit encoding
        self.sha = response.json()['sha']
        decoded_code = base64.b64decode(encoded_code).decode('utf-8')
        self.decoded_code = decoded_code;
        return decoded_code

    def commit(self, code):
      # code will be in english, first we need to convert it into base 64 encoding
        url = f'https://api.github.com/repos/{self.user}/{self.repo}/contents/{self.file}'

        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/vnd.github+json"
        headers["Authorization"] = f"Bearer {self.token}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        # Replace single quotes with double quotes
        formatted_string = code.replace("'", '"')

        # Add double quotes around the entire string
        final_result = f'"{formatted_string}"'
        
        data = {"message":"my commit message","committer":{"name":"Monalisa Octocat","email":"octocat@github.com"},"content":final_result[1:-1], "sha":self.sha}
        data = json.dumps(data)

        # return data
        resp = requests.put(url, headers=headers, data=data)
        
        # print(resp)
        print(resp.status_code)
        
        if(resp.status_code == 200):
          resp = resp.json()
          self.sha = resp['content']['sha']
          # pass


operator = Github_Operator(oAuthToken, userName, repoName, fileName)
