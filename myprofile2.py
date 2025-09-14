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
        print(f"Fun fact: {self.fun_fact}")

    def show_stack(self):
        print("My tech stack includes:")
        for tool in self.tech_stack:
            print(f"- {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"



if __name__ == "__main__":
    my_profile = Profile(
        name="Mutoni_Denise",
        favorite_language="Python",
        hobby="Watching_movies",
        tech_stack=["Python", "Django", "Git"],
        github_username="Denisemutoni02",
        fun_fact="I_laugh_at_my_jokes_before_saying_them!"
    )

    my_profile.introduce()
    my_profile.show_stack()
    print("My GitHub profile:", my_profile.github_link())

