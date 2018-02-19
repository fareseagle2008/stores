import models
import stores

def create_members():
	member1 = models.Member("Fares AbuAmin", 31)
	member2 = models.Member( "Lama Kheir", 30)
	member3 = models.Member("Ali Silan", 28)
	print(member1)
	print(member2)
	print(member3)
	print("=" * 40)

	return member1, member2, member3

def store_should_add_model(member_instance, member_store):
	for Member in member_instance:
		member_store.add(Member)

def print_all_members(member_store):
	print("=" * 40)
	for Member in member_store.get_all():
		print(Member)
	print("=" * 40)

def stores_similar():
	member_store1 = stores.MemberStore()
	member_store2 = stores.MemberStore()
	if member_store1.get_all() is member_store2.get_all():
		print("same stores")

def same_retrieved_objects(member_store, member):
	member_retrieved = member_store.get_by_id(member.id)
	if member is member_retrieved:
		print("tow members matching")
def update_object(member_store, member):
	member_copy = models.Member(member.name, member.age)
	member_copy.id = 2
	if member_copy is not member:
		print("member and member_copy are not the same")
	print(member_copy)
	member_copy.name = "Wafaa"
	member_store.update(member_copy)
	print(member_store.get_by_id(member.id))

def deleteing():
	try:
		member_store.delete(1)
	except ValueError:
		print("It should be an existence entity before deleting !")


member_instance = create_members()
member1, member2, member3 = member_instance
member_store = stores.MemberStore()
store_should_add_model(member_instance, member_store)
stores_similar()
print_all_members(member_store)
same_retrieved_objects(member_store, member2)
print(member_store.get_by_name("Lama Kheir"))
update_object(member_store, member2)
deleteing()


