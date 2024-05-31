## RegEx
In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings. 

<p>This RegEx module provides several functions for working with regular expressions, including
<code>search, split, findall,</code> and <code>sub</code>. 
Python provides a built-in module called <code>re</code>, which allows you to work with regular expressions. </p>

---
First, import the **re module**

<code>import re</code>

The search() function searches for specified patterns within a string. Here is an example that explains how to use the search() function to search for the word "Jackson" in the string "Michael Jackson is the best".

<code>s1 = "Michael Jackson is the best"</code>

# Define the pattern to search for

<code>pattern = "Marie"</code>

# Use the search() function to search for the pattern in the string
<code>result = re.search(pattern, s1)</code>

# Check if a match was found
<code>if result:
    print("Match found!")
else:
    print("Match not found.")
</code>
