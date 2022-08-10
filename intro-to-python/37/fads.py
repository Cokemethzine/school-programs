def emphasize_message(message):
    message = ""
    print("***" + message.upper() + "***")

def main():
    new_message = input("Enter the message you wish to emphasize with stars: ")
    emphasize_message(new_message)

if __name__ == "__main__":
    main()