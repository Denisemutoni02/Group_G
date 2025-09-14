class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def display_profile(self):
        profile_info = (
            f"Name: {self.name}\n"
            f"Favorite Programming Language: {self.favorite_language}\n"
            f"Hobby: {self.hobby}\n"
            f"Tech Stack: {','.join(self.tech_stack)}\n"
            f"GitHub Username: {self.github_username}\n"
            f"Fun Fact: {self.fun_fact}\n"
        )
        return profile_info
    
  
    def introduce(self):
        return f"Hi, I'm {self.name}, Im very happy to meet you!"
    
    def show_stack(self):
        print(f"My tech stack includes:")
        for tools in self.tech_stack:
            print(f"- {tools}")

profile = Profile(
    name="Ocen Deo Lino",
    favorite_language="Python",
    hobby="Playing games",
    tech_stack=["Web Development", "Networking", "Cybersecurity", "Cloud Computing"],
    github_username="dez253",
    fun_fact="can say the alphabet backwards"
)

profile.show_stack()

print(profile.introduce())

print(profile.display_profile())

print("GitHub Link :https://github.com/dez253")