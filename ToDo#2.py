#Rachel Bullock
#To do List
#1/10/2024

#clears all items from the list
#print the number of items that are in the list
#sort list in aplhabetical order

#Init
movies = []

#Functions
def movieList():
     print("Please choose an option: (Type in a number between 1 and 6)")
     print("1. Add to the list \n2. View List \n3. Mark Movie As Watched \n4. Remove Movie \n5. Clear all of the list \n6. Print number of items \n7. sort list aplhabeticaly \n8. Exit")
     option = int(input("Option: "))
     if option == 1:
        movie =input("What movie do you want to add?")
        movies.insert(0, movie)
        movieList()
     elif option == 2:
        print(movies)
        movieList()
     elif option == 3:
        movie = input("What movie have you watched?")
        number = input("Input postion on list- first item is position 0")
        movies[number] = "X" + movie
        movieList()
     elif option == 4:
        movie= input("What movie would you like to remove?")
        movies.remove(movie)
        movieList()
     elif option == 5:
        movies.clear()
        print(movies)
        movieList()
     elif option == 6:
        print(len(movies))
        movieList()
     elif option == 7:
        sortedList = sorted(movies)
        print(sortedList)
        movieList()
     elif option == 8:
        quit()
    

#Main
movieList()