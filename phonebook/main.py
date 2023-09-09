from pathlib import Path

from typing import List


class Phonebook:
    def __init__(self, name):
        self.name = name


class PhonebookEntry:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number


class PhonebookRepository:
    def create_new_phonebook(self, phonebook: Phonebook) -> None:
        pass

    def save_phonebook_entry(self, phonebook: Phonebook, entry: PhonebookEntry) -> None:
        pass

    def delete_phonebook_entry(self, phonebook: Phonebook, entry: PhonebookEntry) -> None:
        pass

    def get_phonebook(self, phonebook: Phonebook) -> List[PhonebookEntry]:
        pass


class FilePhonebookRepository(PhonebookRepository):
    def __init__(self, base_dir: str):
        self.base_dir: str = base_dir

    def get_file_name(self, phonebook) -> str:
        return f"{self.base_dir}/{phonebook.name}.txt"

    @staticmethod
    def entry_formatter(entry: PhonebookEntry):
        return f"{entry.name},{entry.surname},{entry.phone_number}\n"

    def create_new_phonebook(self, phonebook: Phonebook) -> None:
        Path(self.base_dir).mkdir(parents=True, exist_ok=True)
        with open(self.get_file_name(phonebook), 'w') as _:
            pass

    def save_phonebook_entry(self, phonebook: Phonebook, entry: PhonebookEntry) -> None:
        with open(self.get_file_name(phonebook), 'a') as file:
            file.write(FilePhonebookRepository.entry_formatter(entry))

    def delete_phonebook_entry(self, phonebook: Phonebook, entry: PhonebookEntry) -> None:
        with open(self.get_file_name(phonebook), 'r') as file:
            all_lines = file.readlines()
            with open(self.get_file_name(phonebook), 'w') as file:
                for line in all_lines:
                    if line != FilePhonebookRepository.entry_formatter(entry):
                        file.write(line)

    def get_phonebook(self, phonebook: Phonebook) -> List[PhonebookEntry]:
        result = []
        with open(self.get_file_name(phonebook), 'r') as file:
            for line in file.readlines():
                result.append(line.replace("\n", ""))
        return result


if __name__ == '__main__':
    repo = FilePhonebookRepository("base_dir")

    new_phonebook_name = ""
    while new_phonebook_name == "":
        new_phonebook_name = input("Please provide the your PhoneBook Name")

    new_phonebook = Phonebook(new_phonebook_name)
    repo.create_new_phonebook(new_phonebook)

    while True:
        ops = input("""
        what do you want to do on your phonebook?:
        operation allowed:
        s -> save a new phonebook entry
        d -> delete a phonebook entry
        r -> read the full phonebook
        q -> quite
        """)

        if ops == "s":
            contact_name = input("Please provide the contact name")
            contact_surname = input("Please provide the contact surname")
            contact_phone = input("Please provide the contact phone number")

            repo.save_phonebook_entry(new_phonebook, PhonebookEntry(contact_name, contact_surname, contact_phone))
        elif ops == "d":
            contact_name = input("Please provide the contact name")
            contact_surname = input("Please provide the contact surname")
            contact_phone = input("Please provide the contact phone number")

            repo.delete_phonebook_entry(new_phonebook, PhonebookEntry(contact_name, contact_surname, contact_phone))
            contact_phone = input("Please provide the contact phone number")
        elif ops == "r":
            print(repo.get_phonebook(new_phonebook))
        elif ops == "q":
            break
        else:
            print("operation not allowed")
