file = open("/usercode/files/books.txt")
#your code goes here
def read_n_characters(file, n):
    try:
        # Read the first N characters
        content = file.read(n)
        # Print the content
        print(content)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file.close()
# Take the number of characters as input
n = int(input())
# Call the function to read the first N characters
read_n_characters(file, n)
