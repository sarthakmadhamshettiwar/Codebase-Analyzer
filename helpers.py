import requests
import base64


# Do the indentation and check are there any compilation error or not, if there are correct them.
def structure_checker(decoded_code):
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
        prompt_template.format(code = decoded_code)
    ]
    code = model.generate_content(prompt_parts)
    return code.text


# Analyze time and space complexity of the code
def time_space_complexity_analyzer(code, depth):
    prompt_template = PromptTemplate.from_template(
        '''
        Find the time and space complexity of the following code. Answer in two points. First point should contain the exact 
        time and space complexity without any explaination. While second point should contain the {depth} explaination. 
        {code}.
        '''
    )

    # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
    prompt_parts = [
        prompt_template.format(code=code, depth=depth)
    ]
    response = model.generate_content(prompt_parts)
    return response.text


# Possible optimization approaches:
'''
DSA Based: Dynamic Programming, Segment Trees, Binary Search instead of Linear Search, Precomputation, Binary Exponentiation
SOFTWARE Based: API Caching
'''
def optimization_advisor(overview, code):
    prompt_template = PromptTemplate.from_template(
        '''
        Given the brief overview of problem and its solution code. Try to optimize the code using methods like Dynamic Programming, 
        Segment Trees, Binary Search instead of Linear Search, any 1D or 2D Precomputation or Binary Exponentiation to reduce time 
        complexity. Also try to reduce space complexity by changing the data structure, ex: Using adjacency list instead of 
        adjacency matrix and etc. Output the correct code and nothing more. 
        Overview: {overview}
        Code: {code}
        '''
    )

    # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
    prompt_parts = [
        prompt_template.format(overview=overview, code=code)
    ]
    optimized_code = model.generate_content(prompt_parts)
    return optimized_code.text


# Software Engineering Principles Checker
'''
Will take care of KISS, DRY, YAGNI, Privacy, some more OOPs concept.
'''
def principles_analyzer(code):
    prompt_template = PromptTemplate.from_template(
        '''
        Update the above code in such a way that it follows KISS, DRY, YAGNI Principles. Also take care of abstraction and 
        not to make any critical attributes or methods public. If similar sequence of operations are performed, make a 
        new function for operation to suit DRY principle. Output the correct code and nothing more. Don't enclose 
        code with backticks. 
        Code: {code}
        '''
    )

    # Modify this to generate content about any topic in any number of words. Level bhi choose kar sakte khud se.
    prompt_parts = [
        prompt_template.format(code=code)
    ]
    modified_code = model.generate_content(prompt_parts)
    return modified_code.text
