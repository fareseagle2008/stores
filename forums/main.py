import models

member1 = models.Member("Fares AbuAmin", 31)
member2 = models.Member("Lama Kheir", 30)

post1 = models.Post('HEDONIST ROOTS', 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit,')
post2 = models.Post("LOREM IPSUM IN THE NEWS", "Five centuries later Lorem Ipsum experienced a surge in popularity with the release of Letraset's dry-transfer sheets.")
post3 = models.Post("FROM PRINT TO DESKTOP TO WEB", "Aldus Corporation, which later merged with Adobe Systems, helped bring Lorem Ipsum into the information age with its 1985 flagship software Aldus PageMaker. ")

print(post1.body)
print(post2.title)
print(member1.name)