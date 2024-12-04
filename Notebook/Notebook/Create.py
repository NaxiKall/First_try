def create():

    print("Enter note ", end="")
    note = input()
    cur.execute("INSERT INTO daily(note,id) VALUES(?,?)",
                (note, aidi,))
    con.commit()