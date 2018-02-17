import models
import stores

member1 = models.Member("Fares AbuAmin", 31)
member2 = models.Member( "Lama Kheir", 30)
member3 = models.Member("Ali Silan", 28)

post1 = models.Post('HEDONIST ROOTS', 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit,')
post2 = models.Post("LOREM IPSUM IN THE NEWS", "Five centuries later Lorem Ipsum experienced a surge in popularity with the release of Letraset's dry-transfer sheets.")
post3 = models.Post("FROM PRINT TO DESKTOP TO WEB", "Aldus Corporation, which later merged with Adobe Systems, helped bring Lorem Ipsum into the information age with its 1985 flagship software Aldus PageMaker. ")


print("====================Members Operations====================")
member_store = stores.MemberStore()

member_store.add(member1)
member_store.add(member2)
member_store.add(member3)

seperate = "=" *40


print(member_store.get_all())

print(seperate)
member_store.add(member1)
print(seperate)
print(member_store.get_by_id(1))
print(seperate)

member_store.delete(1)

print(member_store.get_all())

print(seperate)
print(seperate)


print("====================Posts Operations====================")

post_store = stores.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print(post_store.get_all())
print(seperate)

print(post_store.get_by_id(1))

print(seperate)
post_store.add(post1)
print(seperate)
post_store.delete(1)
print(post_store.get_all())

