class Github_Operator:
    def __init__(self, oAuthToken, userName, repoName, fileName):
        self.oAuthToken = oAuthToken
        self.userName = userName
        self.repoName = repoName
        self.fileName = fileName

    def codeExtractor(self):
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {self.oAuthToken}',
            'X-GitHub-Api-Version': '2022-11-28',
        }
        response = requests.get(
            f'https://api.github.com/repos/{self.userName}/{self.repoName}/contents/{self.fileName}',
            headers=headers)
        encoded_code = response.json()['content']  # in 64 bit encoding
        decoded_code = base64.b64decode(encoded_code).decode('utf-8')
        self.decoded_code = decoded_code;
        return decoded_code

    def get_SHA(self):
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + self.oAuthToken,
            'X-GitHub-Api-Version': '2022-11-28',
        }
        response = requests.get(
            f'https://api.github.com/repos/{self.userName}/{self.repoName}/contents/{self.fileName}',
            headers=headers)
        my_dict = literal_eval(response.content.decode('utf-8'))
        return my_dict['sha']

    def codeCommiter(self, updated_code):
        url = f"https://api.github.com/repos/{self.userName}/{self.repoName}/contents/{self.fileName}"

        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/vnd.github+json"
        headers["Authorization"] = f"Bearer {self.oAuthToken}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        # Extract SHA when downloading the file for the first time itself.
        # Remember to update the SHA.
        sha = self.get_SHA(self.oAuthToken, self.ownerName, self.repoName, self.fileName)

        # print(sha)
        my_bytes = updated_code.encode('utf-8')
        updated_encoded_code = base64.b64encode(my_bytes)

        data = """
        {"message":"Simple Commit For trying REST API.",
          "committer":{"name":"Sarthak Madhamshettiwar","email":"sarthakmadhamshettiwar@gmail.com"},
          "sha":""" + f'"{sha}"' + """, 
          "content":""" + f'"{updated_encoded_code}"' + """}
        """
        # print(data)
        resp = requests.put(url, headers=headers, data=data)
        if (resp.status_code == 200):
            print('Code updated !')
        else:
            print(f'Error {resp.status_code}')
