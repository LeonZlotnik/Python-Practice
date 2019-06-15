
import csv

userMovie = input("What movie are you watching: ")
movieFound = False

with open('netflix_ratings.csv', 'r', newline='') as csvfile:
    movieList = csv.reader(csvfile, delimiter=',')
    
    for title in movieList:
        if userMovie in title:
            movieFound = True
            break
        
if movieFound:
    print(f"{title[0]} is rated {title[1]} with a rating {title[-2]} ")
else:
    print("Movie not found")


#El error aquí esta en el tipo de formato en el questa guardado el archivo CSV
#Hay que ver en que utf esta ??


