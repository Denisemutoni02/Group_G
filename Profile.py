

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")

    def show_stack(self):
        print("My tech stack includes:")
        for tool in self.tech_stack:
            print(f" - {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"



tumwine_profile = Profile(
    name="Tumwine Timothy",
    favorite_language="Python",
    hobby="watching football, fighting, and smashing things",
    tech_stack=["Python", "cybersecurity", "Git", "HTML", "CSS"],
    github_username="ETRBIU", 
    fun_fact="I once fixed a bug by accident and pretended it was intentional!"
)


tumwine_profile.introduce()
tumwine_profile.show_stack()
print("My github profile link is :https://github.com/ETRBIU")
