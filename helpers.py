import requests
import base64

class Auxilary_Functions:
    def __init__(self, model):
        self.model = model

    def structure_checker(self, decoded_code):
        '''
        :return: Do the indentation and check are there any compilation error or not, if there are correct them and return it.
        '''
        prompt_template = PromptTemplate.from_template(
            '''
            Indent the code properly depending upon the language. Also correct any syntax error if present, for now ignore any logical
            logical error. Just focus on syntax. Output the correct code and nothing more. 
            {code}. 
            Dont even write the language at the top.
            '''
        )

        # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
        prompt_parts = [
            prompt_template.format(code=decoded_code)
        ]
        code = self.model.generate_content(prompt_parts)
        return code.text

    def code_explainer(self, code, length):
        '''
            :param code: input code which user want to understand, by-default it will be the file we are currently working analyzing.
            :param length: number of words in the explanation of code.
            :return: explanation of code in about #length words.
            '''
        prompt_template = PromptTemplate.from_template(
            '''Please explain the following code in around {length} words. 
            Code: {code}.
            Don't compromise quality of explanation for number of words restriction.
            '''
        )

        # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
        prompt_parts = [
            prompt_template.format(code=code, length=length)
        ]
        response = self.model.generate_content(prompt_parts)
        return response.text


class CodeAnalyzer:
    def __init__(self, model, oAuthToken, userName, repoName, fileName, length=75):
        github_operator = Github_Operator(oAuthToken, userName, repoName, fileName)
        self.model = model
        self.decoded_code = github_operator.codeExtractor()
        self.Aux = Auxilary_Functions(model)
        self.code = self.Aux.structure_checker(self.decoded_code)
        self.length = length
        self.description = self.Aux.code_explainer(self.code, self.length)


    def time_space_complexity_analyzer(self):
      prompt_template = PromptTemplate.from_template(
          '''
          Find the time and space complexity of the following code. Answer in two points. First point should contain the exact 
          time and space complexity without any explaination. While second point should contain the brief explaination of calculation of time and space complexity. 
          {code}.
          '''
      )

      # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
      prompt_parts = [
          prompt_template.format(code=self.code)
      ]
      response = model.generate_content(prompt_parts)
      return response.text


    # Work is needed: Access the file we are currently working on, either remove.
    def optimization_advisor(self):
        '''
        :param description: A brief overview of the code.
        :param code: Code, which is going to be optimized.
        :return: Optimized code.
        '''
        prompt_template = PromptTemplate.from_template(
            '''
            Given the brief description of problem and its solution code. Try to optimize the code using methods like Dynamic Programming, 
            Segment Trees, Binary Search instead of Linear Search, any 1D or 2D Precomputation or Binary Exponentiation to reduce time 
            complexity. Also try to reduce space complexity by changing the data structure, ex: Using adjacency list instead of 
            adjacency matrix and etc. Output the optimized code brief overview of the changes done.\. 
            Description: {description}
            Code: {code}
            '''
        )
        # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
        prompt_parts = [
            prompt_template.format(description=self.description, code=self.code)
        ]
        optimized_code = self.model.generate_content(prompt_parts)
        return optimized_code.text

    def principles_analyzer(self):
        '''
        :param description: brief overview of the code.
        :param code: code, which we want to improve
        :return: Will take care of KISS, DRY, YAGNI, Privacy, some more OOPs concept and return improved code.
        '''
        prompt_template = PromptTemplate.from_template(
            '''
            Given the brief description and the code, update the above code in such a way that it follows KISS, DRY, YAGNI Principles. 
            Also take care of abstraction and 
            not to make any critical attributes or methods public. If similar sequence of operations are performed, make a 
            new function for operation to suit DRY principle. Output the correct code and nothing more. Don't enclose 
            code with backticks. 
            Description: {description}
            Code: {code}
            '''
        )

        # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
        prompt_parts = [
            prompt_template.format(code=self.code, description=self.description)
        ]
        modified_code = self.model.generate_content(prompt_parts)
        return modified_code.text

    def bug_analyzer(self):
        '''
        :param description: brief overview of the code.
        :param code: code, which we want to improve
        :return: Will identify the possible bugs, like runtime or logic errors including infinite loops, etc.
        '''
        prompt_template = PromptTemplate.from_template(
            '''
            Given small description of problem and code written, check for logic errors and runtime errors. 
            Runtimer erros include: out-of-bound error (accessing element that doesn't exist), integer overflow error, 
            division by zero, trying to dereference NULL pointer, etc.
            Logic errors: flawed logic, incorrect algorithmic implementation, early or delayed termination of recurssion or loops 
            leading to infinite loops, etc. 
            Pinpoint bugs with possible solutions or preventive measures. Only bugs and solutions are needed. No need for new code.
            If you think code doesn't have any bugs print 'CORRECT CODE', or if you are not sure, then say so. 
            Don't give wrong points please.
            Description: {description}
            Code: {code}
            ALERT: Don't write updated code !!!
            '''
        )

        # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
        prompt_parts = [
            prompt_template.format(description=self.description, code=self.code)
        ]
        bugs = self.model.generate_content(prompt_parts)
        return bugs.text

    def testCase_generator(self, testcase):
        '''
        :param testcase: some sample testcases along with their input.
        '''
        prompt_template = PromptTemplate.from_template(
            '''
            Given code and the description, generate stronger test cases for the given code. Some test cases are already given.
            Code: {code}.

            Below testcases are in the format: 
            'Input': .....
            'Output': .....
            Testcases: {testcase}

            Generate few strong input cases and expected output.
            '''
        )

        # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
        prompt_parts = [
            prompt_template.format(testcase=testcase, code=self.code)
        ]
        testcases = self.model.generate_content(prompt_parts)
        return testcases.text
