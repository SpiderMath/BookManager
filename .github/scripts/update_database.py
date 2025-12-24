import os

def main():
    issue_content = os.environ.get("ISSUE_BODY", "No content found")

    print(issue_content)

    try:
        with open("database.csv", "w") as f:
            # f.write("Hello world")
            print("I could write to the DB but I won't rn")
        print("Successfully wrote to database.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1) # This tells GitHub Actions the step failed

if __name__ == "__main__":
    main()
