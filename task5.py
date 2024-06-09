def display_monument(city):
    monuments = {
        "Delhi": "Red Fort",
        "Agra": "Taj Mahal",
        "Jaipur": "Jal Mahal"
    }
    
    if city in monuments:
        print(f"The monument of {city} is {monuments[city]}")
    else:
        print("Monument not found for the given city.")

def main():
    city = input("Enter a city: ")
    display_monument(city)

if __name__ == "__main__":
    main()
