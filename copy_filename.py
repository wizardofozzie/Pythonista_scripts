import clipboard, editor, console, os

def main():
    try:
        choice = console.alert("Copy what?", "Choose...", "File (full)", "File (~/Documents)", "Dir")
    except:
        choice = 1
    fn = editor.get_path()
    fn = fn[fn.find("/Documents"):] if choice == 2 else os.path.split(fn)[0][8:] if choice == 3 else fn[8:]
    clipboard.set(fn)

if __name__ == "__main__":
    main()
