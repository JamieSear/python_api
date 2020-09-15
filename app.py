from api import fetch_user_data
from repos import Repos


class CLI():

    ''' User interface '''

    def __init__(self):
        self._user_input = ""

    def start(self):
        print('Welcome to the GitHub Repo CLI')
        self.get_user_name()

    def get_user_name(self):
        try:
            self._user_input = input('Please enter your GitHub username. \n')
            fetch_user_data(self._user_input)
            self.menu()
            self.get_user_choice()

        except:
            print('Please enter a valid GitHub username')

    def menu(self):
        for idx, repo in enumerate(Repos.all, start=1):
            print(f'{idx}. {repo.get_name()}')

    def get_user_choice(self):
        try:
            self._user_choice = input(
                'Which number repo would you like to view?')
            self.show_repo(self._user_choice)
        except:
            print('Please select a number from the options above')

    def show_repo(self, choice):
        repo = Repos.find_by_input(choice)
        print(f'Name:{repo.get_name()}')
        print(f'Description:{repo.get_description()}')
        print(f'URL:{repo.get_url()}')


CLI().start()
