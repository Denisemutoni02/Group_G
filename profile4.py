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
        print("\nMy Tech Stack:")
        for i, tool in enumerate(self.tech_stack, start=1):
            print(f"{i}. {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"


if __name__ == "__main__":
   
    my_profile = Profile(
        name="Mwiza Dorothy",
        favorite_language="taking pics",
        hobby="traveling",
        tech_stack=["HTML", "CSS", "Node.js", "JavaScript", "React"],
        github_username="mwii520",
        fun_fact="I once stayed up all night just to fix one stubborn bug!"
    )

    
    my_profile.introduce()
    my_profile.show_stack()
    print("My GitHub Profile link is :https://github.com/mwii520")
