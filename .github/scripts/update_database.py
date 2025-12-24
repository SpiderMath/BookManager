import os
import csv

def main():
    issue_content = os.environ.get("ISSUE_BODY", "No content found")

    print(issue_content)

    try:
        with open("database.csv", mode="r", encoding="utf-8") as f:
            # f.write("Hello world")
            reader = csv.reader(f)
            for row in reader:
                print(row)
        print("Successfully wrote to database.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1) # This tells GitHub Actions the step failed

if __name__ == "__main__":
    main()
