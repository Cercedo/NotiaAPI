from typing import Any, List

from annotations.db.notia.populators import DBPopulator_auth_user


class HandlerNotiaDB:
    """
    Main class for setting up and creating required "Notia"
    application's data.
    """

    def start(self) -> None:
        print(
            f"####----<><><><> START {HandlerNotiaDB.__name__} -----------------------------------------"
        )

        DBHandler_list = self.__get_class_handler_list()

        for DBHandler in DBHandler_list:
            print(f"\n####---- {DBHandler.execute.__qualname__}")
            DBHandler.execute()

        print(
            f"####----<><><><> END {HandlerNotiaDB.__name__} -------------------------------------------"
        )

    def __get_class_handler_list(self) -> List[Any]:
        """
        Notes:
        - Given that some instances have related fields, take care of
          modifying the current list order.
        """

        handler_list = [
            DBPopulator_auth_user(),
        ]
        return handler_list


def main() -> None:
    DB_handler = HandlerNotiaDB()
    DB_handler.start()


if __name__ == "__main__":
    main()
