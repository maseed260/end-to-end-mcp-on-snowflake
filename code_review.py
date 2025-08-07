import os
import uuid
import snowflake.connector

# Read the contents of 'cortex_agents.py'
with open('cortex_agents.py', 'r') as file:
    code_to_review = file.read()

prompt = f"Please provide a detailed code review for the following Python file 'cortex_agents.py':\n{code_to_review}"

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
