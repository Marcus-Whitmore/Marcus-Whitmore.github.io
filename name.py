import json
import os.path


class LoadWorkDumpProgram:
    file_path = None

    def load(self):
        """
        If `file_path` is provided, and a file
        exists for that path, return the contents
        of that file after `json.load`ing.
        """
        if self.file_path is None:
            return

        if not os.path.exists(self.file_path):
            return

        with open(self.file_path) as file:
            return json.load(file)

    def work(self):
        """
        By default, this method does nothing.
        It is intended for subclasses to override
        this method.

        `self.data` will be populated before this method is called.
        After the method returns, `self.data` will be dumped to
        the specified file.
        """
        pass

    def dump(self):
        """
        If `file_path` is defined, `data` will be
        `json.dump`ed to that file.
        """
        if self.file_path is None:
            return

        with open(self.file_path, "w") as file:
            json.dump(self.data, file)

    def run(self):
        self.data = self.load()
        self.work()
        self.dump()


# ^^^ Nate's job ^^^
# vvv Your job vvv


class DecadesOldProgram(LoadWorkDumpProgram):
    file_path = "last_user.json"

    def work(self):
        name = input("Name: ")
        age = int(input("Age: "))
        print(f"{name}, you are {age // 10} decades old")

        last_user = self.data
        self.data = {"name": name, "age": age}

        if last_user is None:
            print("You are the first person to sign in!")
        else:
            print(f"The last user was {last_user['name']}.")
            print(f"They were {last_user['age'] // 10} decades old")


class StepProgram3(LoadWorkDumpProgram):
    file_path = "last_user.json"

    def work(self):

        name = input("Name: ")
        age = int(input("Age: "))
        print(f" Hello {name}, you are {age // 10} decades old")

        if self.data is None:
            self.data = []

        else:
            for user in self.data:
                print(user["name"], user["age"] // 10)
        self.data.append({"name": name, "age": age})


def main():
    program = StepProgram3()
    program.run()


if __name__ == "__main__":
    main()
