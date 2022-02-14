def main():
    try:
        configuration = open('config.txt')
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    

if __name__ == '__main__':
    main()