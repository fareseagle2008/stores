import itertools

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
		return (member for member in self.get_all() if member.name == name)

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

	def get_member_with_post(self, all_posts):
		all_members = self.get_all()
		for member, post in itertools.product(all_members, all_posts):
			if member.id == post.member_id:
				member.posts.append(post)
		for member in all_members:
			yield member

	def get_top_two(self, all_posts):
		all_members = self.get_member_with_post(all_posts)
		sorted_members = sorted(all_members, key=lambda top: len(top.posts), reverse=True)
		return sorted_members[:2]





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
		


		
