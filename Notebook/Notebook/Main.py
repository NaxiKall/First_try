import sqlite3

DB_FILENAME = "Daily planner"
con = sqlite3.connect(DB_FILENAME)

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS daily(note TEXT, date TEXT DEFAULT (datetime('now', 'localtime')),importance TEXT DEFAULT 'Not important', status TEXT DEFAULT 'Not done',id INTEGER PRIMARY KEY)
""")
while True:

    def create():
        print("Enter note ", end="")
        note = input()
        cur.execute("INSERT INTO daily(note) VALUES(?)",
                    (note,))
        con.commit()

    def tabl():
        (cur.execute("select * from daily"))
        res = cur.fetchall()
        for row in res:
            note, date, importance, status, id = row
            print(f"#{id} {date}  {note} ({importance},  {status})")
    def tabl_u():
        cur.execute("select * from daily WHERE status = 'Not done'")
        res = cur.fetchall()
        for row in res:
            note, date, importance, status, id = row
            print(f"#{id} {date}  {note} ({importance},  {status})")
    def updt():
        id = input("Which one you want to update? ")
        cur.execute("UPDATE daily SET status  = 'Done' WHERE id = (?)",(id,))
        con.commit()


    def dlt():
        id = input("Which one you want to delete? ")
        cur.execute("DELETE FROM daily WHERE id = (?)", (id,))
        con.commit()

    print("What you want to do: ", end = "")
    job = input()
    job = job.lower().replace(" ","")

    match job:
        case "c":
            create()
            print("Note created")
        case "ta":
            tabl()
        case "tu":
            tabl_u()
        case "h":
            print("c - add a note \nta - print the table\ntu - print undone tasks\nd - delete a row\nu - update the status of row to done\ne - exit ")
        case "d":
            dlt()
        case "u":
            updt()
        case "e":
            break
        case _:
            print("Command not found")

