import os

def main():
    issue_content = os.environ.get("ISSUE_BODY", "No content found")

    # 2. Print it to the console (this shows up in your GitHub Actions logs)
    print("--- Issue Body Received ---")
    print(issue_content)
    print("---------------------------")

    # 3. Write "Hello world" to the database.csv file
    # 'w' will overwrite the file. Use 'a' if you want to append a new line.
    try:
        with open("database.csv", "w") as f:
            f.write("Hello world")
        print("Successfully wrote to database.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1) # This tells GitHub Actions the step failed

if __name__ == "__main__":
    main()
