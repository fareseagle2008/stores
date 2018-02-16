import models
import stores

member1 = models.Member(1,"Fares AbuAmin", 31)
member2 = models.Member(2, "Lama Kheir", 30)
member3 = models.Member(3, "Ali Silan", 28)

post1 = models.Post('HEDONIST ROOTS', 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit,')
post2 = models.Post("LOREM IPSUM IN THE NEWS", "Five centuries later Lorem Ipsum experienced a surge in popularity with the release of Letraset's dry-transfer sheets.")
post3 = models.Post("FROM PRINT TO DESKTOP TO WEB", "Aldus Corporation, which later merged with Adobe Systems, helped bring Lorem Ipsum into the information age with its 1985 flagship software Aldus PageMaker. ")


print("====================Members Operations====================")
member_store = stores.MemberStore()

member_store.add(member1)
member_store.add(member2)



member_store.get_all()

print("=====================================")
member_store.add(member1)
print("=====================================")
print(member_store.get_by_id(1))
print("=====================================")

print(member_store.get_by_id(2))
print("=====================================")
member_store.delete(member1)

print(member_store.get_all())


print("====================Posts Operations====================")

post_store = stores.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

post_store.get_all()

print("=====================================")
post_store.add(post2)
print("========================================================")
post_store.delete(post1)
post_store.get_all()

