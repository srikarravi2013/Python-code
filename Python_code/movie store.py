class MovieStore:

  def __init__(self):
    # Start with an empty list to keep track of movies
    self.movies = []

  def add(self, title):
    # Add a new movie to the store marking it as available by default
    self.movies.append({"title": title, "available": True})
    print(f"Added: {title}")

  def rent(self, idx):
    # Check if the movie index is valid and if it's currently available
    if 0 <= idx < len(self.movies) and self.movies[idx]["available"]:
      self.movies[idx]["available"] = False
      print(f"Rented: {self.movies[idx]['title']}")
    else:
      print("Cannot rent this movie.")

  def return_m(self, idx):
    # Check if the movie index is valid and if it's currently rented out
    if 0 <= idx < len(self.movies) and not self.movies[idx]["available"]:
      self.movies[idx]["available"] = True
      print(f"Returned: {self.movies[idx]['title']}")
    else:
      print("Cannot return this movie.")

  def show(self, available_only=False):
    print("\nMovies")
    for i, m in enumerate(self.movies):
      # Skip rented movies if we only want to see available ones
      if not available_only or m["available"]:
        status = "Available" if m["available"] else "Rented"
        print(f"{i + 1}. {m['title']} [{status}]")


# Command-line loop
store = MovieStore()
while True:
  print("\nMovie Store Menu: ")
  print("1. Add Movie")
  print("2. Rent")
  print("3. Return")
  print("4. Show All")
  print("5. Show Avaible")
  print("6. Exit")

  choice = input("Choice: ")

  # Add a new movie
  if choice == "1":
    store.add(input("Title: "))

  # Rent or return a movie (shows the list first so the user knows the numbers)
  elif choice in ("2", "3"):
    store.show()
    try:
      idx = int(input("Number: ")) - 1
      store.rent(idx) if choice == "2" else store.return_m(idx)
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Show all movies in the store
  elif choice == "4":
    store.show()

  # Show only the movies that are currently available to rent
  elif choice == "5":
    store.show(available_only=True)

  # Exit the program
  elif choice == "6":
    print("Goodbye!")
    break