import os
import uuid
import snowflake.connector

# Read the contents of 'cortex_agents.py'
with open('cortex_agents.py', 'r') as file:
    code_to_review = file.read()

prompt = f"""
You are an expert Python code reviewer with experience in production systems, security, and best practices.

I am sharing the full contents of a Python source file named 'cortex_agents.py'. Please analyze it and provide a comprehensive, structured code review using the following format for each of the categories below:

For each category (1-9), do all of the following:
- Give a brief assessment of how well the code performs in that area
- **Rate the code on a scale from 1 (Poor) to 5 (Excellent)**
- **List specific strengths**
- **List concrete weaknesses or areas for improvement**
- **Suggest detailed improvements or refactorings** (with code snippets where helpful)

Categories:

1. **Summary of the File:** Brief explanation of what the file does.
2. **Correctness**
3. **Security**
4. **Performance**
5. **Clarity & Readability**
6. **Python Best Practices**
7. **Testability & Robustness**
8. **Actionable Suggestions**
9. **Potential Enhancements**

After the category-by-category review:
- Provide a final summary **overall rating** for the code (with explanation).

Respond in a clear, structured format using headings for each section and bullet points where appropriate.
Here is the file content to review:

{code_to_review}

"""

# Connect to Snowflake
conn = snowflake.connector.connect(
    user="ilyas",
    password="IlyasMaseed@260",
    account="TVNZMTQ-XCA13477",
    warehouse="COMPUTE_WH",
    database="DEMO",
    schema="PUBLIC"
)

cs = conn.cursor()
query = f"""
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'snowflake-arctic', %s
) AS REVIEW_RESULT
"""
cs.execute(query, (prompt,))
review = cs.fetchone()[0]
print(review)
# Save review as a GitHub Action output if needed
delimiter = str(uuid.uuid4())

with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_out:
    gh_out.write(f'review<<{delimiter}\n')
    gh_out.write(f'{review}\n')
    gh_out.write(f'{delimiter}\n')
