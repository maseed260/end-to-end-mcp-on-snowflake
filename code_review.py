import os
import snowflake.connector

# Read the code diff from file
with open('diff.patch', 'r') as file:
    code_diff = file.read()

prompt = f"Please provide a detailed code review for the following diff:\n{code_diff}"

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.environ['SNOWFLAKE_USER'],
    password=os.environ['SNOWFLAKE_PASSWORD'],
    account=os.environ['SNOWFLAKE_ACCOUNT'],
    warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
    database=os.environ['SNOWFLAKE_DATABASE'],
    schema=os.environ['SNOWFLAKE_SCHEMA']
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
with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_out:
    gh_out.write(f"review={review}\n")
