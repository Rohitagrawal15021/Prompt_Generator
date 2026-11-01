from database.store import conn, insert_event

insert_event(
    "Chrome",
    "TCP Congestion PDF",
    "Studying slow start and congestion avoidance"
)

insert_event(
    "YouTube",
    "Computer Networks Lecture",
    "Learning TCP congestion control"
)

insert_event(
    "VS Code",
    "main.py",
    "Writing Python simulation for TCP"
)

conn.close()

