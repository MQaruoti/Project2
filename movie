import streamlit as st
movies = {
    "Inception": {
        "Genres": ["Action", "Sci-Fi"],
        "Year": 2010,
        "Run Time": 148,
        "Rating": 8.8,
        "Actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"]
    },
    "Interstellar": {
        "Genres": ["Adventure", "Drama", "Sci-Fi"],
        "Year": 2014,
        "Run Time": 169,
        "Rating": 8.6,
        "Actors": ["Matthew McConaughey", "Anne Hathaway"]
    },
    "The Dark Knight": {
        "Genres": ["Action", "Crime", "Drama"],
        "Year": 2008,
        "Run Time": 152,
        "Rating": 9.0,
        "Actors": ["Christian Bale", "Heath Ledger"]
    },
    "Forrest Gump": {
        "Genres": ["Drama", "Romance"],
        "Year": 1994,
        "Run Time": 142,
        "Rating": 8.8,
        "Actors": ["Tom Hanks", "Robin Wright"]
    },
    "Pulp Fiction": {
        "Genres": ["Crime", "Drama"],
        "Year": 1994,
        "Run Time": 154,
        "Rating": 8.9,
        "Actors": ["John Travolta", "Uma Thurman"]
    },
    "Casablanca": {
        "Genres": ["Drama", "Romance", "War"],
        "Year": 1942,
        "Run Time": 102,
        "Rating": 8.5,
        "Actors": ["Humphrey Bogart", "Ingrid Bergman"]
    },
    "Gone with the Wind": {
        "Genres": ["Drama", "History", "Romance"],
        "Year": 1939,
        "Run Time": 238,
        "Rating": 8.1,
        "Actors": ["Clark Gable", "Vivien Leigh"]
    },
    "Psycho": {
        "Genres": ["Horror", "Mystery", "Thriller"],
        "Year": 1960,
        "Run Time": 109,
        "Rating": 8.5,
        "Actors": ["Anthony Perkins", "Janet Leigh"]
    },
    "Amélie": {
        "Genres": ["Comedy", "Romance"],
        "Year": 2001,
        "Run Time": 122,
        "Rating": 8.3,
        "Actors": ["Audrey Tautou", "Mathieu Kassovitz"]
    },
    "Spirited Away": {
        "Genres": ["Animation", "Adventure", "Family"],
        "Year": 2001,
        "Run Time": 125,
        "Rating": 8.6,
        "Actors": ["Rumi Hiiragi", "Miyu Irino"]}
}
def main():
    st.title("Movie Recomender App")
    
    menu = ["Recommend Movies", "Find a Movie", "Filter Movies", "Add Movie", "Exit"]
    choice = st.sidebar.selectbox("Choose an action:", menu)

    recommended=[]
    if choice == "Recommend Movies":
        genre = st.text_input("Enter Your Favorite Genre:")
        if st.button("Recommend"):
             for title,details in movies.items():
                 if genre in details["Genres"]:
                    recommended.append(title)
             if recommended:
                st.success(f"Based on your love for {genre}: {', '.join(recommended)}")
             else:
                st.error("No movies found for this genre. Try again.")

    elif choice == "Find a Movie":
        find = st.text_input("Enter a Movie to find:")
        if st.button("Find Movie"):
            found = False
            for title, details in movies.items():
                if find.lower() in title.lower():
                    st.info(f"Movie Found: {title}\nDetails: Year: {details['Year']}\nRun Time: {details['Run Time']} minutes\nRating: {details['Rating']}\nActors: {', '.join(details['Actors'])}")
                    found = True
                    break
            if not found:
                st.error("Movie not found. Please try another title.")

    elif choice == "Filter Movies":
        filter_by = st.radio("Filter by:", ('Rate', 'Year', 'Run Time'))
        if filter_by == 'Rate':
            rate = st.slider("Enter Rating:", 1.0, 10.0, 0.1)
            if st.button("Filter by Rating"):
                found = False
                for title, details in movies.items():
                    if rate == details['Rating']:
                        st.write(details['Rating'], title)
                        found = True
                if not found:
                    st.error("Did not find a movie with the same rating.")
        
        elif filter_by == 'Year':
            year = st.number_input("Enter Year of Movie:", min_value=1900, max_value=2023, step=1)
            if st.button("Filter by Year"):
                found = False
                for title, details in movies.items():
                    if year == details['Year']:
                        st.write(details['Year'], title)
                        found = True
                if not found:
                    st.error("Movie with this year wasn't found.")
        
        elif filter_by == 'Run Time':
            run_time = st.number_input("Enter minimum Run Time of Movie you want:", min_value=0, max_value=500, step=1)
            if st.button("Filter by Run Time"):
                found = False
                for title, details in movies.items():
                    if run_time <= details['Run Time']:
                        st.write(details['Run Time'], title)
                        found = True
                if not found:
                    st.error("Movie with this Run Time range wasn't found.")

    elif choice == "Add Movie":
        name = st.text_input("Enter the name of the movie to add:")
        genres = st.text_input("Enter genres separated by commas:")
        year = st.number_input("Enter the year:", min_value=1900, max_value=2023, step=1)
        run_time = st.number_input("Enter the run time:", min_value=0, max_value=500, step=1)
        rating = st.slider("Enter the rating (1-10):", 1.0, 10.0, 0.1)
        actors = st.text_input("Enter actors separated by commas:")
        if st.button("Add Movie"):
            if name not in movies:
                movies[name] = {"Genres": genres.split(','), "Year": year, "Run Time": run_time, "Rating": rating, "Actors": actors.split(',')}
                st.success(f"Movie '{name}' added!")
            else:
                st.error("Movie already exists.")

    elif choice == "Exit":
        st.stop()
