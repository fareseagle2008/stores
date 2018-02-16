class MemberStore:
	members = []

	def get_all(self):
		if len(MemberStore.members) > 0:
			for member in MemberStore.members:
				print(member)
		else:
			print("There aren't any member in store")



		
	def add(self, member):
		if MemberStore().entity_exists(member):
			print("this user is already exists")
		else:
			memberList = [member.id, member.name, member.age]
			MemberStore.members.append(memberList)
	    

	def get_by_id(self, id):
		i = 0
		while i < len(MemberStore.members):
			if MemberStore.members[i][0] == id:
				return MemberStore.members[i]
			i +=1
	
	def entity_exists(self, member):
		member = [member.id, member.name, member.age]
		if member in MemberStore.members:
			return True
		else:
			return False

	# def update(self, member, member1):
	# 	member = [member.id, member.name, member.age]
	# 	member1 = [member1.id, member1.name, member1.age]
	# 	if member in MemberStore.members:
	# 		i = MemberStore.members.index(member)
	# 		MemberStore.members.remove(member)
	# 		MemberStore.members.insert(i, member1)

	def delete(self, member):
		member = [member.id, member.name, member.age]
		if member in MemberStore.members:
			MemberStore.members.remove(member)
		else:
			print("this member doesn't exist")




class PostStore:
	posts = []

	def get_all(self):
		if len(PostStore.posts) > 0:
			for post in PostStore.posts:
				print(post)


	def add(self, post):
		if PostStore().entity_exists(post):
			print("this post is already exists")
		else:
			postlist = [post.title, post.body]
			PostStore.posts.append(postlist)

	def delete(self, post):
		post = [post.title, post.body]
		if post in PostStore.posts:
			PostStore.posts.remove(post)
		else:
			print("this post doesn't exist")

	def entity_exists(self, post):
		post = [post.title, post.body]
		if post in PostStore.posts:
			return True
		else:
			return False
		


		
