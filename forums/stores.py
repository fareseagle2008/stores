class MemberStore:
	members = []

	def get_all(self):
		if len(MemberStore.members) > 0:
			return MemberStore.members



		
	last_id = 1
	def add(self, member):
		if MemberStore().entity_exists(member):
			print("this user is already exists")
		else:
			member.id = MemberStore.last_id
			MemberStore.members.append(member)
			self.last_id += 1

		
	    

	def get_by_id(self, id):
		allMembers = self.get_all()
		for member in allMembers:
			if member.id == id:
				return member
			else:
				return
	
	def entity_exists(self, member):
		if member in self.members:
			return True
		else:
			return False


	def delete(self, id):
		member = MemberStore().get_by_id(id)
		MemberStore.members.remove(member)





class PostStore:
	posts = []
	last_id = 1

	def get_all(self):
		if len(self.posts) > 0:
			return self.posts


	def add(self, post):
		if PostStore().entity_exists(post):
			print("this post is already exists")
		else:
			post.id = PostStore.last_id
			self.posts.append(post)
			self.last_id += 1

	def get_by_id(self, id):
		allPosts = self.get_all()
		for post in allPosts:
			if post.id == id:
				return post
			else:
				return

	def delete(self, id):
		post = self.get_by_id(id)
		if post in self.posts:
			self.posts.remove(post)
		else:
			print("this posts doesn't exist")

	def entity_exists(self, post):
		post = [post.title, post.body]
		if post in self.posts:
			return True
		else:
			return False
		


		
