from typing import Optional

import environ
import pandas as pd
from django.contrib.auth.models import User

from annotations.db.notia import DBPopulatorInterface
from annotations.db.notia.utils import read_dataset_as_csv


class DBPopulator_auth_user(DBPopulatorInterface):
    def execute(self) -> None:
        sheet_df = self.__get_auth_user_df()

        if sheet_df is None:
            return

        index_list = sheet_df.index.values.tolist()
        for i in index_list:
            item = sheet_df.iloc[i]
            self.__handle_auth_user_creation(item)

    def __get_auth_user_df(self) -> Optional[pd.DataFrame]:
        file_path = "data/db/auth_user.csv"
        password = self.__get_password()

        if password == None:
            return None

        sheet_df = read_dataset_as_csv(file_path)
        sheet_df["password"] = [password]

        return sheet_df

    def __handle_auth_user_creation(self, item: pd.Series) -> None:
        self.__get_or_create_user(item)

    def __get_or_create_user(self, item: pd.Series) -> User:
        try:
            user = User.objects.get(username=item["username"])
        except User.DoesNotExist:
            dataset = {
                "username": item["username"],
                "email": item["email"],
                "password": item["password"],
                "first_name": item["first_name"],
                "last_name": item["last_name"],
            }
            if item["is_superuser"]:
                user = User.objects.create_superuser(**dataset)
            else:
                user = User.objects.create_user(**dataset)

        print(f"# {user.pk} (User)")

        return user

    def __get_password(self) -> Optional[str]:
        env = environ.Env()
        password = None

        environ.Env.read_env()
        try:
            password = env("DJANGO_SUPERUSER_PASSWORD")
        except Exception as e:
            print(f"# ERROR: {e}")

        return password
