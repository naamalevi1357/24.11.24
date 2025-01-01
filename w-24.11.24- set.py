# start

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a:
oscar_winners.add("Watson Emma")
print(oscar_winners)

# b:
rt=oscar_winners.copy()
print(rt)
oscar_winners.remove("Meryl Streep")
print(oscar_winners)
oscar_winners.clear()
print(oscar_winners)

# c:

print(titanic_actors & dark_knight_actors)
print(titanic_actors.intersection(dark_knight_actors))

# d:
print(iron_man_actors.isdisjoint(avengers_actors))

# e:
print(actor_list.issubset(oscar_winners))
print(actor_list<=oscar_winners)

# f:
print(actor_list.issuperset(avengers_actors))
print(actor_list>=avengers_actors)

# g:
print(movie_cast.pop())
print(movie_cast)

# h:
movie_cast.remove("Matt Damon")
print(movie_cast)

# i:
print(titanic_actors.difference(oscar_winners))
print(titanic_actors-oscar_winners)

# j:

print(titanic_actors.symmetric_difference(dark_knight_actors))
print(titanic_actors^dark_knight_actors)

# k:

print(oscar_winners)
oscar_winners.add("Lewis-Day Daniel")
oscar_winners.add("Blanchett Cate")
print(oscar_winners)

# j:

titanic_actors.update(dark_knight_actors)
print(titanic_actors)

print(titanic_actors | dark_knight_actors)

# עשיתי את הבונוס




























# stop