# Re:Tether's Movie Streaming Site Generator

# Dictionary mapping movies to streaming platforms
movies_database = {
    "12 Angry Men": ["HBO Max", "Amazon Prime"],
    "2001: A Space Odyssey": ["Amazon Prime", "HBO Max"],
    "Schindler's List": ["HBO Max"],
    "The Shawshank Redemption" : ["HBO"],
    "The Godfather" : ['Amazon Prime Video' , 'Paramount+'],
    "The Godfather Part II" : ['Amazon Prime Video', 'Paramount+'],
    "The Dark Knight" : ['Amazon Prime Video', 'HBO Max'],
    "Pulp Fiction" : ['Paramount+'],
    "The Lord of the Rings: The Return of the King": ['HBO Max'],
    "127 Hours": ['Hulu', 'Paramount+'],
    "A Beautiful Mind": ['Amazon Prime Video', 'Paramount+'],
    "A Clockwork Orange": ['Amazon Prime Video', 'HBO Max'],
    "A History of Violence": ['Amazon Prime Video', 'HBO Max'],
    "Akira": ['Hulu'],
    "Alien": ['Hulu', 'Starz'],
    "All About Eve": ['Amazon Prime Video', 'Criterion Channel'],
    "American Beauty": ['Amazon Prime Video', 'Paramount+'],
    "American History X": ['Hulu', 'HBO Max'],
    "American Psycho": ['Amazon Prime Video', 'Paramount+'],
    "Anchorman: The Legend of Ron Burgundy": ['Amazon Prime Video', 'HBO Max'],
    "Annie Hall": ['Amazon Prime Video', 'HBO Max'],
    "Apocalypse Now": ['Amazon Prime Video', 'Criterion Channel'],
    "The Apartment": ['Amazon Prime Video', 'Criterion Channel'],
    "Apocalypto": ['Hulu', 'Amazon Prime Video (rent or purchase)'],
    "Ararat": ['Kanopy', 'Criterion Channel'],
    "The Artist": ['Amazon Prime Video', 'Hulu'],
    "Audition": ['Shudder'],
    "Au revoir les enfants (1987)": ['Amazon Prime Video (rent or purchase)'],
    "The Babadook": ['Shudder', 'Amazon Prime Video (rent or purchase)'],
    "Back to the Future": ['Netflix'],
    "The Bad and the Beautiful": ['Amazon Prime Video','Criterion Channel'],
    "Badlands ": ['Criterion Channel'],
    "The Bad Lieutenant: Port of Call New Orleans": ['Amazon Prime Video', 'HBO Max'],
    "Bad Santa": ['Hulu', 'Amazon Prime Video (rent or purchase)'],
    "BASEketball": ['Hulu', 'HBO Max'],
    "Batman": ['Amazon Prime Video', 'HBO Max'],
    "The Big Lebowski": ['Hulu', 'Amazon Prime Video (rent or purchase)'],
    "Birdman or (The Unexpected Virtue of Ignorance)": ['Hulu', 'Amazon Prime Video (rent or purchase)'],
    "Black Narcissus": ['Criterion Channel'],
    "Black Sheep": ['Hulu', 'Amazon Prime Video (rent or purchase)'],
    "Blade Runner": ['Amazon Prime Video', 'HBO Max'],
    "Blood Simple": ['Criterion Channel'],
    "Boogie Nights": ['Hulu'],
    "The Boyhood": ['Amazon Prime Video'],
    "The Breakfast Club": ['Amazon Prime Video', 'Paramount+'],
    "The Bridge on the River Kwai": ['Hulu', 'Criterion Channel'],
    "Brighton Rock": ['Criterion Channel'],
    "Bringing Up Baby": ['Criterion Channel'],
    "Brokeback Mountain": ['Amazon Prime Video'],
    "Casablanca": ['Amazon Prime Video', 'HBO Max'],
    "Close Encounters of the Third Kind": ['Amazon Prime Video, Hulu'],
    "The Coen brothers": ['Hulu'],
    "Crouching Tiger": ['Hidden Dragon, Hulu'],
    "The Crown": ['Netflix'],
    "Das Boot": ['Hulu, Criterion Channel'],
    "David Lean's Lawrence of Arabia": ['Amazon Prime Video, HBO Max'],
    "Dawn of the Dead":  ['Hulu, Criterion Channel'],
    "Days of Heaven": ['Criterion Channel'],
    "Dead Man": ['Hulu, Criterion Channel'],
    "The Dead": ['Criterion Channel'],
    "The Departed": ['HBO Max'],
    "Despicable Me": ['Peacock'],
    "Dial M for Murder": ['Amazon Prime Video, HBO Max'],
    "Die Hard": ['Hulu, Starz'],
    "The Dirty Dozen": ['Amazon Prime Video, HBO Max'],
    "Do the Right Thing": ['Amazon Prime Video, HBO Max'],
    "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb": ['Hulu, Criterion Channel'],
    "Django Unchained": ['Amazon Prime Video, HBO Max'],
    "The Silence of the Lambs":	['Amazon Prime Video, Paramount+'],
    "E.T. the Extra-Terrestrial": ['Amazon Prime Video'],
    "Easy Rider": ['Amazon Prime Video, Criterion Channel'],
    "Edge of Darkness": ['Amazon Prime Video, Paramount+'],
    "The Elephant Man":	['Amazon Prime Video, Criterion Channel'],
    "Eraserhead": ['HBO Max'],
    "Eternal Sunshine of the Spotless Mind": ['Hulu'],
    "The Exorcist": ['Hulu, HBO Max'],
    "The Fabelmans": ['Amazon Prime Video, Universal Pictures Home Entertainment'],
    "The Fall":	['Amazon Prime Video, Criterion Channel'],
    "Falling for a Dancer": ['AMC+, Amazon Prime Video, FuboTV, Spectrum on Demand'],
    "The 400 Blows": ['Criterion Channel'],
    "Full Metal Jacket": ['Amazon Prime Video, HBO Max'],
    "The General": ['Amazon Prime Video, Criterion Channel'],
    "Ghostbusters": ['Amazon Prime Video'],
    "Gladiator": ['Paramount+'],
    "Good Will Hunting": ['Amazon Prime Video, Paramount+'],
    "The Good, the Bad and the Ugly": ['Amazon Prime Video, HBO Max'],
    "The Graduate Amazon Prime Video": ['Criterion Channel'],
    "Gravity": ['HBO Max'],
    "Heat": ['Amazon Prime Video, HBO Max'],
    "Hell or High Water": ['Netflix']
    
    # Add more movies and streaming platforms as needed
}

def find_movie_streaming_platforms(movie_name):
    platforms = movies_database.get(movie_name, [])
    if platforms:
        return platforms
    else:
        return ["Movie not found on any streaming platforms."]

# Get user input for the movie name
print("WELCOME TO FILMVOYANT BY TETHER")
print("Reminder: This program is case sensitive, please type your movie of your choice correctly. Thank you for your cooperation!")

movie_name = input("\nEnter the movie name (ex: The Shawshank Redemption): ")
result = find_movie_streaming_platforms(movie_name)

# Display the streaming platforms
print("\nStreaming platforms for \"{}\": {}".format(movie_name, ', '.join(result)))
