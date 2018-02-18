class MemberStore:
	members = []
	last_id = 1

	def get_all(self):
		return MemberStore.members

	
	def add(self, member):
		member.id = MemberStore.last_id
		MemberStore.members.append(member)
		self.last_id += 1
    

	def get_by_id(self, id):
		allMembers = self.get_all()
		result = None
		for member in allMembers:
			if member.id == id:
				result = member
				break
		return result

	def get_by_name(self, name):
		result = None
		for member in self.members:
			if member.name == name:
				result += member
		return result

	def entity_exists(self, member):
		result = True
		if self.get_by_id(member.id) is None:
			result = False
		return result


	def delete(self, id):
		member = MemberStore().get_by_id(id)
		MemberStore.members.remove(member)


	def update(self, member):
		result = member
		all_members = self.get_all()
		for index, current_member in enumerate(all_members):
			if current_member.id == member.id:
				all_members[index] = member
		return result





class PostStore:
	posts = []
	last_id = 1

	def get_all(self):
		return self.posts


	def add(self, post):
		post.id = PostStore.last_id
		self.posts.append(post)
		self.last_id += 1

	def get_by_id(self, id):
		allPost = self.get_all()
		result = None
		for post in allPost:
			if post.id == id:
				result = member
				break
		return result

	def delete(self, id):
		post = self.get_by_id(id)
		self.posts.remove(member)

	def entity_exists(self, post):
		result = True
		if self.get_by_id(post.id) is None:
			result = False
		return result

	def update(self, post):
		result = post
		allPosts = self.get_all()
		for index, current_post in enumerate(allPosts):
			if current_post.id == post.id:
				allPosts[index] = post
		return result
		


		
