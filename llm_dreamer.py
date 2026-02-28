from openai import OpenAI
import os

token = ""
with open("token.txt", "r") as file:
    token = file.read()
print(f"Look at that I have a token {token}")

if token == "" or token == "Put yo' token here.":
  print("Write your API token to token.txt, thank you")
  with open("token.txt", "w") as file:
     file.write("Put yo' token here.")
  quit()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=token,
)

def hallucionate(prompt):
  global client
  completion = client.chat.completions.create(
    extra_body={},
    model="arcee-ai/trinity-mini:free",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ]
  )
  return completion.choices[0].message.content   

print("Brainstorming ideas, please stand by...")

answer = hallucionate("Generate me 20 ideas for writing a single complex Python script that would do something funny. Just a bullet point list of ideas, nothing else.")
ideas = answer.splitlines()

def remove_first_last_lines(text):
    lines = text.splitlines()
    if len(lines) <= 2:
        return ""  # Return empty string if there are 2 or fewer lines
    return '\n'.join(lines[1:-1])

for idea in ideas:
  idea = idea.removeprefix("*")
  idea = idea.strip()
  if idea == "":
    continue
  print(f"Idea: {idea}")
  print("Generating code...")
  script_code = hallucionate(f'Make me a single Python script (using only standard libraries) that would implement the following idea: "{idea}". Just a Python code in text, nothing else needed.')
  script_code = remove_first_last_lines(script_code)
  print("Code generated.")
  print("Thinking about the script name...")
  script_name = hallucionate(f'Tell me how to call the file of the following Python script:\n{script_code}\n---\nJust a name for the Python script in text, nothing else needed. Follow the pattern like "mr_robot_script.py". Output the name with a file extension included.')
  script_name = script_name.strip()
  print(f"Script name is {script_name}")
  with open(f"generated_scripts/{script_name}", "w", encoding='utf-8') as file:
     file.write(script_code)
  print("Running a script!")
  os.system(f"python generated_scripts/{script_name}")
  
