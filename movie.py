movies_list = []

def add(movie):
    if movie.lower() not in (m.lower() for m in movies_list):
        movies_list.append(movie)
        print(f"'{movie}' added to the list.")
    else:
        print(f"'{movie}' is already in the list.")

def display_list():
    if not movies_list:
        print("Your list is empty.")
    else:
        print("Your movie list:")
        for movie in movies_list:
            print(f"> {movie}")

def check(movie):
    if movie.lower() in (m.lower() for m in movies_list):
        print(f"Yes, '{movie}' is on the list.")
    else:
        print(f"No, '{movie}' is not on the list.")

def remove(movie):
    if movie.lower() in (m.lower() for m in movies_list):
        movies_list.remove(movie)
        print(f"'{movie}' has been removed.")
    else:
        print(f"'{movie}' is not on the list.")

while True:
    print("\n1. Add a movie\n2. Display your list\n3. Check if a movie is on the list\n4. Remove a movie\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        movie_name = input("Enter the movie name: ")
        add(movie_name)
    elif choice == "2":
        display_list()
    elif choice == "3":
        movie_to_check = input("Enter the movie name to check: ")
        check(movie_to_check)
    elif choice == "4":
        movie_to_remove = input("Enter the movie name to remove: ")
        remove(movie_to_remove)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")