SELECT * FROM Follows JOIN People
    ON Follows.from_id = People.id WHERE People.id = 1